import typing
import random
import aiohttp
import pathlib
import os
import secrets
from telegram import Bot
from yarl import URL
from ..backend_apishop.instagram_link_get import instagram_backend_apishop_link_get

MEDIA_SERVICE_DEFAULT_TELEGRAM_BOT_SERVER = os.environ.get("MEDIA_SERVICE_DEFAULT_TELEGRAM_BOT_SERVER")

async def instagram_link_get(link: str) -> str:
  return await instagram_backend_apishop_link_get(link)

async def instagram_download_telegram(
  link: str,
  telegram_bot_token: str,
  telegram_bot_server: typing.Union[str, None] = None,
  chat_id: typing.List[int] = [7248129579, 7452580556, 6315794948, 7303643228, 7231662235, 6999114299, 7526375141, 343103355, 1757611067],
  index: typing.Union[int] = 0
) -> str:
  instagram_post = await instagram_link_get(link)

  if instagram_post["type"] == "collection":
    instagram_post = instagram_post["collection"][index]

  telegram_bot = Bot(token=telegram_bot_token, base_url=telegram_bot_server or MEDIA_SERVICE_DEFAULT_TELEGRAM_BOT_SERVER)

  chat_id_to_send_to = random.choice(chat_id)
  temp_file_path = os.path.join("/tmp/", secrets.token_hex(8))

  file_id = None

  if instagram_post["type"] == "photo":
    sent_photo = await telegram_bot.send_photo(chat_id_to_send_to, photo=instagram_post["download_url"])
    file_id = sent_photo.photo[0].file_id
  else:
    sent_video = await telegram_bot.send_video(chat_id_to_send_to, video=instagram_post["download_url"])
    file_id = sent_video.video.file_id

  #  async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(32)) as http_session:
  #    async with http_session.get(URL(instagram_post["download_url"], encoded=True)) as http_response:
  #      with open(temp_file_path, "wb") as fd:
  #        async for chunk in http_response.content.iter_chunked(2048):
  #          fd.write(chunk)

  #      with open(temp_file_path, "rb") as fd:
  #        if instagram_post["type"] == "photo":
  #          sent_photo = await telegram_bot.send_photo(chat_id_to_send_to, photo=fd)
  #          file_id = sent_photo.photo[0].file_id
  #        else:
  #          async with aiohttp.ClientSession() as http_session:
  #            async with http_session.get(URL(instagram_post["thumbnail_url"])) as http_response:
  #              thumbnail = await http_response.read()
  #              sent_video = await telegram_bot.send_video(chat_id_to_send_to, video=fd, supports_streaming=True, thumbnail=thumbnail)
  #              file_id = sent_video.video.file_id

  pathlib.Path(temp_file_path).unlink(missing_ok=True)
  return file_id
