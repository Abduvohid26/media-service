import asyncio
from youtube_search import YoutubeSearch

def get_duration(duration: str):
  return int(duration.split(":")[0]) * 60 + int(duration.split(":")[1]) if duration else 0

def _track_search_deserialize(track):
  return {
    "id": track["id"],
    "title": track["title"],
    "performer": track["channel"],
    "duration": get_duration(track["duration"]),
    "thumbnail_url": track["thumbnails"][0]
  }

async def track_youtube_search_search(query: str, offset: int, limit: int):
  search_results = YoutubeSearch(query + " music", max_results=offset+limit).to_json()

  search_results = await asyncio.get_event_loop().run_in_executor(None, lambda: YoutubeSearch(query, max_results=offset+limit).to_dict())
  deserialized_search_results = [_track_search_deserialize(search_result) for search_result in search_results]
  return deserialized_search_results[offset:offset+limit]