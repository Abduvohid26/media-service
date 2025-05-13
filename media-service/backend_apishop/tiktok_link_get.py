import aiohttp

def _tiktok_deserialize(data):
  non_watermark_formats = filter(lambda format: "no_watermark" in format["quality"], data["medias"])

  return {
    "id": data["id"],
    "type": "video",
    "download_url": next(non_watermark_formats)["url"],
    "thumbnail_url": data["thumbnail"]
  }

async def tiktok_backend_apishop_link_get(link: str):
  params = {"url": link}
  async with aiohttp.ClientSession("https://full.apishop.uz") as http_session:
    async with http_session.get("/get-media-info", params=params) as http_response:
      json_response = await http_response.json()
      return _tiktok_deserialize(json_response) 