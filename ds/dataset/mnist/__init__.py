from .. import Dataset

class MNIST(Dataset):
    def data(self):
        return {
            'mnist.npz': {
                description: 'splitted NumPy array',
                url: 'https://s3.amazonaws.com/img-datasets/mnist.npz'
            }
        }

    def load(self):
        import numpy
        f = numpy.load(self.get_file('mnist.npz'))
        x_train, y_train = f['x_train'], f['y_train']
        x_test, y_test = f['x_test'], f['y_test']
        return (x_train, y_train, x_test, y_test)
