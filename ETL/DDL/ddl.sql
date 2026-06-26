CREATE SCHEMA IF NOT EXISTS Dimensional;

CREATE TABLE Dimensional.dim_order_payments (
  payment_key INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  payment_sequential INT NOT NULL,
  payment_type VARCHAR(50) NOT NULL,
  payment_installments INT NOT NULL
);

CREATE TABLE Dimensional.dim_sellers (
  seller_key INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  seller_id VARCHAR(50) NOT NULL,
  seller_city VARCHAR(100) NOT NULL,
  seller_state CHAR(2) NOT NULL,
  geolocation_lat NUMERIC(10, 8),
  geolocation_lng NUMERIC(11, 8)
);

CREATE TABLE Dimensional.dim_customers (
  customer_key INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  customer_unique_id VARCHAR(50) NOT NULL,
  customer_city VARCHAR(100) NOT NULL,
  customer_state CHAR(2) NOT NULL,
  geolocation_lat NUMERIC(10, 8),
  geolocation_lng NUMERIC(11, 8)
);

CREATE TABLE Dimensional.dim_items (
  item_key INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  product_id VARCHAR(50) NOT NULL,
  product_name_lenght INT,
  product_description_lenght INT,
  product_photos_qty INT,
  product_weight_g INT,
  product_length_cm INT,
  product_height_cm INT,
  product_width_cm INT,
  product_category_name_english VARCHAR(100),
  validity_start_date DATE NOT NULL,
  validity_end_date DATE NOT NULL
);

CREATE TABLE Dimensional.dim_time (
  time_key INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  datum_date DATE NOT NULL,
  time_day INT NOT NULL,
  time_month INT NOT NULL,
  time_year INT NOT NULL,
  time_weekday VARCHAR(20) NOT NULL,
  time_quarter CHAR(2) NOT NULL
);

CREATE TABLE Dimensional.fact_order_items (
  order_items_key INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  payment_key INT NOT NULL REFERENCES Dimensional.dim_order_payments(payment_key),
  seller_key INT NOT NULL REFERENCES Dimensional.dim_sellers(seller_key),
  customer_key INT NOT NULL REFERENCES Dimensional.dim_customers(customer_key),
  item_key INT NOT NULL REFERENCES Dimensional.dim_items(item_key),
  shipping_limite_date_key INT NOT NULL REFERENCES Dimensional.dim_time(time_key),
  order_purchase_timestamp_key INT NOT NULL REFERENCES Dimensional.dim_time(time_key),
  order_approved_at_key INT REFERENCES Dimensional.dim_time(time_key),
  order_delivered_carrier_date_key INT REFERENCES Dimensional.dim_time(time_key),
  order_delivered_customer_date_key INT REFERENCES Dimensional.dim_time(time_key),
  order_estimated_delivery_date_key INT NOT NULL REFERENCES Dimensional.dim_time(time_key),
  order_status VARCHAR(50) NOT NULL,
  order_id VARCHAR(50) NOT NULL,
  price NUMERIC(10, 2) NOT NULL,
  freight_value NUMERIC(10, 2) NOT NULL
);