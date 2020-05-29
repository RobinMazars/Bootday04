from FileLoader import FileLoader
from pprint import pprint


def howManyMedals(data, name):
    full = data.query(f' Name == "{name}"')[["Year", "Medal"]]
    d2 = full.groupby("Year").Medal
    d3 = dict(d2.apply(list))
    d4 = {}
    for x in d3:
        d4[x] = {'G': d3[x].count("Gold"), 'S': d3[x].count(
            "Silver"), 'B': d3[x].count("Bronze")}
    return d4


loader = FileLoader()
data = loader.load('../athlete_events.csv')
re = howManyMedals(data, 'Kjetil Andr Aamodt')
pprint(re)
