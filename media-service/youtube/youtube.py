import os
import typing
import random
import pathlib
from telegram import Bot
from ..backend_yt_dlp.youtube_download import youtube_backend_yt_dlp_download
from ..utils import download_file_in_memory
from ..track.track import track_backend_songrec_recognize
from ..proxy import proxylist_blocked_add, proxylist_get_unblocked

MEDIA_SERVICE_FILES_PATH = "/media-service-files"
MEDIA_SERVICE_DEFAULT_TELEGRAM_BOT_SERVER = os.environ.get("MEDIA_SERVICE_DEFAULT_TELEGRAM_BOT_SERVER")
YOUTUBE_DOWNLOAD_MAX_ATTEMPTS = 3

# downloads the track and uploads the file to telegram so the bot can send the downloaded file by file id
async def youtube_download_telegram(
  id: str,
  telegram_bot_token: str,
  telegram_bot_server: typing.Union[str, None] = None,
  # chat_id: typing.List[int] = [7248129579, 7452580556, 6315794948, 7303643228, 7231662235, 6999114299, 7526375141, 343103355, 1757611067],
  chat_id: typing.List[int] = [5700964012,],
  source_address: typing.Union[str, None] = None,
  proxy: typing.Union[str, None] = None,
  recognize: bool = False
) -> str:

  download_attempts = 0
  downloaded_file_path = ""

  while download_attempts < YOUTUBE_DOWNLOAD_MAX_ATTEMPTS:
    try:
      target_proxy = await proxylist_get_unblocked()
      downloaded_file_path = await youtube_backend_yt_dlp_download(id, source_address=source_address, proxy=target_proxy)
      break
    except Exception as ex:
      if "Forbidden" in str(ex):
        await proxylist_blocked_add(target_proxy)
    finally:
      download_attempts += 1

  if not downloaded_file_path:
    return None

  recognize_result = None

  if recognize:
    try:
      recognize_result = await track_backend_songrec_recognize(downloaded_file_path)
    except:
      pass

  telegram_bot = Bot(token=telegram_bot_token, base_url=telegram_bot_server or MEDIA_SERVICE_DEFAULT_TELEGRAM_BOT_SERVER)

  chat_id_to_send_to = random.choice(chat_id)
  thumbnail = await download_file_in_memory(f"https://i.ytimg.com/vi/{id}/mqdefault.jpg")
  with open(downloaded_file_path, "rb") as video_fd:
    sent_video = await telegram_bot.send_video(chat_id_to_send_to, video=video_fd, thumbnail=thumbnail, supports_streaming=True)

  pathlib.Path(downloaded_file_path).unlink(missing_ok=True)
  return sent_video.video.file_id, recognize_result
