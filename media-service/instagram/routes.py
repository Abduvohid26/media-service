import aiohttp.web as http
from .instagram import instagram_link_get, instagram_download_telegram
from ..report import report

async def instagram_link_route_handler(request: http.Request):
  """
   description: Instagram link get
   tags:
   - Instagram
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
    instagram_link = await instagram_link_get(link)
    return http.json_response(instagram_link)
  except Exception as ex:
    return http.json_response({"error": ex})
    
async def instagram_download_telegram_route_handler(request: http.Request):
  """
   description: Instagram download by telegram
   tags:
   - Instagram
   produces:
   - application/json
   parameters:
   - in: query
     name: link
     description: Instagram link
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
   - in: query
     name: index
     description: Collection item index
     schema:
       type: number
  """

  link = request.query.get("link", "")
  index = int(request.query.get("index", 0))
  telegram_bot_token = request.query.get("telegram_bot_token", "")
  telegram_bot_server = request.query.get("telegram_bot_server", None)
  
  if not telegram_bot_token:
    return http.json_response({"error": "Telegram bot token is not provided"}, status=http.HTTPBadRequest.status_code)
  
  try:
    file_id = await instagram_download_telegram(link, telegram_bot_token, telegram_bot_server, index=index)
    return http.json_response({"file_id": file_id})
  except Exception as ex:
    await report("instagram-download-telegram", f"Unable to download instagram to telegram (Link: {link}, Index: {index})", str(ex))
    return http.json_response({"error": str(ex)}, status=http.HTTPInternalServerError.status_code)