from FileLoader import FileLoader
from pprint import pprint


def howManyMedals(data, name):
    full = data.query(f' Name == "{name}"')[["Year", "Medal"]]
    # print(full)
    d2 = full.groupby("Year").Medal
    # print(d2)
    # d3 = pd.concat([d2.apply(list), d2.count()],
    #                axis=1, keys=['Year', 'count2'])
    d3 = dict(d2.apply(list))
    d4 = {}
    for x in d3:
        d4[x] = {'G': d3[x].count("Gold"), 'S': d3[x].count(
            "Silver"), 'B': d3[x].count("Bronze")}
    # print(d2)
    # d4 = (map({'G': d2.count(), 'S': d2.count(
    #     ), 'B': d2.count()}, d3))
    return d4


loader = FileLoader()
data = loader.load('../athlete_events.csv')
re = howManyMedals(data, 'Kjetil Andr Aamodt')
pprint(re)
