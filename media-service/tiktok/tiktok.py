import typing
import random
import aiohttp
import pathlib
import os
import secrets
from telegram import Bot
from yarl import URL
from ..backend_apishop.tiktok_link_get import tiktok_backend_apishop_link_get
import traceback

MEDIA_SERVICE_DEFAULT_TELEGRAM_BOT_SERVER = os.environ.get("MEDIA_SERVICE_DEFAULT_TELEGRAM_BOT_SERVER")

async def tiktok_link_get(link: str) -> str:
  return await tiktok_backend_apishop_link_get(link)

async def tiktok_download_telegram(
    link: str,
    telegram_bot_token: str,
    telegram_bot_server: typing.Union[str, None] = None,
    chat_id: typing.List[int] = [5700964012],
) -> typing.Union[str, dict]:
    tiktok_post = await tiktok_link_get(link)
    print(tiktok_post, "POST")

    telegram_bot = Bot(
        token=telegram_bot_token,
        base_url=telegram_bot_server or MEDIA_SERVICE_DEFAULT_TELEGRAM_BOT_SERVER,
    )
    chat_id_to_send_to = random.choice(chat_id)
    temp_file_path = os.path.join("/tmp/", secrets.token_hex(8))
    file_id = None

    try:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(100)) as http_session:
            async with http_session.get(URL(tiktok_post["download_url"], encoded=True)) as http_response:
                if http_response.status != 200:
                    raise Exception(f"Failed to download video: {http_response.status}")

                with open(temp_file_path, "wb") as fd:
                    async for chunk in http_response.content.iter_chunked(2048):
                        fd.write(chunk)

            with open(temp_file_path, "rb") as fd:
                fd.seek(0)

                if tiktok_post["type"] == "photo":
                    sent_photo = await telegram_bot.send_photo(chat_id_to_send_to, photo=fd)
                    file_id = sent_photo.photo[0].file_id
                else:
                    # async with http_session.get(URL(tiktok_post["thumbnail_url"])) as thumb_response:
                    #     if thumb_response.status != 200:
                    #         raise Exception("Failed to download thumbnail")
                    #     thumbnail = await thumb_response.read()

                    fd.seek(0)
                    sent_video = await telegram_bot.send_video(
                        chat_id_to_send_to, video=fd, supports_streaming=True, thumbnail=tiktok_post["thumbnail_url"]
                    )
                    file_id = sent_video.video.file_id
        return file_id

    except Exception as e:
        print("❌ Error during TikTok download:", str(e))
        traceback.print_exc()
        return {"success": False, "error": str(e)}

    finally:
        # Faylni har doim o'chirish (hatto xatolik bo'lsa ham)
        pathlib.Path(temp_file_path).unlink(missing_ok=True)




# async def tiktok_download_telegram(
#   link: str,
#   telegram_bot_token: str,
#   telegram_bot_server: typing.Union[str, None] = None,
#   # chat_id: typing.List[int] = [7248129579, 7452580556, 6315794948, 7303643228, 7231662235, 6999114299, 7526375141, 343103355, 1757611067]
#   chat_id: typing.List[int] = [5700964012,],

# ) -> str:
#   tiktok_post = await tiktok_link_get(link)
#   print(tiktok_post, "POST")
#   telegram_bot = Bot(token=telegram_bot_token, base_url=telegram_bot_server or MEDIA_SERVICE_DEFAULT_TELEGRAM_BOT_SERVER)

#   chat_id_to_send_to = random.choice(chat_id)
#   temp_file_path = os.path.join("/tmp/", secrets.token_hex(8))

#   file_id = None
#   async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(32)) as http_session:
#     async with http_session.get(URL(tiktok_post["download_url"], encoded=True)) as http_response:
#       with open(temp_file_path, "wb") as fd:
#         async for chunk in http_response.content.iter_chunked(2048):
#           fd.write(chunk)

#       with open(temp_file_path, "rb") as fd:
#         if tiktok_post["type"] == "photo":
#           sent_photo = await telegram_bot.send_photo(chat_id_to_send_to, photo=fd)
#           file_id = sent_photo.photo[0].file_id
#         else:
#           async with aiohttp.ClientSession() as http_session:
#             async with http_session.get(URL(tiktok_post["thumbnail_url"])) as http_response:
#               thumbnail = await http_response.read()
#               sent_video = await telegram_bot.send_video(chat_id_to_send_to, video=fd, supports_streaming=True, thumbnail=thumbnail)
#               file_id = sent_video.video.file_id

#   pathlib.Path(temp_file_path).unlink(missing_ok=True)
#   return file_id
