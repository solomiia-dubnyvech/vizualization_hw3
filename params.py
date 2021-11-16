def add_title(chart, title):
    return chart.properties(
        title=title,
    ).configure_title(
        fontSize=24,
        font='Courier',
        anchor='start',
        dy=-30
    )


def decorate_map(chart):
    return chart.properties(width=950, height=500, background='#F9F9F9', padding=25)


def get_geo_shape_params():
    return dict(stroke='white')
