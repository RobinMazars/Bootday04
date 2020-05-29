from FileLoader import FileLoader


def youngestFellah(data, year):
    AgeF = data.query(f'Year == {year} & Sex == "F"').Age.min()
    AgeM = data.query(f'Year == {year} & Sex == "M"').Age.min()
    di = {"f": AgeF, "m": AgeM}
    return di
    # dataM = data.query(f'(Age == {minAge}) & (Sex == M)')
    # print(dataM)


loader = FileLoader()
data = loader.load('../athlete_events.csv')
# loader.display(data["Year"], 10)
re = youngestFellah(data, "2001")
print(re)
