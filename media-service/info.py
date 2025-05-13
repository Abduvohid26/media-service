import aiohttp.web as http
import traceback
from .backend_apishop.media_info import media_backend_apishop_info

async def media_info(link: str):
  return await media_backend_apishop_info(link)

async def media_info_route_handler(request: http.Request):
  """
   description: Media info
   produces:
   - application/json
   parameters:
   - in: query
     name: link
     description: Link to fetch info from
     schema:
       type: string
  """
  link = request.query.get("link")

  try:
    info = await media_info(link)
    return http.json_response({"info": info})
  except:
    return http.json_response({"error": traceback.format_exc()})