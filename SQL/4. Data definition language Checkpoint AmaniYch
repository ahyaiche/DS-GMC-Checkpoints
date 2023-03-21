## customers table has a “primary key” column customer_id, and the name, email, and address columns are all defined as “VARCHAR” with different maximum lengths and each is 
#marked as “NOT NULL”.
## products table has a “primary key” column product_id, and the name and price columns are defined as “VARCHAR” and “DECIMAL” respectively, 
#both are marked as “NOT NULL” and the price column has a “CHECK” constraint that ensures that the value is greater than 0.
## orders  table has a “primary key” column order_id, and the customer_id, product_id, quantity and order_date columns are defined as “INT”, “DATE” respectively, 
#all are marked as “NOT NULL”. The customer_id and product_id columns also have “FOREIGN KEY” constraints that reference the primary key columns of the customers and products 
#tables, respectively, to ensure that each order is associated with a valid customer and product.
## Instructions: You are asked to create the above given relational model using SQL language and based on the different mentioned constraints.

# 1.Create a database
create database gmc_vh;
use gmc_vh;

# 2.Create customers table
CREATE TABLE customers (
    customer_id VARCHAR(20) NOT NULL,
    customers_name VARCHAR(20) NOT NULL,
    email VARCHAR(30) NOT NULL,
    adress VARCHAR(50) NOT NULL,
    PRIMARY KEY (customer_id)
);

# 3. Create products table
CREATE TABLE products (
    product_id VARCHAR(20),
    products_name VARCHAR(20) NOT NULL,
    price DECIMAL NOT NULL,
    CONSTRAINT price CHECK (price > 0),
    PRIMARY KEY (product_id)
);

# 4. Create orders table
CREATE TABLE orders (
    order_id VARCHAR(20) NOT NULL,
    customer_id VARCHAR(20) NOT NULL,
    product_id VARCHAR(20) NOT NULL,
    quantity INT NOT NULL,
    order_date DATE NOT NULL,
    PRIMARY KEY (order_id),
    FOREIGN KEY (customer_id)
        REFERENCES customers (customer_id),
    FOREIGN KEY (product_id)
        REFERENCES products (product_id)
);

# 5. Display the tables
desc customers;    
desc products;
desc orders;
