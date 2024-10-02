-- database code

-- Creating customers table
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255),
    phone VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Creating interactions table
CREATE TABLE interactions (
    interaction_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    interaction_type VARCHAR(50),
    interaction_date DATE,
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Creating sales table
CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    product VARCHAR(100),
    amount DECIMAL(10, 2),
    sale_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
