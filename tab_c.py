import pandas as pd
 

dwh = dict(
    sales_fact=pd.DataFrame(columns=['customer_id', 'product_id', 'date_id', 'promotion_id', 'branch_id','cashier_id', 'quantity', 'sales_discount', 'sales_amount', 'time']),
    date_dim=pd.DataFrame(columns=['date_id', 'full_date_description', 'day_of_week', 'day_of_month', 'year', 'week_of_year', 'month_name']),
    cashier_dim=pd.DataFrame(columns=['cashier_id', 'cashier_name', 'cashier_email', 'cashier_phone']), 
    branch_dim=pd.DataFrame(columns=['branch_id', 'branch_area', 'city_name', 'state_name']),
    category_dim=pd.DataFrame(columns=['category_id', 'sub_id', 'category_name','sub_category_name']),
    customer_dim=pd.DataFrame(columns=['customer_id', 'name', 'email', 'phone', 'age', 'gender', 'martital_status', 'has_children']),
    product_dim=pd.DataFrame(columns=['product_id', 'product_name', 'price']),
    promotion_product_dim=pd.DataFrame(columns=['promotion_id', 'product_id','start_date','end_date', 'discount']),
    promotion_dim=pd.DataFrame(columns=['promotion_id', 'promotion_name'])
    )

import pandas as pd
import numpy as np

# Transaction DataFrame
transaction = pd.DataFrame({
    'transact_id': [1, 2, 3, 4, 5, 6],
    'customer_id': [101, 102, 103, 104, 105, 105],
    'product_id': [201, 202, 203, 204, 205, 205],
    'casher_id': [901, 902, 901, 902, 901, 901],
    'sales_discount': [0.1, 0.0, 0.2, 0.15, 0.05, 0.05],
    'sales_amount': [100, 200, 150, 300, 250, 250],
    'quantity': [1, 2, 1, 3, 2, 5],
    'date': ['2023-10-01', '2023-10-02', '2023-10-03', '2023-10-04', '2023-10-05', '2023-10-09'],
    'time': ['10:15', '11:30', '12:45', '14:00', '15:15', '15:15']
})

# Customer DataFrame
customer = pd.DataFrame({
    'customer_id': [101, 102, 103, 104, 105],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 40, 45],
    'gender': ['F', 'M', 'M', 'M', 'F'],
    'email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'david@example.com', 'eve@example.com'],
    'phone': ['123-456-7890', '234-567-8901', '345-678-9012', '456-789-0123', '567-890-1234'],
    'martital_status': ['Single', 'Married', 'Single', 'Married', 'Single'],
    'has_children': [False, True, False, True, False]
})

# Promotion DataFrame
promotion = pd.DataFrame({
    'promotion_id': [301, 302, 303],
    'promotion_name': ['Summer Sale', 'Winter Sale', 'Clearance'],
    'start_date': ['2023-06-01', '2023-12-01', '2023-09-01'],
    'end_date': ['2023-06-30', '2023-12-31', '2023-09-30']
})

# Promotion Product DataFrame
promotion_product = pd.DataFrame({
    'promotion_id': [301, 302, 303, 303],
    'product_id': [201, 202, 203, 202],
    'discount': [0.1, 0.2, 0.15, 0.15],
    'start_date': ['2023-06-01', '2023-12-01', '2023-09-01', '2023-09-01'],
    'end_date': ['2023-06-30', '2023-12-31', '2023-09-30', '2023-10-30']
})

# Product DataFrame
product = pd.DataFrame({
    'product_id': [201, 202, 203, 204, 205],
    'product_name': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch'],
    'price': [1000, 500, 300, 150, 200],
    'sub_category_id': [401, 402, 403, 404, 405]
})

# Sub Category DataFrame
sub_category = pd.DataFrame({
    'sub_category_id': [401, 402, 403, 404, 405],
    'sub_category_name': ['Electronics', 'Mobile Devices', 'Portable Devices', 'Audio', 'Wearables'],
    'category_id': [501, 501, 501, 501, 501]
})

# Category DataFrame
category = pd.DataFrame({
    'category_id': [501],
    'category_name': ['Electronics']
})

# State DataFrame
state = pd.DataFrame({
    'state_id': [601, 602],
    'state_name': ['California', 'Texas']
})

# Branch DataFrame
branch = pd.DataFrame({
    'branch_id': [701, 702],
    'branch_area': ['Downtown', 'Uptown'],
    'city_id': [801, 802],
    'state_id': [601, 602]
})

# City DataFrame
city = pd.DataFrame({
    'city_id': [801, 802],
    'city_name': ['Los Angeles', 'Houston'],
    'state_id': [601, 602]
})

# Casher DataFrame
casher = pd.DataFrame({
    'casher_id': [901, 902],
    'name': ['John', 'Jane'],
    'age': [28, 32],
    'gender': ['M', 'F'],
    'email': ['john@example.com', 'jane@example.com'],
    'phone': ['111-222-3333', '444-555-6666'],
    'salary': [3000, 3500],
    'hire_date': ['2022-01-15', '2021-05-20'],
    'branch_id': [701, 702]
})

db = {
    'transaction': transaction,
    'customer': customer,
    'promotion': promotion,
    'promotion_product': promotion_product,
    'product': product,
    'sub_category': sub_category,
    'category': category,
    'state': state,
    'branch': branch,
    'city': city,
    'casher': casher
}



# def trasnfomr(dic):    
#     transaction = dic['transaction']
#     customer = dic['customer']
#     promotion = dic['promotion'] 
#     promotion_product = dic['promotion_product']
#     product = dic['product']
#     sub_category = dic['sub_category']
#     category = dic['category']
#     state = dic['state']
#     branch = dic['branch']
#     city = dic['city']
#     casher = dic['casher']