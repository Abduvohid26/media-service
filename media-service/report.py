import typing
import aiohttp

TELEGRAM_BOT_TOKEN = "7602460249:AAGEhEyp666GLXbG9EkEwHxgtRjQ7eu8dSc"

async def report(service: str, message: str, error: typing.Union[str, None] = None):
  params = {"chat_id": -1002225111619, "text": f"Service: {service}\nMessage: {message}\n\nError:\n{error}"}
  async with aiohttp.ClientSession() as http_session:
    async with http_session.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage", params=params) as http_response:
      pass
