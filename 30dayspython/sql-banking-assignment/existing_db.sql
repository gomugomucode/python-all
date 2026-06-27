-- Create the schema if it does not exist
CREATE SCHEMA IF NOT EXISTS banking;

-- Drop tables in reverse order of dependencies to avoid foreign key conflicts
DROP TABLE IF EXISTS banking.transactions;
DROP TABLE IF EXISTS banking.accounts;
DROP TABLE IF EXISTS banking.customers;
DROP TABLE IF EXISTS banking.branches;

-- =====================================
-- TABLE: banking.branches
-- =====================================
CREATE TABLE banking.branches (
    branch_id INT PRIMARY KEY,
    branch_name VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    address VARCHAR(200),
    phone_number VARCHAR(20)
);

-- =====================================
-- TABLE: banking.customers
-- =====================================
CREATE TABLE banking.customers (
    customer_id INT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    date_of_birth DATE,
    city VARCHAR(100),
    address VARCHAR(200),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================
-- TABLE: banking.accounts
-- =====================================
CREATE TABLE banking.accounts (
    account_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    branch_id INT NOT NULL,
    account_number VARCHAR(30) UNIQUE NOT NULL,
    account_type VARCHAR(20) NOT NULL
        CHECK (account_type IN ('SAVINGS', 'CURRENT', 'FIXED_DEPOSIT')),
    balance NUMERIC(14,2) DEFAULT 0
        CHECK (balance >= 0),
    opened_date DATE NOT NULL,
    account_status VARCHAR(20) DEFAULT 'ACTIVE'
        CHECK (account_status IN ('ACTIVE', 'CLOSED', 'FROZEN')),

    CONSTRAINT fk_account_customer
        FOREIGN KEY (customer_id)
        REFERENCES banking.customers(customer_id),

    CONSTRAINT fk_account_branch
        FOREIGN KEY (branch_id)
        REFERENCES banking.branches(branch_id)
);

-- =====================================
-- TABLE: banking.transactions
-- =====================================
CREATE TABLE banking.transactions (
    transaction_id INT PRIMARY KEY,
    account_id INT NOT NULL,
    transaction_type VARCHAR(20) NOT NULL
        CHECK (transaction_type IN ('DEPOSIT', 'WITHDRAWAL', 'TRANSFER')),
    transaction_amount NUMERIC(12,2) NOT NULL
        CHECK (transaction_amount > 0),
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description VARCHAR(255),

    CONSTRAINT fk_transaction_account
        FOREIGN KEY (account_id)
        REFERENCES banking.accounts(account_id)
);


-- Branches
INSERT INTO banking.branches
VALUES
(1,'Kathmandu Main Branch','Kathmandu','New Road','014567890'),
(2,'Pokhara Branch','Pokhara','Lakeside','061234567'),
(3,'Butwal Branch','Butwal','Traffic Chowk','071987654');

-- Customers
INSERT INTO banking.customers
VALUES
(101,'Anupam Baral','anupam@gmail.com','9800000001','2002-05-10','Kathmandu','Baneshwor',CURRENT_TIMESTAMP),
(102,'Sita Sharma','sita@gmail.com','9800000002','1998-08-15','Pokhara','Lakeside',CURRENT_TIMESTAMP),
(103,'Ram Thapa','ram@gmail.com','9800000003','1995-02-20','Butwal','Golpark',CURRENT_TIMESTAMP);

-- Accounts
INSERT INTO banking.accounts
VALUES
(1001,101,1,'ACC1001','SAVINGS',50000,'2025-01-01','ACTIVE'),
(1002,102,2,'ACC1002','CURRENT',120000,'2025-02-15','ACTIVE'),
(1003,103,3,'ACC1003','SAVINGS',75000,'2025-03-01','ACTIVE');

-- Transactions
INSERT INTO banking.transactions
VALUES
(1,1001,'DEPOSIT',10000,CURRENT_TIMESTAMP,'Initial Deposit'),
(2,1001,'WITHDRAWAL',2000,CURRENT_TIMESTAMP,'ATM Withdrawal'),
(3,1002,'DEPOSIT',50000,CURRENT_TIMESTAMP,'Salary Credit'),
(4,1003,'TRANSFER',10000,CURRENT_TIMESTAMP,'Fund Transfer');

SELECT * FROM banking.transactions;