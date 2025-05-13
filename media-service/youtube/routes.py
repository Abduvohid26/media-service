import aiohttp.web as http
import traceback
import os
from .youtube import youtube_download_telegram
from ..report import report

async def track_search_route_handler(request: http.Request):
  """
   description: Track search
   tags:
   - Track
   produces:
   - application/json
   parameters:
   - in: query
     name: query
     schema:
       type: string
   - in: query
     name: offset
     schema:
       type: string
   - in: query
     name: limit
     schema:
       type: string
  """

  query = request.query.get("query", "")
  offset = request.query.get("offset", "0")
  limit = request.query.get("limit", "10")

  if not (offset.isnumeric() and limit.isnumeric()):
    return http.json_response({"error": "Invalid parameters"}, status=http.HTTPBadRequest.status_code)

  try:
    search_results = await track_search(query, offset, limit)
    return http.json_response({"search_results": search_results})
  except:
    return http.json_response({"error": "Internal server error"})

async def youtube_download_telegram_route_handler(request: http.Request):
  """
   description: YouTube download by telegram
   tags:
   - YouTube
   produces:
   - application/json
   parameters:
   - in: query
     name: id
     description: Youtube video id
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
     name: source_address
     description: Soruce address
     schema:
       type: string
   - in: query
     name: proxy
     description: Proxy
     schema:
       type: string
   - in: query
     name: recognize
     description: Whether should recognize or not
     schema:
       type: boolean
  """

  id = request.query.get("id", "")
  telegram_bot_token = request.query.get("telegram_bot_token", None)
  telegram_bot_server = request.query.get("telegram_bot_server", None)
  source_address = request.query.get("source_address", None)
  proxy = request.query.get("proxy", None)
  recognize = bool(request.query.get("recognize", False))

  if not telegram_bot_token:
    return http.json_response({"error": "Telegram bot token is not provided"}, status=http.HTTPBadRequest.status_code)

  try:
    (file_id, recognize_result,) = await youtube_download_telegram(id, telegram_bot_token, telegram_bot_server, source_address=source_address, proxy=proxy, recognize=recognize)
    return http.json_response({"file_id": file_id, "recognize_result": recognize_result})
  except Exception as ex:
    await report("youtube-download-telegram", f"Unable to download {id}", traceback.format_exc())
    return http.json_response({"error": str(ex)})