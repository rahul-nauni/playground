import pandas as pd
import tabulate as tab

views = pd.DataFrame([], columns=[
    'article_id', 
    'author_id', 
    'viewer_id', 
    'view_date']
    ).astype({
        'article_id':'Int64', 
        'author_id':'Int64', 
        'viewer_id':'Int64', 
        'view_date':'datetime64[ns]'
        })

views_data = pd.DataFrame([
    {'article_id':1, 'author_id':3, 'viewer_id':5, 'view_date':'2019-08-01'},
    {'article_id':1, 'author_id':3, 'viewer_id':6, 'view_date':'2019-08-02'},
    {'article_id':2, 'author_id':7, 'viewer_id':7, 'view_date':'2019-08-01'},
    {'article_id':2, 'author_id':7, 'viewer_id':6, 'view_date':'2019-08-02'},
    {'article_id':4, 'author_id':7, 'viewer_id':1, 'view_date':'2019-07-22'},
    {'article_id':3, 'author_id':4, 'viewer_id':4, 'view_date':'2019-07-21'},
    {'article_id':3, 'author_id':4, 'viewer_id':4, 'view_date':'2019-07-21'},
])

views = pd.concat([views, views_data], ignore_index=True)
views.set_index('article_id', inplace=True)
print(tab.tabulate(views, headers='keys', tablefmt='psql'))

# Find the authors that viewed at least one of their own articles
# Self Inner join

authors_views = views.merge(views, how='inner', left_on=['article_id', 'author_id'], right_on=['article_id', 'viewer_id'], indicator='authors')

self_authors_views = authors_views.loc[authors_views['authors'] == 'both', ['author_id_x']]
self_authors_views.rename(columns={'author_id_x': 'id'}, inplace=True)
self_authors_views.drop_duplicates(subset='id', inplace=True)
self_authors_views.sort_values(by='id', inplace=True)
self_authors_views.reset_index(drop=True, inplace=True)

print(tab.tabulate(self_authors_views, headers='keys', tablefmt='psql'))
