import aiohttp.web as http
import traceback
from .tiktok import tiktok_download_telegram, tiktok_link_get
from ..report import report
import logging
logger = logging.getLogger(__name__)
async def tiktok_link_route_handler(request: http.Request):
  """
   description: Tiktok link get
   tags:
   - Tiktok
   produces:
   - application/json
   parameters:
   - in: query
     name: link
     schema:
       type: string
  """

  link = request.query.get("link", "10")

  try:
    tiktok_link = await tiktok_link_get(link)
    return http.json_response(tiktok_link)
  except Exception as ex:
    logger.error(traceback.format_exc())
    return http.json_response({"error": str(ex)})
    
async def tiktok_download_telegram_route_handler(request: http.Request):
  """
   description: Tiktok download by telegram
   tags:
   - Tiktok
   produces:
   - application/json
   parameters:
   - in: query
     name: link
     description: tiktok link
     schema:
       type: string
   - in: query
     name: telegram_bot_token
     description: Telegram bot token
     schema:
       type: string
   - in: query
     name: telegram_bot_server_url
     description: Telegram bot server url
     schema:
       type: string
  """

  link = request.query.get("link", "")
  telegram_bot_token = request.query.get("telegram_bot_token", "")
  telegram_bot_server = request.query.get("telegram_bot_server", None)
  
  if not telegram_bot_token:
    return http.json_response({"error": "Telegram bot token is not provided"}, status=http.HTTPBadRequest.status_code)
  
  try:
    file_id = await tiktok_download_telegram(link, telegram_bot_token, telegram_bot_server)
    return http.json_response({"file_id": file_id})
  except Exception as ex:
    await report("tiktok-download-telegram", f"Unable to download tiktok to telegram (Link: {link})", traceback.format_exc())
    return http.json_response({"error": str(ex)}, status=http.HTTPInternalServerError.status_code)