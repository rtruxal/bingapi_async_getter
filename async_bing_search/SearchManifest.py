from collections import deque
from asyncio import Queue

class AsyncSearchManifest(Queue):
    """This class is prly unnecessary...keeping names consistent."""
    def __init__(self, maxsize=0, *, loop=None):
        super(AsyncSearchManifest, self).__init__(maxsize, loop=loop)


class SearchManifest(deque):
    """
      ===========
      *IMPORTANT*
      ===========
    - INSERT LEFT
    - REMOVE RIGHT

    """
    def __init__(self, *args, **kwargs):
        super(SearchManifest, self).__init__(*args, **kwargs)

    def append(self, *args, **kwargs):
        """enforce rules on insertion/removal"""
        print('WARN: append() detected. Changed to appendleft(). See SearchManifest docstring.')
        self.appendleft(*args, **kwargs)

    def popleft(self, *args, **kwargs):
        """enforce rules on insertion/removal"""
        print('WARN: popleft() detected. Changed to pop(). See SearchManifest docstring.')
        return self.pop(*args, **kwargs)


class ParamContainer(object):
    """This class is a simple object to provide a unified interface for the SearchManifest queue
    to handle queries, url-params, & headers."""
    def __init__(self, unencoded_query_string, url_param_dict, header_param_dict):

        self.__iscompleted = False

        super(ParamContainer, self).__init__()

        self.query = unencoded_query_string
        self.url_param_dict = url_param_dict
        self.header_param_dict = header_param_dict

    def mark_as_completed(self):
        self.__iscompleted = True

    def iscompleted(self):
        return self.__iscompleted
