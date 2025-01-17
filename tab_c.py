import pandas as pd

# Create DataFrames
# Category table
category_df = pd.DataFrame({
    'category_id': [1, 2, 3],
    'category_name': ['Electronics', 'Clothing', 'Home Appliances']
})

# Sub_category table
sub_category_df = pd.DataFrame({
    'sub_category_id': [101, 102, 103, 104],
    'sub_name': ['Smartphones', 'Laptops', 'Men\'s Wear', 'Refrigerators'],
    'category_id': [1, 1, 2, 3]
})

# Product table
product_df = pd.DataFrame({
    'product_id': [1001, 1002, 1003, 1004],
    'product_name': ['iPhone 13', 'MacBook Pro', 'Men\'s T-Shirt', 'Samsung Fridge'],
    'price': [999.99, 1999.99, 29.99, 899.99],
    'sub_category_id': [101, 102, 103, 104]
})

# Customer table
customer_df = pd.DataFrame({
    'customer_id': [501, 502, 503],
    'customer_name': ['John Doe', 'Jane Smith', 'Alice Johnson'],
    'age': [30, 25, 40],
    'gender': ['Male', 'Female', 'Female'],
    'phone': ['123-456-7890', '987-654-3210', '555-555-5555'],
    'email': ['john@example.com', 'jane@example.com', 'alice@example.com'],
    'marital_status': ['Married', 'Single', 'Married'],
    'has_children': [True, False, True]
})

# State table
state_df = pd.DataFrame({
    'state_id': [1, 2, 3],
    'state_name': ['California', 'Texas', 'New York']
})

# City table
city_df = pd.DataFrame({
    'city_id': [201, 202, 203],
    'city_name': ['Los Angeles', 'Houston', 'New York City'],
    'state_id': [1, 2, 3]
})

# Branch table
branch_df = pd.DataFrame({
    'branch_id': [301, 302, 303],
    'branch_name': ['LA Downtown', 'Houston Central', 'NYC Midtown'],
    'area': ['Downtown', 'Central', 'Midtown'],
    'city_id': [201, 202, 203]
})

# Cashier table
cashier_df = pd.DataFrame({
    'cashier_id': [401, 402, 403],
    'cashier_name': ['Mike Johnson', 'Sarah Lee', 'Chris Brown'],
    'age': [28, 34, 22],
    'phone': ['111-222-3333', '444-555-6666', '777-888-9999'],
    'gender': ['Male', 'Female', 'Male'],
    'hire_date': ['2020-01-15', '2019-05-20', '2021-03-10'],
    'salary': [3500.00, 4000.00, 3000.00],
    'branch_id': [301, 302, 303]
})

# Promotion table
promotion_df = pd.DataFrame({
    'promotion_id': [1, 2],
    'promotion_name': ['Summer Sale', 'Black Friday']
})

# Transactions table
transactions_df = pd.DataFrame({
    'transaction_id': [10001, 10002, 10003],
    'customer_id': [501, 502, 503],
    'product_id': [1001, 1002, 1003],
    'cashier_id': [401, 402, 403],
    'date': ['2023-10-01', '2023-10-02', '2023-10-03'],
    'time': ['10:15:00', '14:30:00', '09:45:00'],
    'quantity': [1, 1, 2],
    'sales_amount': [999.99, 1999.99, 59.98]
})

# Product_Promotion table

product_promotion_df = pd.DataFrame({
    'product_id': [1001, 1002],
    'promotion_id': [1, 2],
    'start_date': ['2023-07-01', '2023-11-24'],
    'end_date': ['2023-07-31', '2023-11-27'],
    'discount': [10.00, 20.00]
})

db = {
    'transaction': transactions_df,
    'customer': customer_df,
    'promotion': promotion_df,
    'promotion_product': product_promotion_df,
    'product': product_df,
    'sub_category': sub_category_df,
    'category': category_df,
    'state': state_df,
    'branch': branch_df,
    'city': city_df,
    'cashier': cashier_df
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