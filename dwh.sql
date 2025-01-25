-- Date Dimension Table
CREATE TABLE date_dim (
    date_id_sk INT,                      -- Surrogate Key
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

-- Category Dimension Table
CREATE TABLE category_dim (
    category_sub_id_sk INT,              -- Surrogate Key
    category_sub_id_bk INT,              -- Business Key
    category_id INT,
    category_name VARCHAR(255),
    sub_category_id INT,
    sub_name VARCHAR(255)
);

-- Product Dimension Table
CREATE TABLE product_dim (
    product_id_sk INT,                   -- Surrogate Key
    product_id_bk INT,                   -- Business Key
    product_name VARCHAR(255),
    price DECIMAL(10, 2),
    category_id INT,
    sub_category_id INT,
    category_sub_id_sk INT,              -- Foreign Key to category_dim
    promotion_id_sk INT                  -- Foreign Key to promotion_dim
);

-- Customer Dimension Table
CREATE TABLE customer_dim (
    customer_id_sk INT,                  -- Surrogate Key
    customer_id_bk INT,                  -- Business Key
    customer_name VARCHAR(255),
    age INT,
    gender VARCHAR(10),
    phone VARCHAR(15),
    email VARCHAR(255),
    marital_status VARCHAR(20),
    has_children INT
);

-- Branch Dimension Table
CREATE TABLE branch_dim (
    branch_id_sk INT,                    -- Surrogate Key
    branch_id_bk INT,                    -- Business Key
    branch_name VARCHAR(255),
    city_id INT,
    city_name VARCHAR(255),
    state_id INT,
    state_name VARCHAR(255),
    area VARCHAR(255)
);

-- Cashier Dimension Table
CREATE TABLE cashier_dim (
    cashier_id_sk INT,                   -- Surrogate Key
    cashier_id_bk INT,                   -- Business Key
    cashier_name VARCHAR(255),
    age INT,                             -- Added missing column
    phone VARCHAR(15),                   -- Added missing column
    gender VARCHAR(10),                  -- Added missing column
    hire_date DATE,                      -- Added missing column
    salary DECIMAL(10, 2),               -- Added missing column
    branch_id_sk INT                     -- Foreign Key to branch_dim
);

-- Promotion Dimension Table
CREATE TABLE promotion_dim (
    promotion_id_sk INT,                 -- Surrogate Key
    promotion_id_bk INT,                 -- Business Key
    promotion_name VARCHAR(255),
    start_date VARCHAR(7),
    end_date VARCHAR(7),
    discount DECIMAL(5, 2)
);

-- Sales Fact Table
CREATE TABLE sales_fact (
    sales_id INT,
    date_id_sk INT,                      -- Foreign Key to date_dim
    product_id_sk INT,                   -- Foreign Key to product_dim
    customer_id_sk INT,                  -- Foreign Key to customer_dim
    cashier_id_sk INT,                   -- Foreign Key to cashier_dim
    branch_id_sk INT,                    -- Foreign Key to branch_dim
    promotion_id_sk INT,                 -- Foreign Key to promotion_dim
    quantity INT,
    total_amount DECIMAL(10, 2),
    time INT
);