class InputSanitizer(object):
    def __init__(self):
        super(InputSanitizer, self).__init__()

    @staticmethod
    def is_dictish(obj):
        assert isinstance(obj, dict) or issubclass(obj, dict), "VARIABLE {} IS NOT A DICT NOR DOES IT SUBCLASS DICT.".format(obj.__name__)

    @staticmethod
    def is_iterable(obj):
        assert obj.__iter__ or obj.__aiter__

    @staticmethod
    def is_allowed_param(obj, ITERABLE_OF_POSSIBLE_VALS):
        assert obj in ITERABLE_OF_POSSIBLE_VALS
