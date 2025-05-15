import asyncio
import typing

MEDIA_SERVICE_FILES_PATH = "/media-service-files"

# async def youtube_backend_yt_dlp_download(id: str, proxy: typing.Union[str, None], source_address: typing.Union[str, None]) -> str:
#   command_to_execute = f"""yt-dlp -f 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' -S vcodec:h264 --windows-filenames --restrict-filenames --embed-thumbnail --add-metadata --no-playlist --remux-video "mp4/mkv" "{id}" --quiet --print "after_move:%(filepath)j" -P {MEDIA_SERVICE_FILES_PATH}"""

#   if proxy:
#     command_to_execute += f" --proxy {proxy}"

#   if source_address:
#     command_to_execute += f" --source_address {source_address}"

#   # create a subprocess shell and execute the command
#   download_process = await asyncio.create_subprocess_shell(
#     command_to_execute,
#     stdout=asyncio.subprocess.PIPE,
#     stderr=asyncio.subprocess.PIPE
#   )

#   # communicate with the subprocess
#   stdout, stderr = await download_process.communicate()
#   if stderr:
#     raise Exception(stderr.decode("utf-8"))

#   # TODO: very very bad
#   return stdout.decode().replace("\"", "").replace("\n", "").replace("webm", "mp3")


async def youtube_backend_yt_dlp_download(id: str, proxy: typing.Union[str, None], source_address: typing.Union[str, None]) -> str:
    command_to_execute = f"""yt-dlp -f 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' -S vcodec:h264 --windows-filenames --restrict-filenames --embed-thumbnail --add-metadata --no-playlist --remux-video "mp4/mkv" "{id}" --quiet --print "after_move:%(filepath)j" -P {MEDIA_SERVICE_FILES_PATH}"""

    if proxy:
        command_to_execute += f" --proxy {proxy}"

    if source_address:
        command_to_execute += f" --source_address {source_address}"

    print("🧾 Running yt-dlp command:\n", command_to_execute)

    download_process = await asyncio.create_subprocess_shell(
        command_to_execute,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await download_process.communicate()

    if stderr:
        stderr_decoded = stderr.decode("utf-8")
        print("❌ yt-dlp stderr:\n", stderr_decoded)
        raise Exception(stderr_decoded)

    stdout_decoded = stdout.decode().strip()
    print("✅ yt-dlp stdout (raw):", stdout_decoded)

    # Clean and format the result path
    cleaned_path = stdout_decoded.replace("\"", "").replace("webm", "mp3").strip()
    print("📁 Cleaned file path:", cleaned_path)

    return cleaned_path
