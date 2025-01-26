-- Table: category_dim

CREATE TABLE IF NOT EXISTS category_dim (
    category_sub_id INT,
    category_sub_id_bk INT,
    category_id INT,
    category_name VARCHAR(255),
    sub_category_id INT,
    sub_name VARCHAR(255)
);

-- Table: customer_dim

CREATE TABLE IF NOT EXISTS customer_dim (
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

-- Table: date_dim

CREATE TABLE IF NOT EXISTS date_dim (
    date_id INT NOT NULL PRIMARY KEY,
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

-- Table: product_dim

CREATE TABLE IF NOT EXISTS product_dim (
    product_id INT,
    product_id_bk INT,
    product_name VARCHAR(255),
    price DECIMAL(10,2),
    category_id INT,
    sub_category_id INT,
    category_sub_id_bk INT,
    promotion_id_bk INT
);

-- Table: promotion_dim

CREATE TABLE IF NOT EXISTS promotion_dim (
    promotion_id INT,
    promotion_id_bk INT,
    promotion_name VARCHAR(255),
    start_date VARCHAR(7),
    end_date VARCHAR(7),
    discount DECIMAL(5,2)
);

-- Table: sales_fact

CREATE TABLE IF NOT EXISTS sales_fact (
    transaction_id BIGINT,
    time BIGINT,
    quantity BIGINT,
    sales_amount DOUBLE PRECISION,
    product_id_bk BIGINT,
    category_sub_id_bk BIGINT,
    promotion_id_bk DOUBLE PRECISION,
    customer_id_bk BIGINT,
    cashier_id_bk BIGINT,
    branch_id_bk BIGINT,
    date_id BIGINT
);