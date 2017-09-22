from async_bing_search.SearchManifest import AsyncSearchManifest, ParamContainer
from async_bing_search.DEFAULT_SEARCH_PARAMS import DefaultHeaders, DefaultUrlParams
import asyncio
import aiohttp


async def populate_manifest_by_expanding_offset(query, params, headers, *, loop=None):
    _param_container = ParamContainer(query, params, headers)
    async with aiohttp.ClientSession() as sess:
        pass


if __name__ == "__main__":
    key = '6bf8fc9ce32d4e98850d688428c8f75f'
    query = '"Forsythe IT" OR "Forsythe Technology"'
    # paramz = DefaultUrlParams()
    headz = DefaultHeaders()
    headz.update({'Ocp-Apim-Subscription-Key': key})
    # loop = asyncio.get_event_loop()
    print(headz)
