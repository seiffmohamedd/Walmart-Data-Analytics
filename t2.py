import pandas as pd 

df_id = pd.DataFrame(1, index=[0], columns=['casher_id', 'branch_id', 'category_sub_id', 'product_id', 'promotion_id', 'customer_id', 'date_id'])
df_id.to_csv('log/id.csv', index=False)


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
## seif committed