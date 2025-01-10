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

print(dwh['sales_fact'])