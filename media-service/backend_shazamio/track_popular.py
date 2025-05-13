from shazamio import Shazam

def _track_popular_deserialize(track):
  return {
    "id": track["id"],
    "title": track["attributes"]["name"],
    "performer": track["attributes"].get("composerName", ""),
    "duration": 0
  }

shazam = Shazam()

async def track_backend_shazamio_popular(country_code: str, limit: int):
  popular_tracks = await shazam.top_country_tracks(country_code, limit)
  return [_track_popular_deserialize(track) for track in popular_tracks["data"]]