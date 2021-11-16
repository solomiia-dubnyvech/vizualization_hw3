import altair as alt


def build_map(world, data, lookup_field, scale, field_type='Q'):
    return alt.Chart(world).transform_lookup(
        lookup='name',
        from_=alt.LookupData(data=data, key='country', fields=['country', lookup_field]),
    ).project('equalEarth').mark_geoshape().encode(
        color=alt.Color(f'{lookup_field}:{field_type}', scale=scale),
        tooltip=[alt.Tooltip('name:N'), alt.Tooltip(f'{lookup_field}:{field_type}')],
    )
