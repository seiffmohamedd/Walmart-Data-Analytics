CREATE TABLE date_dim (
    date_id INT PRIMARY KEY,
    date DATE NOT NULL,
    day_of_week VARCHAR(3),
    day_of_month INT,
    day_of_year INT,
    last_day_in_month_indicator INT,
    week_of_year INT,
    month INT,
    month_name VARCHAR(3),
    quarter INT,
    year INT,
    holiday_indicator INT,
    weekday_indicator INT
);

CREATE TABLE category_dim (
    category_sub_id INT,
    category_sub_id_bk INT,
    category_id INT,
    category_name VARCHAR(255),
    sub_category_id INT,
    sub_name VARCHAR(255)
);

CREATE TABLE product_dim (
    product_id INT,
    product_id_bk INT,
    product_name VARCHAR(255),
    price DECIMAL(10, 2),
    category_id INT,
    sub_category_id INT,
    category_sub_id_bk INT,
    promotion_id_bk INT
);
CREATE TABLE customer_dim (
    customer_id INT,
    customer_id_bk INT,
    customer_name VARCHAR(255),
    age INT,                   
    gender VARCHAR(10),        
    phone VARCHAR(15),        
    email VARCHAR(255),        
    marital_status VARCHAR(20),
    has_children INT      
);
CREATE TABLE branch_dim (
    branch_id INT,
	branch_id_bk INT,
    branch_name VARCHAR(255),
    city_id INT,
    city_name VARCHAR(255),
    state_id INT,
    state_name VARCHAR(255),
    area VARCHAR(255)
);
CREATE TABLE cashier_dim (
    cashier_id INT,
	cashier_id_bk INT,
    
    cashier_name VARCHAR(255),
    branch_id_bk INT
);
CREATE TABLE promotion_dim (
    promotion_id INT,
	promotion_id_bk INT,
    
    promotion_name VARCHAR(255),
    start_date VARCHAR(7),
    end_date VARCHAR(7),
    discount DECIMAL(5, 2)
);