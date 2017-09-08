from collections import OrderedDict
from socket import gethostbyname, gethostname
import asyncio

###############################################
##                                           ##
##       User-defined dictionaries for       ##
##          header and query params          ##
##                                           ##
###############################################
class DefaultHeaders(OrderedDict):
    def __init__(self):
        super(DefaultHeaders, self).__init__()
        ###############################################
        # do NOT modify this:
        self['Ocp-Apim-Subscription-Key'] = None # <== NO TOUCHY-TOUCHY. IT'S HERE TO PRESERVE ORDER.
        # SERIOUSLY. DON'T CHANGE IT.
        # LORD KNOWS HOW MANY ERRORS THAT WOULD CAUSE.

        ###############################################
        ## Enter default-header customizations here. ##
        ###############################################
        self['User-Agent'] = "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1" # <--(dummy User-Agent header for consistent response-format)
        self['X-Search-ClientIP'] = gethostbyname(gethostname())                                                 # <--(these are methods from the 'socket' module which produce the host-machine's public IP)
        self['X-MSEdge-ClientID'] = None
        self['Accept'] = None
        self['Accept-Language'] = None
        self['X-Search-Location'] = None
        self._clean()

    def _clean(self):
        """same as below but not for runtime-execution."""
        for k, v in self.items():
            if k in ('count', 'offset'):
                pass
            if not v: del self[k]

    async def _clean_coro(self):
        """this just cycles through the dict and removes entries that are empty.
         I gave it a breakpoint using `await asyncio.sleep(0)`.
         This SHOULD NOT change its behavior, but it should allow me to run it as a coroutine."""
        async for k, v in self.items():
            await asyncio.sleep(0)
            if k in ('count', 'offset'):
                pass
            if not v: del self[k]

class DefaultUrlParams(OrderedDict):
    def __init__(self):
        super(OrderedDict, self).__init__()
        ##############################################
        ##     Enter query customizations here.      ##
        ###############################################
        self['cc'] = None               # <--(See constants._COUNTRY_CODES below for available options)
        self['count'] = "50"            # <--(Enter a number from 0-50. Must by type==str. EX: count of 5 should be "5")
        self['freshness'] = None        # <--(Poss values are 'Day', 'Week', or 'Month')
        self['mkt'] = 'en-us'           # <--(See constants._MARKET_CODES below for available options)
        self['offset'] = '0'            # <--(Use this in conjunction with totalEstimatedMatches and count to page. Same format as 'count')
        self['responseFilter'] = None   # <--(Poss values are 'Computation', 'Images', 'News', 'RelatedSearches', SpellSuggestions', 'TimeZone', 'Videos', or 'Webpages')
        self['safeSearch'] = None       # <--(Poss values are 'Off', 'Moderate', and 'Strict.')
        self['setLang'] = None          # <--(See ISO 639-1, 2-letter language codes here: https://www.loc.gov/standards/iso639-2/php/code_list.php)
        self['textDecorations'] = None  # <--(Case-insensitive boolean. '(t|T)rue', or '(f|F)alse')
        self['textFormat'] = None       # <--(Poss values are 'Raw', and 'HTML.' Default is 'Raw' if left blank.)
        # News Search Only!
        self['category'] = None         # <--(ONLY FOR NEWS SEARCH. See available categories by mkt)
        self._clean()

    def _clean(self):
        """same as below but not for runtime-execution."""
        for k, v in self.items():
            if k in ('count', 'offset'):
                pass
            if not v: del self[k]


    async def _clean_coro(self):
        """this just cycles through the dict and removes entries that are empty.
         I gave it a breakpoint using `await asyncio.sleep(0)`.
         This SHOULD NOT change its behavior, but it should allow me to run it as a coroutine."""
        async for k, v in self.items():
            await asyncio.sleep(0)
            if k in ('count', 'offset'):
                pass
            if not v: del self[k]

