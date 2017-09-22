# import os
# import sys
# from os import path as p
import asyncio
import aiohttp
# import aiofiles
# import async_timeout
# from functools import partial
from .DEFAULT_SEARCH_PARAMS import DefaultHeaders, DefaultUrlParams
from .InputSanitizer import InputSanitizer






def init_session(urls=None):
    if not urls:
        _urls = ['https://httpbin.org/{}'.format(i) for i in ['ip', 'user-agent', 'headers', 'encoding/utf8']]
    else:
        _urls = urls

if __name__ == "__main__":
    pass
