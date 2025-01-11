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

def get_date_features(df, date):
    df_date = df
    try:
        df_date['month'] = df_date[date].dt.month
        df_date['year'] = df_date[date].dt.year

        df_date['day_of_week'] = df_date[date].dt.dayofweek
        df_date['day_of_month'] = df_date[date].dt.day
        df_date['day_of_year'] = df_date[date].dt.dayofyear

        df_date['week_of_year'] = df_date[date].dt.isocalendar().week
        df_date['week_of_year'] = df_date['week_of_year'].astype(int)

        df_date['quarter'] = df_date[date].dt.quarter
        return df_date
    except:
        return df

casher_dim = casher.drop(columns=['branch_id'])
branch_dim = branch.merge(city, on='city_id', how='inner').drop(columns=['state_id_y']).rename(columns={'state_id_x': 'state_id'})
branch_dim = branch_dim.merge(state, on='state_id', how='inner').drop(columns=['state_id', 'city_id'])
category_dim = category.merge(sub_category, on='category_id', how='inner')
customer_dim = customer
product_dim = product.drop(columns=['sub_category_id'])
promotion_dim = promotion.drop(columns=['start_date', 'end_date'])
promotion_product_factless = promotion_product.copy()
date_dim = transaction[['date']].drop_duplicates()
date_dim['date'] = pd.to_datetime(date_dim['date'])
date_dim.set_index('date', inplace=True)
date_dim = date_dim.resample('D').sum(numeric_only=True).sort_values(by='date').reset_index()
date_dim = get_date_features(date_dim, 'date')
print(date_dim)
