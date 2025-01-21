import pandas as pd 
from el import *

for tbl in extract_table_names(schema_name, src_dict):
    df = extract(tbl, src_dict)
    df_dict[tbl] = df
    # print(f'{tbl} loaded successfully')

db = df_dict.copy()
print(db.keys())

transaction = db['transactions']
customer = db['customer']
promotion = db['promotion'] 
promotion_product = db['product_promotion']
product = db['product']
sub_category = db['sub_category']
category = db['category']
state = db['state']
branch = db['branch']
city = db['city']
casher = db['cashier']


def create_date_dim(df, date):
    day_of_week_dict = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
    month_dict = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    holiday_dates = ["01-01", "20-01", "17-02", "26-05", "04-07", "04-07", "01-09", "11-11", "27-11", "25-12"]
    last_days = ["31-01", "28-02", "31-03", "30-04", "31-05", "30-06", "31-07", "31-08", "30-09", "31-10", "30-11", "31-12"]
    df_date = df
    try:
        df_date['day_of_week'] = df_date[date].dt.dayofweek
        df_date['day_of_week'] = df_date['day_of_week'].map(day_of_week_dict)
        df_date['day_of_month'] = df_date[date].dt.day
        df_date['day_of_year'] = df_date[date].dt.dayofyear
        df_date['last_day_in_month_indecator'] = df_date[date].dt.strftime('%m-%d').apply(lambda x: 1 if x in last_days else 0)

        df_date['week_of_year'] = df_date[date].dt.isocalendar().week
        df_date['week_of_year'] = df_date['week_of_year'].astype(int)

        df_date['month'] = df_date[date].dt.month
        df_date['month_name'] = df_date['month'].map(month_dict)

        df_date['quarter'] = df_date[date].dt.quarter

        df_date['year'] = df_date[date].dt.year

        df_date['holiday_indicator'] = df_date[date].dt.strftime('%m-%d').apply(lambda x: 1 if x in holiday_dates else 0)
        df_date['weekday_indicator'] = df_date['day_of_week'].apply(lambda x: 1 if x in ['Sat', 'Sun'] else 0)
        return df_date
    except:
        return df

date_dim = transaction[['date']].drop_duplicates()
date_dim['date'] = pd.to_datetime(date_dim['date'])
date_dim.set_index('date', inplace=True)
date_dim = date_dim.resample('D').sum(numeric_only=True).sort_values(by='date').reset_index()
date_dim = create_date_dim(date_dim, 'date')
date_dim['date'] = date_dim['date'].dt.strftime('%Y-%m-%d')




product_dim = product.merge(sub_category, on='sub_category_id', how='inner').merge(category, on=
'category_id', how='inner').drop_duplicates().rename(columns={'index': 'category_sub_id'})
category_dim = product_dim.drop(columns=['product_name', 'price', 'product_id']).drop_duplicates().reset_index().rename(columns={'index': 'category_sub_id'})
category_dim['category_sub_id_k'] = category_dim['category_sub_id'] + df_id['category_sub_id'][0]

product_dim = product_dim.merge(category_dim, on=['category_id', 'sub_category_id'], how='inner').drop(columns=
['sub_name_y', 'category_name_y','sub_name_x','category_name_x']).reset_index().rename(columns={'index': 'product_id_k'})
product_dim['product_id_k'] = product_dim['product_id_k'] + df_id['product_id'][0]
customer_dim = customer.reset_index().rename(columns={'index': 'customer_id_k'})
customer_dim['customer_id_k'] = customer_dim['customer_id_k'] + df_id['customer_id'][0]

branch_dim = branch.merge(city, on='city_id', how='inner').merge(state, on='state_id', how='inner').reset_index().rename(columns={'index': 'branch_id_k'})
branch_dim['branch_id_k'] = branch_dim['branch_id_k'] + df_id['branch_id'][0]
casher_dim = casher.merge(branch_dim, on='branch_id', how='inner').drop(columns=
['branch_id','city_id','city_name','state_id','state_name','area','branch_name','branch_id']).reset_index().rename(columns={'index': 'casher_id_k'})
casher_dim['casher_id_k'] = casher_dim['casher_id_k'] + df_id['casher_id'][0]



promotion_dim = promotion.reset_index().rename(columns={'index': 'promotion_id_k'})
promotion_dim['promotion_id_k'] = promotion_dim['promotion_id_k'] + df_id['promotion_id'][0]
promotion_dim = promotion_dim.merge(promotion_product, on='promotion_id', how='inner')
product_dim = product_dim.merge(promotion_product, on='product_id', how='left').merge(promotion_dim, on='promotion_id', how='left')
promotion_dim = promotion_dim.drop(columns='product_id')
promotion_dim[['start_date','end_date']] = promotion_dim[['start_date','end_date']].map(lambda x: str(x)[:7])
product_dim = product_dim.iloc[:,:13].rename(columns={'product_id_x':'product_id'}).drop(columns=
['category_sub_id','start_date_x','end_date_x','discount_x','promotion_id'])


sales_fact = transaction.merge(product_dim[['product_id', 'product_id_k', 'category_sub_id_k', 'promotion_id_k']], on=
'product_id', how='inner').drop(columns='product_id').merge(customer_dim[['customer_id_k', 'customer_id']], on=
'customer_id', how='inner').drop(columns='customer_id').merge(casher_dim[['casher_id_k', 'cashier_id', 'branch_id_k']], on=
'cashier_id', how='inner').drop(columns='cashier_id')
product_dim = product_dim.drop(columns=['sub_category_id','category_id'])


