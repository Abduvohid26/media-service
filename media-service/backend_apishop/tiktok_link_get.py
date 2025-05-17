import aiohttp
import re
# def _tiktok_deserialize(data):
#   non_watermark_formats = filter(lambda format:  format["quality"], data["medias"])

#   return {
#     "id": data["id"],
#     "type": "video",
#     "download_url": next(non_watermark_formats)["url"],
#     "thumbnail_url": data["thumbnail"]
#   }

# async def tiktok_backend_apishop_link_get(link: str):
#   params = {"url": link}
#   async with aiohttp.ClientSession("https://full.apishop.uz") as http_session:
#     async with http_session.get("/get-media-info", params=params) as http_response:
#       json_response = await http_response.json()
#       print(json_response, "js res")
#       return _tiktok_deserialize(json_response) 



def get_tiktok_id(url: str) -> str | None:
    pattern = r'/v/(\d+)\.html'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

    
def _tiktok_deserialize(data, link):
    medias = data.get("medias", [])
    if not medias:
        raise ValueError("No medias found in data")

    first_media = medias[0]
    media_type = first_media.get("type", "video")

    result = {
        "id": get_tiktok_id(link),
        "type": media_type,
    }

    if media_type == "video":
        result.update({
            "download_url": first_media.get("download_url"),
            "thumbnail_url": first_media.get("thumb"),
        })
    elif media_type == "photo":
        result.update({
            "download_url": first_media.get("download_url") or first_media.get("thumb"),
            "thumbnail_url": first_media.get("thumb"),
        })
    else:
        result.update({
            "info": first_media
        })

    return result

async def tiktok_backend_apishop_link_get(link: str):
  params = {"tk_url": link}
  async with aiohttp.ClientSession("https://fast.videoyukla.uz") as http_session:
    async with http_session.get("/tiktok/media/", params=params) as http_response:
      json_response = await http_response.json()
      return _tiktok_deserialize(json_response, link)
    


