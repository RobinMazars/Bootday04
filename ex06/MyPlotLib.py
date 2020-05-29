from FileLoader import FileLoader
import matplotlib.pyplot as plt
import pandas as pd


class MyPlotLib(object):
    """docstring for MyPlotLib."""

    def __init__(self):
        pass

    def histogram(self, data, feature):
        data = data.drop_duplicates("Name")
        fig, axes = plt.subplots(ncols=2)
        for i, x in enumerate(axes):
            x.hist(data[feature[i]], bins=10)
            x.grid()
            x.set_title(f"Histogramme of {feature[i]}")
        fig.tight_layout()
        plt.show()

    # def density(self, data, feature):
    #     data = data.drop_duplicates("Name").dropna()
    #     for x in feature:
    #         density = gaussian_kde(data[x])
    #         xs = np.linspace(0, max(data[x]), 200)
    #         density.covariance_factor = lambda: .08
    #         density._compute_covariance()
    #         plt.plot(xs, density(xs))
    #     plt.show()
    def density(self, data, feature):
        data = data.drop_duplicates("Name").dropna()
        pd.DataFrame(data, columns=feature).plot(kind='density')
        plt.show()

    def pair_plot(self, data, feature):

        data = data.drop_duplicates("Name").dropna()
        pd.DataFrame(data, columns=feature).plot(
            kind='scatter', x=feature[0], y=feature[1])
        plt.show()

    def box_plot(self, data, feature):
        data = data.drop_duplicates("Name").dropna()
        pd.DataFrame(data, columns=feature).plot(
            kind='box')
        plt.show()


loader = FileLoader()
data = loader.load('../athlete_events.csv')
mpl = MyPlotLib()
# mpl.histogram(data, ["Height", "Weight"])
# mpl.density(data, ["Height", "Weight"])
# mpl.pair_plot(data, ["Height", "Weight"])
mpl.box_plot(data, ["Height", "Weight"])

# pprint(re)
