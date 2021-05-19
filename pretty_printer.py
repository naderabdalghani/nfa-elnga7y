from termcolor import cprint
from colorama import init as colorama_init
colorama_init(autoreset=True)


class PrettyPrinter:
    INFO = 0
    WARNING = 1
    ERROR = 2
    SUCCESS = 3
    PRINTING_TAGS = {
        INFO: '[INFO]',
        WARNING: '[WARNING]',
        ERROR: '[ERROR]',
        SUCCESS: '[SUCCESS]'
    }
    PRINTING_TAGS_COLORS = {
        '[INFO]': ['white', 'on_blue'],
        '[ERROR]': ['white', 'on_red'],
        '[SUCCESS]': ['white', 'on_green'],
        '[WARNING]': ['white', 'on_yellow']
    }

    def __call__(self, text, level=None, *args, **kwargs):
        level = self.INFO if level is None else level
        tag = self.PRINTING_TAGS.get(level, 'INFO')
        cprint(tag, self.PRINTING_TAGS_COLORS[tag][0], self.PRINTING_TAGS_COLORS[tag][1], end=' ')
        print(text, *args, **kwargs)
