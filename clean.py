import pandas as pd
print('beginning clean process')

# initialization
products_raw = pd.read_csv('~/Downloads/product.csv')
# styles_raw = pd.read_csv('~/Downloads/styles.csv')
# col_names = ['id', 'styleId', 'url', 'thumbnail_url']
# photos_raw = pd.read_csv('~/Downloads/photos.csv', names=col_names)
features_raw = pd.read_csv('~/Downloads/features.csv')
related_raw = pd.read_csv('~/Downloads/related.csv')

# manipulation
# (1) adds a 'related' column to our products DF with an array of other product ids
related_filtered = related_raw.filter(items=['current_product_id', 'related_product_id']).rename(columns={'current_product_id': 'id'})
products_related = products_raw.merge(related_filtered.groupby('id')['related_product_id'].apply(list).reset_index()).rename(columns={'related_product_id': 'related'})

# (2) adds a 'features' column to our products DF with an array of feature: string, value:string dicts
features_filtered = features_raw.filter(items=['product_id', 'feature', 'value']).rename(columns={'product_id': 'id'})

# replace NaN with empty string, zip feature/val columns together as a fourth column 'kvp' 
# features_filtered.fillna('', inplace=True)
kvp = list(zip(features_filtered['feature'], features_filtered['value']))
kvp = [{p[0] : p[1]} for p in kvp]
kvpd = pd.DataFrame(kvp)
print(kvpd.head())


