import aiohttp

def _instagram_deserialize(data):
  if data["type"] == "album":
    collection_items = [{
      "id": f"{data['shortcode']}.{index}",
      "type": "photo" if media["type"] == "image" else "video",
      "download_url": media["download_url"],
      "thumbnail_url": media["thumb"],
    } for index, media in enumerate(data["medias"])]

    return {
      "id": data["shortcode"],
      "type": "collection",
      "collection": collection_items
    }

  return {
    "id": data["shortcode"],
    "type": "photo" if data["type"] == "image" else "video",
    "download_url": data["download_url"],
    "thumbnail_url": data["thumb"],
  }

def _instagram_deserialize2(data):
  if data["type"] == "album":
    collection_items = [{
      "id": f"{data['shortcode']}.{index}",
      "type": "photo" if media["type"] == "image" else "video",
      "download_url": media["download_url"],
      "thumbnail_url": media["thumb"],
    } for index, media in enumerate(data["medias"])]

    return {
      "id": data["shortcode"],
      "type": "collection",
      "collection": collection_items
    }

  return {
    "id": data["shortcode"],
    "type": "photo" if data["type"] == "image" else "video",
    "download_url": data["medias"][0]["download_url"],
    "thumbnail_url": data["medias"][0]["thumb"],
  }

async def instagram_backend_apishop_link_get(link: str):
  params = {"url": link}
  async with aiohttp.ClientSession("https://full.apishop.uz") as http_session:
    async with http_session.get("/get-media-info", params=params) as http_response:
      json_response = await http_response.json()
      return _instagram_deserialize(json_response)

# async def instagram_backend_apishop_link_get(link: str):
#   params = {"in_url": link}
#   async with aiohttp.ClientSession("https://fast.videoyukla.uz") as http_session:
#     async with http_session.get("/instagram/media", params=params) as http_response:
#       json_response = await http_response.json()
#       return _instagram_deserialize2(json_response)