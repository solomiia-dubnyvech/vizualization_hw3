import pandas as pd
import geopandas as gpd


def load_map():
    return gpd.read_file('world-countries.json')


def load_data():
    fields = ['variant', 'country', 'year', 'population']
    df = pd.read_csv('population_prospects.csv').loc[:, fields]
    df = df[(df['variant'] == 'Estimates') | (df['variant'] == 'Medium variant')]
    df['population'] = df['population'].apply(lambda population: int(population * 1000))
    df['country'] = df['country'].apply(_correct_country)
    return df


def _correct_country(name):
    if name == 'Russian Federation':
        # It was better without russia on map
        return 'Russia'
    elif name == 'Bolivia (Plurinational State of)':
        return 'Bolivia'
    elif name == 'Venezuela (Bolivarian Republic of)':
        return 'Venezuela'
    elif name == 'Congo':
        return 'Republic of the Congo'
    elif name == 'Iran (Islamic Republic of)':
        return 'Iran'
    elif name == 'Guinea-Bissau':
        return 'Guinea Bissau'
    elif name == 'Cote d\'Ivoire':
        return 'Ivory Coast'
    elif name == 'Republic of Korea':
        return 'North Korea'
    elif name == 'Dem. People\'s Republic of Korea':
        return 'South Korea'
    elif name == 'Czechia':
        return 'Czech Republic'
    elif name == 'Republic of Moldova':
        return 'Moldova'
    elif name == 'Viet Nam':
        return 'Vietnam'
    elif name == 'Lao People\'s Democratic Republic':
        return 'Laos'
    elif name == 'Serbia':
        return 'Republic of Serbia'
    elif name == 'North Macedonia':
        return 'Macedonia'
    elif name == 'Eswatini':
        return 'Swaziland'
    elif name == 'Syrian Arab Republic':
        return 'Syria'
    elif name == 'China, Taiwan Province of China':
        return 'Taiwan'
    elif name == 'Brunei Darussalam':
        return 'Brunei'
    elif name == 'Timor-Leste':
        return 'East Timor'
    elif name == 'Bahamas':
        return 'The Bahamas'
    else:
        return name


def get_population_for_2000(df):
    return df[df['year'] == 2000]


def get_population_for_2100(df):
    return df[df['year'] == 2100]


def get_population_binary_comparison(df1, df2):
    merged = pd.merge(df1, df2, on='country', how='inner')
    merged['population_grew'] = merged['population_x'] < merged['population_y']
    return merged


def get_population_comparison(df1, df2):
    merged = pd.merge(df1, df2, on='country', how='inner')
    merged['population_change'] = (merged['population_y'] - merged['population_x']) * 100 / merged['population_x']
    return merged


# testing source functions
if __name__ == '__main__':
    data = load_data()
    print(get_population_comparison(get_population_for_2000(data),
                                    get_population_for_2100(data)))
