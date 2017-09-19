import asyncio
import async_timeout
import aiohttp
from collections import Iterable
# import json
# import ujson
from os import path


class async_getter(object):
    """we don't want multiple instances of this (yet) until interaction between getters is tested.
    As such, all methods, vars, etc... will be class-vars AND NOT instance-vars.
    AKA, instances MUST share all variables and functions."""

    start_url = ''
    base_url = None

    allowed_num_concurrencies = 5
    urls_count = 0

    headers = {}
    error_urls = []
    urls_traversed = [] #<--as this grows larger the spider's performance will slow...
    # ...IF we are checking for traversal-loops.





    async def fetch(url, session):
        with async_timeout.timeout(10):
            async with session.get(url) as response:
                return await response.json()

    async def queue_iterable(foo_iterable, q):
        assert isinstance(foo_iterable, Iterable)



    async def dispatch(urls, loop=None):
        if not loop:
            _loop = asyncio.get_event_loop()
        else:
            _loop = loop
        async with aiohttp.ClientSession() as session:
            pass




if __name__ == "__main__":
    pass