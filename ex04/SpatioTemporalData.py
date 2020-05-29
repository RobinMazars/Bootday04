from FileLoader import FileLoader


class SpatioTemporalData(object):
    """docstring for SpatioTemporalData."""

    def __init__(self, data):
        self.data = data

    def when(self, location):
        d = self.data.query(f'City == "{location}"')["Year"]
        return list(d.drop_duplicates())

    def where(self, date):
        d = self.data.query(f'Year == "{date}"')["City"]
        return list(d.drop_duplicates())


loader = FileLoader()
data = loader.load('../athlete_events.csv')
sp = SpatioTemporalData(data)
print(sp.where(2016))
print(sp.when("Paris"))
