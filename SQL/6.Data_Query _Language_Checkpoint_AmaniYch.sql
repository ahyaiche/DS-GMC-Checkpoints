create database gmc_vh;
use gmc_vh;

# Create the tables
CREATE TABLE customers (
    customer_id VARCHAR(20) NOT NULL,
    cust_name VARCHAR(20) NOT NULL,
    adress VARCHAR(50) NOT NULL,
    PRIMARY KEY (customer_id)
);

CREATE TABLE products (
    product_id VARCHAR(20),
    prod_name VARCHAR(20) NOT NULL,
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

# Insert values into tables
insert into customers values (1, 'Alice', '123 Main St.'), (2, 'Bob', '456 Market St.'), (3, 'Charlie', '789 Elm St.');
insert into products values (1, 'Widget', 10.00), (2, 'Gadget', 20.00), (3, 'Doohickey', 15.00);
insert into orders values (1, 1, 1, 10, '2021-01-01'), (2, 1, 2, 5, '2021-01-02'), (3, 2, 1, 3, '2021-01-03'), 
							(4, 2, 2, 7, '2021-01-04'), (5, 3, 1, 2, '2021-01-05'), (6, 3, 3, 3, '2021-01-06');

# Display the tables
select * from customers;
select * from products;
select * from orders;

# 1. Write an SQL query to retrieve the names of the customers who have placed an order for at least one widget and at least one gadget, along with the total cost of 
# the widgets and gadgets ordered by each customer. The cost of each item should be calculated by multiplying the quantity by the price of the product.
SELECT 
    c.cust_name, SUM(o.quantity * p.price) AS total_cost
FROM
    customers AS c,
    orders AS o,
    products AS p
WHERE
    c.customer_id = o.customer_id
        AND o.product_id = p.product_id
        AND (o.product_id = 1 OR o.product_id = 2)
        AND o.quantity >= 1
GROUP BY c.customer_id;

# 2. Write a query to retrieve the names of the customers who have placed an order for at least one widget, 
# along with the total cost of the widgets ordered by each customer.
SELECT 
    c.cust_name, SUM(o.quantity * p.price) AS total_cost
FROM
    customers AS c,
    orders AS o,
    products AS p
WHERE
    c.customer_id = o.customer_id
        AND o.product_id = p.product_id
        AND p.product_id = 1 
        AND o.quantity >= 1
GROUP BY c.customer_id;

# 3. Write a query to retrieve the names of the customers who have placed an order for at least one gadget, 
# along with the total cost of the gadgets ordered by each customer.
SELECT 
    c.cust_name, SUM(o.quantity * p.price) AS total_amount
FROM
    customers AS c,
    orders AS o,
    products AS p
WHERE
    c.customer_id = o.customer_id
	AND o.product_id = p.product_id
    AND p.product_id = 2 
    AND o.quantity >= 1
GROUP BY c.customer_id;

# 4. Write a query to retrieve the names of the customers who have placed an order for at least one doohickey, 
# along with the total cost of the doohickeys ordered by each customer.
SELECT 
    c.cust_name, SUM(o.quantity * p.price) AS total_amount
FROM
    customers AS c,
    orders AS o,
    products AS p
WHERE
    c.customer_id = o.customer_id
	AND o.product_id = p.product_id
    AND p.product_id = 3 
    AND o.quantity >= 1
GROUP BY c.customer_id;

# 5. Write a query to retrieve the total number of widgets and gadgets ordered by each customer, along with the total cost of the orders.
SELECT 
    c.cust_name,
    SUM(CASE
        WHEN p.product_id = 1 THEN o.quantity
        ELSE 0
    END) AS total_number_of_widgets,
    SUM(CASE
        WHEN p.product_id = 2 THEN o.quantity
        ELSE 0
    END) AS total_number_of_gadgets,
    SUM(o.quantity * p.price) AS total_amount
FROM
    customers AS c,
    orders AS o,
    products AS p
WHERE
    c.customer_id = o.customer_id
        AND o.product_id = p.product_id
GROUP BY c.customer_id;

# 6. Write a query to retrieve the names of the products that have been ordered by at least one customer, along with the total quantity of each product ordered.
SELECT 
    p.prod_name, SUM(o.quantity) AS total_quantity
FROM
    products AS p,
    orders AS o
WHERE
    o.product_id = p.product_id
        AND o.quantity >= 1
GROUP BY p.prod_name;

# 7. Write a query to retrieve the names of the customers who have placed the most orders, along with the total number of orders placed by each customer.
SELECT 
    c.cust_name, SUM(o.quantity) AS total_number_of_orders
FROM
    customers AS c,
    orders AS o
WHERE
    o.customer_id = c.customer_id
GROUP BY c.cust_name
ORDER BY total_number_of_orders DESC
LIMIT 3;

# 8. Write a query to retrieve the names of the products that have been ordered the most, along with the total quantity of each product ordered.
SELECT 
    p.prod_name, SUM(o.quantity) AS total_quantity_of_products
FROM
    products AS p,
    orders AS o
WHERE
    o.product_id = p.product_id
GROUP BY p.prod_name
ORDER BY total_quantity_of_products DESC
LIMIT 3;

# 9. Write a query to retrieve the names of the customers who have placed an order on every day of the week, 
# along with the total number of orders placed by each customer.
SELECT 
    c.cust_name,
    COUNT(DISTINCT DATE(o.order_date)) AS orders_placed
FROM
    customers c
        INNER JOIN
    orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id , c.cust_name
HAVING COUNT(DISTINCT DATE(o.order_date)) = 7;
