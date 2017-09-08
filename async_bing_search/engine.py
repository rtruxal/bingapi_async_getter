import os
import sys
from os import path as p
import asyncio
import aiohttp
import async_timeout
from functools import partial
from .DEFAULT_SEARCH_PARAMS import DefaultHeaders, DefaultUrlParams
from .InputSanitizer import InputSanitizer



class AsyncRequester(object):
    def __init__(self, api_key, *, endpoint_type='web', alt_header_dict=None, alt_url_param_dict=None, loop=None):
        super(AsyncRequester, self).__init__()

        if not loop:
            self._loop = asyncio.get_event_loop()
        else:
            self._loop = loop
        if alt_header_dict is None:
            self._headers = DefaultHeaders()
        else:
            InputSanitizer.is_dictish(alt_header_dict)
            self._headers = alt_header_dict
        if alt_url_param_dict is None:
            self._params = DefaultUrlParams()
        else:
            InputSanitizer.is_dictish(alt_url_param_dict)
            self._params = alt_url_param_dict



async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as resp:
            return await resp.text()

async def init_session(urls=None):
    if not urls:
        _urls = ['https://httpbin.org/{}'.format(i) for i in ['ip', 'user-agent', 'headers', 'encoding/utf8']]
    else:
        _urls = urls

