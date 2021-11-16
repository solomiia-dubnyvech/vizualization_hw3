from source import *
from params import *
from chart_builder import *
import altair as alt


def task1():
    world_map = load_map()
    population_data = load_data()
    agg_data = get_population_binary_comparison(get_population_for_2000(population_data),
                                                get_population_for_2100(population_data))

    chart = build_map(world=world_map,
                      data=agg_data,
                      lookup_field='population_grew',
                      field_type='N',
                      scale=alt.Scale(scheme='category20'))

    return add_title(chart=decorate_map(chart),
                     title='Зміна населення країн світу в 2100 році у порівнянні з 2000 роком (більше/менше)')


def task2():
    world_map = load_map()
    population_data = load_data()
    agg_data = get_population_comparison(get_population_for_2000(population_data),
                                         get_population_for_2100(population_data))

    chart = build_map(world=world_map,
                      data=agg_data,
                      lookup_field='population_change',
                      scale=alt.Scale(scheme='redyellowgreen', domainMid=0))

    return add_title(chart=decorate_map(chart),
                     title='Зміна населення країн світу в 2100 році у порівнянні з 2000 роком (у %)')


def task3():
    world_map = load_map()
    population_data = load_data()
    agg_data = get_population_for_2100(population_data)

    chart = build_map(world=world_map,
                      data=agg_data,
                      lookup_field='population',
                      scale=alt.Scale(scheme='orangered'))

    return add_title(chart=decorate_map(chart),
                     title='Населення країн світу у 2100 році')


if __name__ == '__main__':
    alt.data_transformers.disable_max_rows()
    task3().show()
