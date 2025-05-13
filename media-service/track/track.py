import aiohttp
import typing
import random
import pathlib
import secrets
import os
import asyncio
import hashlib
import json
from ..backend_youtube_search.track_search import track_youtube_search_search
from ..backend_yt_dlp.track_download import track_backend_yt_dlp_download
from ..backend_yt_dlp.track_search import track_backend_yt_dlp_search
from ..backend_songrec.track_recognize import track_backend_songrec_recognize
from ..backend_shazamio.track_popular import track_backend_shazamio_popular
from ..utils import download_file_in_memory
from ..proxy import proxylist_blocked_add, proxylist_get_unblocked
from ..redis import redis

MEDIA_SERVICE_DEFAULT_TELEGRAM_BOT_SERVER = os.environ.get("MEDIA_SERVICE_DEFAULT_TELEGRAM_BOT_SERVER")

from telegram import Bot
from yarl import URL

MEDIA_SERVICE_FILES_PATH = "/media-service-files"
TRACK_DOWNLOAD_MAX_ATTEMPTS = 3

TRACK_SEARCH_CACHE = {}
async def track_search(query: str, offset: int, limit: int, proxy: typing.Union[str, None] = None):
  track_search_cache_key = f"track-search-cache-{hashlib.sha256(query.encode("utf-8")).hexdigest()}"

  track_search_cache = await redis.get(track_search_cache_key)

  if track_search_cache:
    track_search_cache = json.loads(track_search_cache)
    if len(track_search_cache) >= offset + limit:
      return track_search_cache[offset:offset+limit]

  search_results = await track_backend_yt_dlp_search(query, offset, limit)
  await redis.set(track_search_cache_key, json.dumps(search_results), ex=60*60*24)
  return search_results

# downloads the track and returns the name of the downloaded file
async def track_download(
  id: str,
  proxy: typing.Union[str, None] = None,
) -> str:
  download_attempts = 0
  downloaded_file_path = ""

  while download_attempts < TRACK_DOWNLOAD_MAX_ATTEMPTS:
    try:
      target_proxy = proxy or (await proxylist_get_unblocked())
      downloaded_file_path = await track_backend_yt_dlp_download(id, proxy=target_proxy)
      break
    except Exception as ex:
      if "Forbidden" in str(ex):
        await proxylist_blocked_add(target_proxy)
    finally:
      download_attempts += 1

  if not downloaded_file_path:
    return None

  return downloaded_file_path

# downloads the track and uploads the file to telegram so the bot can send the downloaded file by file id
async def track_download_telegram(
  id: str,
  telegram_bot_token: str,
  telegram_bot_username: str,
  telegram_bot_server: typing.Union[str, None] = None,
  chat_id: typing.List[int] = [7248129579, 7452580556, 6315794948, 7303643228, 7231662235, 6999114299, 7526375141, 343103355, 1757611067],
  source_address: typing.Union[str, None] = None,
  proxy: typing.Union[str, None] = None,
) -> str:
  telegram_bot = Bot(token=telegram_bot_token, base_url=telegram_bot_server or MEDIA_SERVICE_DEFAULT_TELEGRAM_BOT_SERVER)
  
  downloaded_file_path = await track_download(id, proxy)

  try:
    chat_id_to_send_to = random.choice(chat_id)
    thumbnail = await download_file_in_memory(f"https://i.ytimg.com/vi/{id}/mq1.jpg")
    with open(downloaded_file_path, "rb") as audio_fd:
      sent_audio = await telegram_bot.send_audio(chat_id_to_send_to, audio=audio_fd, thumbnail=thumbnail)
    return sent_audio.audio.file_id
  except:
    return None
  finally:
    if downloaded_file_path:
      pathlib.Path(downloaded_file_path).unlink(missing_ok=True)

# track recognize by file
async def track_recognize_by_multipart_reader(reader):
  temp_file_path = os.path.join("/media-service-files", secrets.token_hex(8) + reader.filename)
  with open(temp_file_path, "wb") as temp_fd:
    while True:
      chunk = await reader.read_chunk()
      if not chunk:
        break
      temp_fd.write(chunk)

  try:
    recognize_result = await track_backend_songrec_recognize(temp_file_path)
    pathlib.Path(temp_file_path).unlink(missing_ok=True)
    return recognize_result
  except:
    return None

async def track_recognize_by_link(link: str):
  file_name = secrets.token_hex(8)
  file_path = os.path.join(MEDIA_SERVICE_FILES_PATH, file_name)

  async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(240)) as http_session:
    async with http_session.get(URL(link, encoded=True)) as http_response:
      with open(file_path, "wb") as fd:
        async for chunk in http_response.content.iter_chunked(2048):
          fd.write(chunk)
  try:
    return await track_backend_songrec_recognize(file_path)
  finally:
    pathlib.Path(file_path).unlink(missing_ok=True)

POPULAR_TRACKS_CACHE = {}
async def track_popular_tracks(country_code: str, offset: int, limit: int):
  if country_code in POPULAR_TRACKS_CACHE and len(POPULAR_TRACKS_CACHE[country_code]) >= offset+limit:
    return POPULAR_TRACKS_CACHE[country_code][offset:offset+limit]

  popular_tracks = await track_backend_shazamio_popular(country_code, limit)
  search_results = await asyncio.gather(*[track_search(f"{track['title']} {track['performer']}", 0, 1) for track in popular_tracks])
  search_results = [search_result[0] for search_result in search_results if search_result]
  POPULAR_TRACKS_CACHE[country_code] = search_results
  return search_results