import pandas as pd 
from tab_c import db


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
casher = db['cashier']

###columns
# transaction: ['transaction_id', 'customer_id', 'product_id', 'cashier_id', 'date','time', 'quantity', 'sales_amount']
# customer: ['customer_id', 'customer_name', 'age', 'gender', 'phone', 'email','marital_status', 'has_children']
# promotion: ['promotion_id', 'promotion_name']
# promotion_product: ['product_id', 'promotion_id', 'start_date', 'end_date', 'discount']
# product: ['product_id', 'product_name', 'price', 'sub_category_id']
# sub_category: ['sub_category_id', 'sub_name', 'category_id']
# category: ['category_id', 'category_name']
# state: ['state_id', 'state_name']
# branch: ['branch_id', 'branch_name', 'area', 'city_id']
# city: ['city_id', 'city_name', 'state_id']
# cashier: ['cashier_id', 'cashier_name', 'age', 'phone', 'gender', 'hire_date','salary', 'branch_id'],

def create_date_dim(df, date):
    day_of_week_dict = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
    month_dict = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    holiday_dates = ["01-01", "20-01", "17-02", "26-05", "04-07", "04-07", "01-09", "11-11", "27-11", "25-12"]
    last_days = ["31-01", "28-02", "31-03", "30-04", "31-05", "30-06", "31-07", "31-08", "30-09", "31-10", "30-11", "31-12"]
    df_date = df
    try:
        #name of month ++ nummber of month ,  ++ weekday indecator, list of holdays
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
# print(date_dim)

df_id = pd.DataFrame(0, index=[0], columns=['casheir_id', 'branch_id', 'category_sub_id', 'product_id', 'promotion_id', 'customer_id'])
df_id.to_csv('log/id.csv', index=False)


# casher_dim = casher.drop(columns=['branch_id'])
# branch_dim = branch.merge(city, on='city_id', how='inner').drop(columns=['state_id_y']).rename(columns={'state_id_x': 'state_id'})
# branch_dim = branch_dim.merge(state, on='state_id', how='inner').drop(columns=['state_id', 'city_id'])
# category_dim = category.merge(sub_category, on='category_id', how='inner')
# customer_dim = customer
# product_dim = product.drop(columns=['sub_category_id'])
# promotion_dim = promotion.drop(columns=['start_date', 'end_date'])
# promotion_product_factless = promotion_product.copy()

