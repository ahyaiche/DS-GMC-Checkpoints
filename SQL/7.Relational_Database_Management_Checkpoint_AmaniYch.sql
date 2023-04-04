# 1. Convert the entity relationship diagram into relational model.
# wine(*NumW, Category, Year, Degree)
# producer(*NumP, FirstName, LastName, Region)
# harvest(#NumW, #NumP, Quantity)
# PS: * represents the primary key and # the foreign key

# 2. Give the list of the producers.
SELECT 
    FirstName, LastName
FROM
    producer;

# 3. Give the list of producers sorted by name.
SELECT 
    FirstName, LastName
FROM
    producer
ORDER BY FirstName;

# 4. Give the list of the producers of Sousse.
SELECT 
    FirstName, LastName
FROM
    producer
WHERE
    Region = 'Sousse';

# 5. Calculate the total quantity of wine produced having the number 12.
SELECT 
    SUM(Quantity) AS total_quantity
FROM
    harvest
WHERE
    NumW = 12;

# 6. Calculate the quantity of wine produced by category.
SELECT 
    h.sum(Quantity) AS Quantity_produced
FROM
    harvest AS h,
    wine AS w
WHERE
    h.NumW = w.NumW
GROUP BY w.Category;

# 7. Which producers in the Sousse region have harvested at least one wine in quantities greater than 300 liters? 
# We want the names and first names of the producers, sorted in alphabetical order.
SELECT 
    p.FirstName, p.LastName
FROM
    producer AS p
        INNER JOIN
    harvest AS h ON p.NumP = h.NumP
WHERE
    h.Quantity > 300 AND p.Region = 'Sousse'
ORDER BY p.FirstName , acs;

# 8. List the wine numbers that have a degree greater than 12 and that have been produced by producer number 24.
SELECT 
    w.NumW
FROM
    wine AS w,
    harvest AS h
WHERE
    w.NumP = h.NumP AND w.Degree > 12
        AND h.NumP = 24;
