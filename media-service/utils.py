import aiohttp

async def download_file_in_memory(file_url: str):
  async with aiohttp.ClientSession() as http_session:
    async with http_session.get(file_url) as http_response:
      return await http_response.read()