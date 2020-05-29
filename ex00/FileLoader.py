import pandas as pd


class FileLoader(object):
    """docstring for FileLoader."""

    def __init__(self):
        pass

    def load(self, path):
        data = pd.read_csv(path)
        print(data.shape)
        return data

    def display(self, data, n):
        if n >= 0:
            print(data[:n])
        else:
            print(data)


path = "./good.csv"
fl = FileLoader()
data = fl.load(path)
fl.display(data, 1)
