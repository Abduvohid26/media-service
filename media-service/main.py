import aiohttp.web as http
import os
from aiohttp_swagger import *

from .track.routes import track_search_route_handler, track_download_telegram_route_handler, \
    track_recognize_by_file_route_handler, track_recognize_by_link_route_handler, track_popular_route_handler, \
    track_download_route_handler
from .youtube.routes import youtube_download_telegram_route_handler
from .instagram.routes import instagram_link_route_handler, instagram_download_telegram_route_handler
from .tiktok.routes import tiktok_link_route_handler, tiktok_download_telegram_route_handler
from .info import media_info_route_handler

async def files_route_handler(request: http.Request):
  file_name = request.match_info["name"]
  return http.FileResponse(os.path.join("/media-service-files/", file_name))

async def main():
  http_server = http.Application()

  http_server.add_routes([
    http.get("/track-search", track_search_route_handler),
    http.get("/track-download-telegram", track_download_telegram_route_handler),
    http.get("/track-download", track_download_route_handler),
    http.get("/track-popular", track_popular_route_handler),
    http.post("/track-recognize-by-file", track_recognize_by_file_route_handler),
    http.post("/track-recognize-by-link", track_recognize_by_link_route_handler),

    http.get("/youtube-download-telegram", youtube_download_telegram_route_handler),

    http.get("/instagram-link", instagram_link_route_handler),
    http.get("/instagram-download-telegram", instagram_download_telegram_route_handler),

    http.get("/tiktok-link", tiktok_link_route_handler),
    http.get("/tiktok-download-telegram", tiktok_download_telegram_route_handler),

    http.get("/info", media_info_route_handler),
    http.get("/files/{name}", files_route_handler)
  ])

  setup_swagger(http_server, swagger_url="/docs", ui_version=2, title="Media service API documentation")

  return http_server
