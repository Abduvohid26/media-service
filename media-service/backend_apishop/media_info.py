import aiohttp

def _media_info_instagram_deserialize(data):
  if data["type"] == "album":
    collection_items = [{
      "id": data["shortcode"],
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

def _media_info_twitter_deserialize(data):
  if data["type"] == "multiple":
    collection_items = [{
      "id": data['id'],
      "type": "photo" if media["type"] == "image" else "video",
      "download_url": media["url"],
      "thumbnail_url": None,
    } for index, media in enumerate(data["medias"])]

    return {
      "id": data["id"],
      "type": "collection",
      "collection": collection_items
    }

  return {
    "id": data["id"],
    "type": "photo" if data["medias"][0]["type"] == "image" else "video",
    "download_url": data["medias"][0]["url"],
    "thumbnail_url": None
  }

def _media_info_tumblr_deserialize(data):
  if data["type"] == "multiple":
    collection_items = [{
      "id": None,
      "type": "photo" if media["type"] == "image" else "video",
      "download_url": media["url"],
      "thumbnail_url": None,
    } for index, media in enumerate(data["medias"])]

    return {
      "id": data["id"],
      "type": "collection",
      "collection": collection_items
    }

  return {
    "id": None,
    "type": "photo" if data["medias"][0]["type"] == "image" else "video",
    "download_url": data["medias"][0]["url"],
    "thumbnail_url": None
  }

def _media_info_tiktok_deserialize(data):
  non_watermark_formats = filter(lambda format: "no_watermark" in format["quality"], data["medias"])

  return {
    "id": data["id"],
    "type": "video",
    "download_url": next(non_watermark_formats)["url"],
    "thumbnail_url": data["thumbnail"]
  }

def _media_info_likee_deserialize(data):
  return {
    "id": None,
    "type": "video",
    "download_url": data["medias"][0]["url"],
    "thumbnail_url": data["thumbnail"]
  }

def _media_info_pinterest_deserialize(data):
  return {
    "id": None,
    "type": "photo" if data["medias"][0]["type"] == "image" else "video",
    "download_url": data["medias"][0]["url"],
    "thumbnail_url": data["medias"][0]["thumbnail"] if "thumbnail" in data["medias"][0] else None
  }

def _media_info_facebook_deserialize(data):
  if data["type"] == "multiple":
    collection_items = [{
      "id": data["id"],
      "type": "photo" if media["type"] == "image" else "video",
      "download_url": media["url"],
      "thumbnail_url": None,
    } for index, media in enumerate(data["medias"])]

    return {
      "id": data["id"],
      "type": "collection",
      "collection": collection_items
    }

  return {
    "id": data["id"],
    "type": "photo" if data["medias"][0]["type"] == "image" else "video",
    "download_url": data["medias"][0]["url"],
    "thumbnail_url": None
  }

def _media_info_deserialize(data):
  if "hosting" in data and data["hosting"] == "instagram":
    return _media_info_instagram_deserialize(data)

  if "source" in data:
    if data["source"] == "x":
      return _media_info_twitter_deserialize(data)
    elif data["source"] == "tiktok":
      return _media_info_tiktok_deserialize(data)
    elif data["source"] == "likee":
      return _media_info_likee_deserialize(data)
    elif data["source"] == "tumblr":
      return _media_info_tumblr_deserialize(data)
    elif data["source"] == "pinterest":
      return _media_info_pinterest_deserialize(data)
    elif data["source"] == "facebook":
      return _media_info_facebook_deserialize(data)

  return None

async def media_backend_apishop_info(link: str):
  params = {"url": link}
  async with aiohttp.ClientSession("https://full.apishop.uz") as http_session:
    async with http_session.get("/get-media-info", params=params) as http_response:
      json_response = await http_response.json()
      return _media_info_deserialize(json_response)