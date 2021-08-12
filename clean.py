import pandas as pd
print('beginning clean process')

# initialization
products_raw = pd.read_csv('~/Downloads/product.csv')
styles_raw = pd.read_csv('~/Downloads/styles.csv')
col_names = ['id', 'styleId', 'url', 'thumbnail_url']
photos_raw = pd.read_csv('~/Downloads/photos.csv', names=col_names)
features_raw = pd.read_csv('~/Downloads/features.csv')
related_raw = pd.read_csv('~/Downloads/related.csv')

# manipulation
# products_raw['related'] = something 
related_filtered = related_raw.filter(items=['current_product_id', 'related_product_id'])
print(related_filtered.head())
