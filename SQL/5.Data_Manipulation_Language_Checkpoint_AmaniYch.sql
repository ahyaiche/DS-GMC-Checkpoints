create database gmc_vh;
use gmc_vh;

CREATE TABLE customers (
    customer_id VARCHAR(20) NOT NULL,
    name VARCHAR(20) NOT NULL,
    adress VARCHAR(50) NOT NULL,
    PRIMARY KEY (customer_id)
);

CREATE TABLE products (
    product_id VARCHAR(20),
    name VARCHAR(20) NOT NULL,
    price DECIMAL NOT NULL,
    CONSTRAINT price CHECK (price > 0),
    PRIMARY KEY (product_id)
);

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

# Fill the values of each table
# 1. customers table
insert into customers values (1, 'Alice', '123 Main St.'), (2, 'Bob', '456 Market St.'), (3, 'Charlie', '789 Elm St.');

# 2. products table
insert into products values (1, 'Widget', 10.00), (2, 'Gadget', 20.00), (3, 'Doohickey', 15.00);

# 3. orders table
insert into orders values (1, 1, 1, 10, '2021-01-01'), (2, 1, 2, 5, '2021-01-02'), (3, 2, 1, 3, '2021-01-03'), 
							(4, 2, 2, 7, '2021-01-04'), (5, 3, 1, 2, '2021-01-05'), (6, 3, 3, 3, '2021-01-06');

# 4. Display the filled tables
select * from customers;    
select * from products;
select * from orders;
