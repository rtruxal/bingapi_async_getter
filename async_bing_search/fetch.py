import aiohttp
async def fetch(url, headers, session, semaphore):
    error_code = 000 # <-- means it didn't go through.
    with (await semaphore): # <--...UH...K?
        # Can't think of when this if/else bloc would be necessary,
        # but the herd compells me:
        if callable(headers):
            _headers = headers()
        else:
            _headers = headers
        try:
            async with session.get(url, headers=_headers) as response:
                if response.status in (200, 201):
                    data = await response.text()
                    return data
                else:
                    error_code = response.status
                    raise aiohttp.ClientResponseError('')
        except aiohttp.ClientResponseError as err:
            print('[FETCH-ERROR] url: {} -- code: {}\t msg: {}'.format(url, error_code, (err.msg if err.msg else "NO DATA FROM SERVER")))
            return None