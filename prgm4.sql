use teju;
CREATE DATABASE shop;
USE shop;

-- Products Table
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50),
    Price DECIMAL(10,2),
    Stock INT
);

INSERT INTO Products (ProductID, ProductName, Price, Stock) VALUES
(1, 'Laptop', 60000, 10),
(2, 'Mobile', 20000, 15),
(3, 'Headphones', 2000, 50),
(4, 'Keyboard', 1500, 30);


SELECT * FROM Products;
