import pandas as pd 
from tab_c import db
#['transaction', 'customer', 'promotion', 'promotion_product', 'product', 'sub_category', 'category', 'state', 'branch', 'city', 'casher']

transaction = db['transaction']
customer = db['customer']
promotion = db['promotion'] 
promotion_product = db['promotion_product']
product = db['product']
sub_category = db['sub_category']
category = db['category']
state = db['state']
branch = db['branch']
city = db['city']
casher = db['casher']

casher_dim = casher.drop(columns=['branch_id'])
branch_dim = branch.merge(city, on='city_id', how='inner').drop(columns=['state_id_y']).rename(columns={'state_id_x': 'state_id'})
branch_dim = branch_dim.merge(state, on='state_id', how='inner').drop(columns=['state_id', 'city_id'])
category_dim = category.merge(sub_category, on='category_id', how='inner')
customer_dim = customer
product_dim = product.drop(columns=['sub_category_id'])








    




