import asyncio
import json

def _track_recognize_deserialize(track):
  return {
    "id": track["key"],
    "title": track["title"],
    "performer": track["subtitle"],
    "duration": 0,
    "thumbnail_url": track["images"].get("coverart", track["images"].get("coverarthq", None)) if "images" in track else None
  }

async def track_backend_songrec_recognize(file_path: str):
  songrec_proc = await asyncio.create_subprocess_shell(
    f"proxychains4 -f proxychains4.conf -q songrec recognize {file_path} --json",
    stdout=asyncio.subprocess.PIPE,
    stderr=asyncio.subprocess.PIPE,
    shell=True,
  )

  songrec_proc_stdout, songrec_proc_stderr = await songrec_proc.communicate()
  if songrec_proc_stderr:
    return None

  recognize_result = json.loads(songrec_proc_stdout)["track"]
  return _track_recognize_deserialize(recognize_result)
