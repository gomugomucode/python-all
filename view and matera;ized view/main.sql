CREATE DATABASE bankingdb;

-- \c bankingdb;


CREATE TABLE customer (
    cust_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    nationality VARCHAR(50),
    phone VARCHAR(20),
    email VARCHAR(100),
    created_at DATE DEFAULT CURRENT_DATE
);

CREATE TABLE branch (
    branch_id SERIAL PRIMARY KEY,
    branch_name VARCHAR(100),
    province VARCHAR(50),
    district VARCHAR(50),
    city VARCHAR(50)
);

CREATE TABLE product (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    schm_type VARCHAR(5)
);


CREATE TABLE account (
    account_id SERIAL PRIMARY KEY,

    cust_id INT REFERENCES customer(cust_id),

    branch_id INT REFERENCES branch(branch_id),

    product_id INT REFERENCES product(product_id),

    account_balance NUMERIC(15,2),

    acct_crncy_code VARCHAR(5),

    acct_cls_flg CHAR(1),

    schm_type VARCHAR(5),

    open_date DATE
);

CREATE TABLE card (
    card_id SERIAL PRIMARY KEY,

    account_id INT REFERENCES account(account_id),

    card_number VARCHAR(20),

    card_type VARCHAR(20),

    expiry_date DATE
);


INSERT INTO branch(branch_name,province,district,city)
VALUES
('Kathmandu Main','Bagmati','Kathmandu','Kathmandu'),
('Pokhara Branch','Gandaki','Kaski','Pokhara'),
('Biratnagar Branch','Koshi','Morang','Biratnagar'),
('Butwal Branch','Lumbini','Rupandehi','Butwal'),
('Nepalgunj Branch','Lumbini','Banke','Nepalgunj'),
('Dhangadhi Branch','Sudurpashchim','Kailali','Dhangadhi');



INSERT INTO product(product_name,schm_type)
VALUES
('Savings Account','SA'),
('Current Account','CA'),
('Fixed Deposit','FD'),
('Recurring Deposit','RD'),
('Loan','LD');


INSERT INTO customer(customer_name,nationality,phone,email)
VALUES
('Ram Sharma','Nepali','9800000001','ram@gmail.com'),
('Sita Karki','Nepali','9800000002','sita@gmail.com'),
('Hari Thapa','Nepali','9800000003','hari@gmail.com'),
('Gita Rai','Nepali','9800000004','gita@gmail.com'),
('John Smith','American','9800000005','john@gmail.com'),
('Anita Gurung','Nepali','9800000006','anita@gmail.com'),
('Rabin KC','Nepali','9800000007','rabin@gmail.com'),
('Sunita Lama','Nepali','9800000008','sunita@gmail.com'),
('David Lee','Canadian','9800000009','david@gmail.com'),
('Mina Shrestha','Nepali','9800000010','mina@gmail.com');


INSERT INTO account
(cust_id,branch_id,product_id,account_balance,acct_crncy_code,acct_cls_flg,schm_type,open_date)
VALUES
(1,1,1,450000,'NPR','N','SA','2024-01-05'),
(1,1,3,850000,'NPR','N','FD','2024-02-10'),

(2,2,1,250000,'NPR','N','SA','2023-05-10'),
(2,2,5,1200000,'NPR','N','LD','2024-01-15'),

(3,3,2,90000,'USD','N','CA','2023-08-11'),

(4,1,1,310000,'NPR','N','SA','2024-03-12'),

(5,4,3,1500000,'USD','N','FD','2022-07-01'),

(6,5,5,700000,'NPR','N','LD','2023-11-09'),

(7,6,1,80000,'NPR','Y','SA','2021-02-14'),

(8,2,2,460000,'USD','N','CA','2022-09-17'),

(9,3,3,520000,'NPR','N','FD','2021-05-25'),

(10,1,4,180000,'NPR','N','RD','2022-12-31'),

(6,5,1,340000,'NPR','N','SA','2023-01-01'),

(3,3,5,650000,'USD','N','LD','2024-04-02'),

(8,2,3,930000,'NPR','N','FD','2024-06-11');


INSERT INTO card(account_id,card_number,card_type,expiry_date)
VALUES
(1,'1111222233334444','Debit','2028-01-01'),
(2,'1111222233335555','Credit','2028-01-01'),
(3,'1111222233336666','Debit','2029-03-01'),
(4,'1111222233337777','Credit','2028-06-01'),
(5,'1111222233338888','Debit','2029-01-01');