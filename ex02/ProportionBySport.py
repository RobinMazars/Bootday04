from FileLoader import FileLoader


def proportionBySport(data, year, sport, gender):
    dataset = data.query(
        f'Year == {year} & Sex == "{gender}"').drop_duplicates("Name")  # ID
    len_total = len(dataset)
    nbr_sport = len(dataset.query(f'Sport == "{sport}"'))
    result = nbr_sport / len_total
    return (result)


loader = FileLoader()
data = loader.load('../athlete_events.csv')
re = proportionBySport(data, 2004, 'Tennis', 'F')
print(re)
