import json
import random
import typing
from .redis import redis

PROXYLIST = json.loads(open("/proxylist.json").read())

async def proxylist_get_unblocked() -> typing.Union[str, None]:
  blocklist = json.loads(await redis.get("proxy-blocklist") or "[]")
  unblocked_proxylist = [proxy for proxy in PROXYLIST if proxy not in blocklist]
  return random.choice(unblocked_proxylist or [None])

async def proxylist_blocked_add(proxy: str):
  blocklist = json.loads(await redis.get("proxy-blocklist") or "[]")
  blocklist.append(proxy)
  await redis.set("proxy-blocklist", json.dumps(blocklist))