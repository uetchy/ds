if __name__ == '__main__':
    from ds.dataset.mnist import MNIST
    mnist = MNIST()
    print(mnist())

    from ds.dataset.voice_statistics import VoiceStatistics
    vs = VoiceStatistics()
    print(vs())