
-- =====================================
-- TABLE: banking.employees
-- =====================================

CREATE TABLE banking.employees (
    employee_id INT PRIMARY KEY,
    branch_id INT NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    job_title VARCHAR(50) NOT NULL,
    salary NUMERIC(12,2) NOT NULL CHECK (salary > 0),
    hire_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,

    CONSTRAINT fk_employee_branch
        FOREIGN KEY (branch_id)
        REFERENCES banking.branches(branch_id)
);

-- =====================================
-- TABLE: banking.loans
-- =====================================

CREATE TABLE banking.loans (
    loan_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    branch_id INT NOT NULL,

    loan_type VARCHAR(20) NOT NULL
        CHECK (loan_type IN ('HOME', 'AUTO', 'PERSONAL', 'BUSINESS')),

    loan_amount NUMERIC(14,2) NOT NULL
        CHECK (loan_amount > 0),

    interest_rate NUMERIC(5,2) NOT NULL
        CHECK (interest_rate BETWEEN 0 AND 30),

    start_date DATE NOT NULL,

    end_date DATE NOT NULL
        CHECK (end_date > start_date),

    loan_status VARCHAR(20) DEFAULT 'ACTIVE'
        CHECK (loan_status IN ('ACTIVE', 'CLOSED', 'DEFAULTED')),

    CONSTRAINT fk_loan_customer
        FOREIGN KEY (customer_id)
        REFERENCES banking.customers(customer_id),

    CONSTRAINT fk_loan_branch
        FOREIGN KEY (branch_id)
        REFERENCES banking.branches(branch_id)
);

  -- =====================================
-- TABLE: banking.loan_payments
-- =====================================

CREATE TABLE banking.loan_payments (
    payment_id INT PRIMARY KEY,

    loan_id INT NOT NULL,

    payment_amount NUMERIC(12,2) NOT NULL
        CHECK (payment_amount > 0),

    payment_date DATE NOT NULL,

    payment_method VARCHAR(30) NOT NULL
        CHECK (
            payment_method IN (
                'CASH',
                'BANK_TRANSFER',
                'CHEQUE',
                'ONLINE'
            )
        ),

    payment_status VARCHAR(20) DEFAULT 'COMPLETED'
        CHECK (
            payment_status IN (
                'COMPLETED',
                'PENDING',
                'FAILED'
            )
        ),

    CONSTRAINT fk_payment_loan
        FOREIGN KEY (loan_id)
        REFERENCES banking.loans(loan_id)
);

SELECT * FROM banking.loans;
