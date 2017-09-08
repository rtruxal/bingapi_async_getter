
FRESHNESS_PARAMS = (
    'Day',
    'Week',
    'Year',
)
RESPONSE_FILTER_PARAMS = (
    'Computation',
    'Images',
    'News',
    'RelatedSearches',
    'SpellSuggestions',
    'TimeZone',
    'Videos',
    'Webpages',
)
SAFE_SEARCH_PARAMS = (
    'Off',
    'Moderate',
    'Strict',
)
## For use with 'cc'
COUNTRY_CODE_DICT = {
    'Australia': 'AR',
    'Austria': 'AU',
    'Belgium': 'AT',
    'Brazil': 'BE',
    'Canada': 'BR',
    'Chile': 'CA',
    'Denmark': 'CL',
    'Finland': 'DK',
    'France': 'FI',
    'Germany': 'FR',
    'Hong Kong SAR': 'DE',
    'India': 'HK',
    'Indonesia': 'IN',
    'Ireland': 'ID',
    'Italy': 'IE',
    'Japan': 'IT',
    'Korea': 'JP',
    'Malaysia': 'KR',
    'Mexico': 'MY',
    'NO': 'CN',
    'Netherlands': 'MX',
    'New Zealand': 'NL',
    'Norway': 'NZ',
    'Poland': 'PL',
    'Portugal': 'PT',
    'Republic of the Philippines': 'PH',
    'Russia': 'RU',
    'Saudi Arabia': 'SA',
    'South Africa': 'ZA',
    'Spain': 'ES',
    'Sweden': 'SE',
    'Switzerland': 'CH',
    'Taiwan': 'TW',
    'Turkey': 'TR',
    'United Kingdom': 'GB',
    'United States': 'US'
}
## For use with 'mkt'
MARKET_CODE_DICT = {
    'Argentina-Spanish': 'es-AR',
    'Australia-English': 'en-AU',
    'Austria-German': 'de-AT',
    'Belgium-Dutch': 'nl-BE',
    'Belgium-French': 'fr-BE',
    'Brazil-Portuguese': 'pt-BR',
    'Canada-English': 'en-CA',
    'Canada-French': 'fr-CA',
    'Chile-Spanish': 'es-CL',
    'Denmark-Danish': 'da-DK',
    'Finland-Finnish': 'fi-FI',
    'France-French': 'fr-FR',
    'Germany-German': 'de-DE',
    'Hong Kong SAR-Traditional Chinese': 'zh-HK',
    'India-English': 'en-IN',
    'Indonesia-English': 'en-ID',
    'Ireland-English': 'en-IE',
    'Italy-Italian': 'it-IT',
    'Japan-Japanese': 'ja-JP',
    'Korea-Korean': 'ko-KR',
    'Malaysia-English': 'en-MY',
    'Mexico-Spanish': 'es-MX',
    'Netherlands-Dutch': 'nl-NL',
    'New Zealand-English': 'en-NZ',
    'Norway-Norwegian': 'no-NO',
    "People's republic of China-Chinese": 'zh-CN',
    'Poland-Polish': 'pl-PL',
    'Portugal-Portuguese': 'pt-PT',
    'Republic of the Philippines-English': 'en-PH',
    'Russia-Russian': 'ru-RU',
    'Saudi Arabia-Arabic': 'ar-SA',
    'South Africa-English': 'en-ZA',
    'Spain-Spanish': 'es-ES',
    'Sweden-Swedish': 'sv-SE',
    'Switzerland-French': 'fr-CH',
    'Switzerland-German': 'de-CH',
    'Taiwan-Traditional Chinese': 'zh-TW',
    'Turkey-Turkish': 'tr-TR',
    'United Kingdom-English': 'en-GB',
    'United States-English': 'en-US',
    'United States-Spanish': 'es-US'
}
# COUNTRY_CODE_KEYS = tuple(i for i in COUNTRY_CODE_DICT.keys())
COUNTRY_CODES = tuple(i for i in COUNTRY_CODE_DICT.values())
MARKET_CODES = tuple(i for i in MARKET_CODE_DICT.values())
LANGUAGE_CODES = tuple(i[-2:] for i in list(MARKET_CODE_DICT.values()))
NEWS_CATEGORIES_US = (
    'Business',
    'Entertainment',
    'Entertainment_MovieAndTV',
    'Entertainment_Music',
    'Health',
    'Politics',
    'ScienceAndTechnology',
    'Science',
    'Technology',
    'Sports',
    'Sports_Golf',
    'Sports_MLB',
    'Sports_NBA',
    'Sports_NFL',
    'Sports_NHL',
    'Sports_Soccer',
    'Sports_Tennis',
    'Sports_CFB',
    'Sports_CBB',
    'US',
    'US_Northeast',
    'US_South',
    'US_Midwest',
    'US_West',
    'World',
    'World_Africa',
    'World_Americas',
    'World_Asia',
    'World_Europe',
    'World_MiddleEast',
)
NEWS_CATEGORIES_GB = (
    'Business',
    'Entertainment',
    'Health',
    'Politics',
    'ScienceAndTechnology',
    'Sports',
    'UK',
    'World',
)

def _ADVANCED_OPERATOR_3_TERM_DICT():
    # https://msdn.microsoft.com/en-us/library/ff795634.aspx
    ADVANCED_OPERATOR_3_TERM_DICT = {
        'near' : '{} near:{} {}',   # Ex: foo near:10 bar --> returns pages where bar is found within 10 words (before/after) foo.
    }
    return ADVANCED_OPERATOR_3_TERM_DICT

def _ADVANCED_OPERATOR_2_TERM_DICT():
    ADVANCED_OPERATOR_2_TERM_DICT = {
        'AND': '{} AND {}',
        '&&' : '{} && {}',
        'OR' : '{} OR {}',
        '|' : '{} | {}',
        '||' : '{} || {}',
        'NOT' : '{} NOT {}',                    # EVERYTHING to the right of NOT will be negated..
        'instreamset': 'instreamset:({}):{}',   # Ex: instreamset:(url title):foo --> This is a more generic version of intitle:, inbody:, and inanchor: - any of these meta tags can be specified within the parentheses.
        'literalmeta': 'literalmeta:{}({})',    # Ex: "literalmeta:foo(bar)" --> pages for which the metatag foo contains the word bar would be returned.
        'meta' : 'meta:{}({})',                 # Ex: meta:Search.os("Windows 7") See link above. Allows the filtering of content based on special tags in HTML.
    }
    return ADVANCED_OPERATOR_2_TERM_DICT

def _ADVANCED_OPERATOR_1_TERM_DICT():
    ADVANCED_OPERATOR_1_TERM_DICT = {
        '-' : '-"{}"',              # negation. Same as NOT, but interpreted literally due to inclusion of quotations by yours truely
        '+' : '+"{}"',              # necessitation. All retuned pages must contain the EXACT contents of the enclosed
        'altloc' : 'altloc:{}',     # used to specify a local search that is outside major markets
        'contains' : 'contains:{}', # takes a file-extension as arg. Ex: "foo contains:pdf"
        'domain' : 'domain:{}',     # same as site: but decends further into directory tree
        'ext' : 'ext:{}',           # filetype. Ex: ext:pdf
        'feed' : 'feed:{}',         # Finds RSS or Atom feeds pertaining to the term you specify.
        'filetype' : 'filetype:{}', # same as ext
        'hasfeed' : 'hasfeed:{}',   # same as feed, except for use in conjunction w/ other 1-term operators. See msdn link above.
        'inanchor' : 'inanchor:{}', # word order is preserved. Ex: inanchor: bird watching looks up bird 1st. For single-phrases that include spaces, use quotes.
        'inbody' : 'inbody:{}',     # what it sounds like
        'intitle' : 'intitle:{}',   # also what it sounds like
        'ip' : 'ip:{}',             # what websites has bing crawled that have used the IP in question?'
        'language' : 'language:{}', # mkt-codes are typically <country code>-<language code>. use those for ref
        'loc' : 'loc:{}',           # same as above, but use the country-code.
        'location' : 'location:{}', # same as loc
        'site' : 'site:{}',         # similar to domain but less-specific and better for combinatorial queries.
        'url' : 'url:{}',           # checks to see whether a particular URL has been indexed by Bing.
    }
    return ADVANCED_OPERATOR_1_TERM_DICT

def _ADVANCED_OPERATOR_ALT_TERM_DICT():
    ADVANCED_OPERATOR_ALT_TERM_DICT = {
        'images' : {'imagesize': 'imagesize:{}', 'msite' : 'msite:{}',},
        'videos' : {'msite' : 'msite:{}',},
    }
    return ADVANCED_OPERATOR_ALT_TERM_DICT

AO3 = _ADVANCED_OPERATOR_3_TERM_DICT()
AO2 = _ADVANCED_OPERATOR_2_TERM_DICT()
AO1 = _ADVANCED_OPERATOR_1_TERM_DICT()
AOA = _ADVANCED_OPERATOR_ALT_TERM_DICT()


QUERY_PARAM_DICT = {
    'q' : 'ARBITRARY -- str()',
    'category' : (NEWS_CATEGORIES_US, NEWS_CATEGORIES_GB), # <--news only
    'cc' : COUNTRY_CODES,
    'count' : 'ARBITRARY -- str(int)',
    'freshness' : ('Day', 'Week', 'Year'),
    'mkt' : MARKET_CODES,
    'offset' : 'ARBITRARY -- str(int)',
    'responseFilter' : RESPONSE_FILTER_PARAMS,
    'safeSearch' : SAFE_SEARCH_PARAMS,
    'setLang' : LANGUAGE_CODES,
    'textDecorations' : ('true', 'false'),  # <-- bool
    'textFormat' : ('Raw', "HTML"),
}
HEADER_PARAM_DICT = {
    'User-Agent' : 'VALID USER-AGENT STRING',
    'X-Search-ClientIP' : 'VALID SOURCE-IP ADDR',
    'X-MSEdge-ClientID' : 'COMES FROM JSON RESPONSE. UNIQUE IDENTIFIER TO CUSTOMIZE RESPONSES',
    'Accept' : ('application/json', 'application/ld+json'),
    'Accept-Language' : LANGUAGE_CODES,
    'X-Search-Location' : 'Semicolon-delimited list of k/v pairs described at https://msdn.microsoft.com/en-us/library/dn760794.aspx#Headers',
}