import pandas as pd

world = pd.DataFrame([], columns=['name', 'continent', 'area', 'population', 'gdp']).astype({
    'name':'object', 
    'continent':'object', 
    'area':'Int64', 
    'population':'Int64', 
    'gdp':'Int64'})

data = [
    {
        'name': 'Afghanistan',
        'continent': 'Asia', 
        'area': 652230, 
        'population': 25500100, 
        'gdp': 20343000000
    },
    {
        'name': 'Albania',
        'continent': 'Europe',
        'area': 28748,
        'population': 2831741,
        'gdp': 12960000000
    },
    {
        'name': 'Algeria',
        'continent': 'Africa',
        'area': 2381741,
        'population': 37100000,
        'gdp': 188681000000
    },
    {
        'name': 'Andorra',
        'continent': 'Europe',
        'area': 468,
        'population': 78115,
        'gdp': 3712000000
    },
    {
        'name': 'Angola',
        'continent': 'Africa',
        'area': 1246700,
        'population': 20609294,
        'gdp': 100990000000
    }
]

world = pd.concat([world, pd.DataFrame(data)], ignore_index=True)
world.set_index('name', inplace=True)
#print(f"world dataframe: {world}")


# dictionary for parameters to be classed as a big country
big_country = {
    'area': 3000000,
    'population': 25000000,
}

condition = (world['area'] > big_country['area']) | (world['population'] > big_country['population'])
print(world.loc[condition, ['population', 'area']])


