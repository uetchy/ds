import os
from os import path
import re
import urllib.request

class Dataset(object):
    def __init__(self):
        pass

    def __call__(self):
        return self.load()

    def _get_cache_dir(self):
        return path.join(path.expanduser('~'), '.datasets', self._get_name(), 'cache')

    def _get_name(self):
        # https://stackoverflow.com/a/1176023
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', self.__class__.__name__)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def data(self):
        pass

    def get_file(self, filename):
        filepath = path.join(self._get_cache_dir(), filename)
        if path.exists(filepath):
            print('exist:', filepath)
            return open(filepath, 'rb')

        origin_url = self.data()[filename]['url']
        print('download:', origin_url, filepath)
        try:
            os.makedirs(path.dirname(filepath))
        except OSError as exception:
            pass

        with urllib.request.urlopen(origin_url) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())

        return self.get_file(filename)

    def load(self):
        pass