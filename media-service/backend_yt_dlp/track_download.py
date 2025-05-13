import asyncio
import typing

MEDIA_SERVICE_FILES_PATH = "/media-service-files"

async def track_backend_yt_dlp_download(track_id: str, proxy: typing.Union[str, None], source_address: typing.Union[str, None] = None) -> str:
    track_id = f"https://youtube.com/watch?v={track_id}"
    command_to_execute = f"""yt-dlp --embed-thumbnail --embed-metadata -f "bestaudio[ext=m4a]" --windows-filenames --restrict-filenames "{track_id}" --geo-bypass -P {MEDIA_SERVICE_FILES_PATH} --quiet --print "after_move:%(filepath)j" """

    if proxy:
      command_to_execute += f" --proxy {proxy}"

    if source_address:
      command_to_execute += f" --source_address {source_address}"

    # create a subprocess shell and execute the command
    download_process = await asyncio.create_subprocess_shell(
      command_to_execute,
      stdout=asyncio.subprocess.PIPE,
      stderr=asyncio.subprocess.PIPE
    )

    # communicate with the subprocess
    stdout, stderr = await download_process.communicate()
    if stderr:
      raise Exception(stderr.decode("utf-8"))

    # TODO: very very bad
    return stdout.decode().replace("\"", "").replace("\n", "").replace("webm", "mp3")