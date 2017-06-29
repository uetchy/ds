import itertools
from .. import Dataset


class VoiceStatistics(Dataset):
    def __init__(self):
        self.endpoint = 'https://github.com/voice-statistics/voice-statistics.github.com/raw/master/assets/data'
        self.actors = [
            {'name': '土谷麻貴', 'slug': 'tsuchiya'},
            {'name': '上村彩子', 'slug': 'uemura'},
            {'name': '藤東知夏', 'slug': 'fujitou'}
        ]
        self.variants = ['normal', 'happy', 'angry']

    def data(self):
        return {
            "{}_{}.tar.gz".format(actor['slug'], variant): {
                'description': actor['name']+'_'+variant,
                'url': "{}/{}_{}.tar.gz".format(self.endpoint, actor['slug'], variant)
            } for actor, variant in itertools.product(self.actors, self.variants)
        }

    def preprocess():
        pass

    def load(self, actor_slug):
        return [self.get_file("{}_{}.tar.gz".format(actor_slug, variant)) for variant in self.variants]