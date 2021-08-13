import pandas as pd
print('beginning clean process')

# initialization
# products_raw = pd.read_csv('~/Downloads/product.csv')
styles_raw = pd.read_csv('~/Downloads/styles.csv')
col_names = ['id', 'styleId', 'url', 'thumbnail_url']
photos_raw = pd.read_csv('~/Downloads/photos.csv', names=col_names)
photos_raw = photos_raw.iloc[1:]
photos_raw.astype({'styleId': int})
print(photos_raw.head())
# features_raw = pd.read_csv('~/Downloads/features.csv')
# related_raw = pd.read_csv('~/Downloads/related.csv')

# manipulation
# (1) adds a 'related' column to our products DF with an array of other product ids
# related_filtered = related_raw.filter(items=['current_product_id', 'related_product_id']).rename(columns={'current_product_id': 'id'})
# products_related = products_raw.merge(related_filtered.groupby('id')['related_product_id'].apply(lambda x: list(set(x))).reset_index())
# products_related.rename(columns={'related_product_id': 'related'}, inplace=True)

# (2) adds a 'features' column to our products DF with an array of feature: string, value:string dicts
# features_filtered = features_raw.filter(items=['product_id', 'feature', 'value']).rename(columns={'product_id': 'id'})

# zip feature/val columns together as a fourth column 'kvp' 
# kvp = list(zip(features_filtered['feature'], features_filtered['value']))
# kvp = [{'feature': p[0], 'value' : p[1]} for p in kvp]
# features_filtered['kvp'] = kvp

# merge features into products DF and rename to 'features' field
# products_final = products_related.merge(features_filtered.groupby('id')['kvp'].apply(list).reset_index())
# products_final.rename(columns={'kvp': 'features'}, inplace=True)
# products_final.drop_duplicates(subset=['id'], inplace=True)

styles_raw.rename(columns={'default_style' : 'default'}, inplace=True)
photos_filtered = photos_raw.filter(items=['styleId', 'url', 'thumbnail_url'])
urls = list(zip(photos_filtered['url'], photos_filtered['thumbnail_url']))
urls = [{'url': p[0], 'thumbnail_url' : p[1]} for p in urls]
photos_filtered['photos'] = urls
grouped_photos = photos_filtered.groupby('styleId')['photos']
for key, item in grouped_photos:
    print(grouped_photos.get_group(key))
# styles_photos = styles_raw.merge(photos_filtered, how='left', on='id' )
# styles_photos = styles_raw.merge(photos_filtered.groupby('id')['photos'].apply(list).reset_index())
# print(styles_photos.head(50))
