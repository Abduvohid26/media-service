import aiohttp.web as http
import traceback
import os
from .track import track_search, track_download_telegram, \
    track_recognize_by_multipart_reader, track_recognize_by_link, \
    track_popular_tracks, track_download
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
   - in: query
     name: proxy
     schema:
       type: string
  """

  query = request.query.get("query", "")
  offset = request.query.get("offset", "0")
  limit = request.query.get("limit", "10")
  proxy = request.query.get("proxy", None)

  if not (offset.isnumeric() and limit.isnumeric()):
    return http.json_response({"error": "Invalid parameters"}, status=http.HTTPBadRequest.status_code)

  try:
    search_results = await track_search(query, int(offset), int(limit), proxy)
    return http.json_response({"search_results": search_results})
  except Exception as ex:
    await report("track-search", f"Unable to search (Query: {query}, Offset: {offset}, Limit: {limit})", str(ex))
    return http.json_response({"error": "Unable to search"}, status=http.HTTPInternalServerError.status_code)

async def track_download_telegram_route_handler(request: http.Request):
  """
   description: Track download by telegram
   tags:
   - Track
   produces:
   - application/json
   parameters:
   - in: query
     name: id
     description: Track id
     schema:
       type: string
   - in: query
     name: telegram_bot_token
     description: Telegram bot token
     schema:
       type: string
   - in: query
     name: telegram_bot_username
     description: Telegram bot username
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
  """

  id = request.query.get("id", "")
  telegram_bot_token = request.query.get("telegram_bot_token", "")
  telegram_bot_username = request.query.get("telegram_bot_username", "")
  telegram_bot_server = request.query.get("telegram_bot_server", None)
  source_address = request.query.get("source_address", None)
  proxy = request.query.get("proxy", None)

  if not telegram_bot_token:
    return http.json_response({"error": "Telegram bot token is not provided"}, status=http.HTTPBadRequest.status_code)

  try:
    file_id = await track_download_telegram(id, telegram_bot_token, telegram_bot_username, telegram_bot_server, source_address=source_address, proxy=proxy)
    return http.json_response({"file_id": file_id})
  except Exception as ex:
    await report("track-download-telegram", f"Unable to download track (ID: {id}, Telegram bot server: {telegram_bot_server}, Telegram bot token: {telegram_bot_token}, Source address: {source_address}, Proxy: {proxy})", traceback.format_exc())
    return http.json_response({"error": str(ex)})

async def track_recognize_by_file_route_handler(request: http.Request):
  reader = await request.multipart()

  file = await reader.next()
  if not file.name == "file":
    return http.json_response({"error": "Invalid file"}, status=http.HTTPBadRequest.status_code)

  try:
    recognize_result = await track_recognize_by_multipart_reader(file)
    status_code = http.HTTPNotFound.status_code if not recognize_result else http.HTTPOk.status_code
    return http.json_response({"recognize_result": recognize_result}, status=status_code)
  except Exception as ex:
    await report("track-recognize-by-file", f"Unable to recognize by file", str(ex))
    return http.json_response({"error": str(ex)}, status=http.HTTPInternalServerError.status_code)

async def track_recognize_by_link_route_handler(request: http.Request):
  """
   description: Track recognize by link
   tags:
   - Track
   produces:
   - application/json
   parameters:
   - in: query
     name: link
     description: Link
     schema:
       type: string
  """
  link = str(request.query.get("link", ""))

  if not link:
    return http.json_response({"error": "link parameter is missing"})

  try:
    recognize_result = await track_recognize_by_link(link)
    return http.json_response({"recognize_result": recognize_result})
  except Exception as ex:
    await report("track-recognize-by-link", f"Unable to recognize by link", traceback.format_exc())
    return http.json_response({"error": str(ex)}, status=http.HTTPInternalServerError.status_code)

async def track_popular_route_handler(request: http.Request):
  """
   description: Track popular
   tags:
   - Track
   produces:
   - application/json
   parameters:
   - in: query
     name: country_code
     description: Country code
     schema:
       type: string
   - in: query
     name: offset
     description: Offset
     schema:
       type: number
   - in: query
     name: limit
     description: Limit
     schema:
       type: number
  """
  country_code = request.query.get("country_code", "")
  offset = int(request.query.get("offset", 0))
  limit = int(request.query.get("limit", 10))

  country_code = country_code.replace("en", "us")
  country_code = country_code.upper()

  try:
    popular_tracks = await track_popular_tracks(country_code, offset, limit)
    return http.json_response({"popular_tracks": popular_tracks})
  except Exception as ex:
    await report("track-popular", f"Unable to get popular tracks", traceback.format_exc())
    return http.json_response({"error": str(ex)}, status=http.HTTPInternalServerError.status_code)

async def track_download_route_handler(request: http.Request):
  """
   description: Track download
   tags:
   - Track
   produces:
   - application/json
   parameters:
   - in: query
     name: id
     description: Track id
     schema:
       type: string
  """
  id = request.query.get("id", "")

  try:
    track_path = await track_download(id)
    return http.json_response({"file_name": os.path.basename(track_path)})
  except Exception as ex:
    await report("track-download", f"Unable to get download track", traceback.format_exc())
    return http.json_response({"error": str(ex)}, status=http.HTTPInternalServerError.status_code)