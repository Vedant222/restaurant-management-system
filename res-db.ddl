DROP TABLE IF EXISTS paid_to;
DROP TABLE IF EXISTS contains;
DROP TABLE IF EXISTS taken_by;
DROP TABLE IF EXISTS assigned_delivery;
DROP TABLE IF EXISTS assigned_waiter;
DROP TABLE IF EXISTS prepare;
DROP TABLE IF EXISTS pays;
DROP TABLE IF EXISTS places;
DROP TABLE IF EXISTS order;
DROP TABLE IF EXISTS bill;
DROP TABLE IF EXISTS item;
DROP TABLE IF EXISTS cashier;
DROP TABLE IF EXISTS delivery_person;
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS waiter;
DROP TABLE IF EXISTS chef;
DROP TABLE IF EXISTS manager;

-- Item
CREATE TABLE item(
    item_no BIGINT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    quantity BIGINT,
    description TEXT,
    PRIMARY KEY (item_no)
);

-- Cashier
CREATE TABLE cashier(
    id BIGINT NOT NULL,
    name TEXT NOT NULL,
    PRIMARY KEY (id)
);

-- Bill
CREATE TABLE bill(
    bill_no BIGINT NOT NULL,
    cashier_id BIGINT NOT NULL,
    waiter_id BIGINT NOT NULL,
    total_cost DECIMAL(10,2),
    tax DECIMAL(10,2),
    total_amount DECIMAL(10,2),
    order_details TEXT NOT NULL,
    chef_id BIGINT,
    FOREIGN KEY(cashier_id) REFERENCES cashier(id),
    FOREIGN KEY(waiter_id) REFERENCES waiter(waiter_id),
    PRIMARY KEY(bill_no)
);

-- Home delivery
CREATE TABLE delivery_person(
    id BIGINT NOT NULL,
    name TEXT NOT NULL,
    PRIMARY KEY (id)    
);

-- Customer
CREATE TABLE customer(
    phone VARCHAR(20) NOT NULL,
    name VARCHAR(50) NOT NULL,
    address TEXT,
    PRIMARY KEY (phone)
);

-- Waiter
CREATE TABLE waiter(
    waiter_id BIGINT NOT NULL,
    name TEXT NOT NULL,
    PRIMARY KEY (waiter_id)   
);

-- Chef
CREATE TABLE chef(
    chef_id BIGINT NOT NULL,
    name TEXT NOT NULL,
    PRIMARY KEY (chef_id)
);

-- Order
CREATE TABLE "order" (
    order_no BIGINT NOT NULL,
    order_date DATE NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    order_type TEXT CHECK (order_type='takeaway' or order_type='dine-in'),
    name TEXT,
    delivery_person_id BIGINT,
    delivery_fee DECIMAL(10,2),
    FOREIGN KEY(delivery_person_id) REFERENCES delivery_person(id),
    PRIMARY KEY (order_no)
);

-- Manager
CREATE TABLE manager(
    id BIGINT NOT NULL,
    contact BIGINT NOT NULL,
    name TEXT NOT NULL,
    PRIMARY KEY (id)
);

-- Paid to
CREATE TABLE paid_to(
    cashier_id BIGINT NOT NULL,
    bill_no BIGINT NOT NULL,
    FOREIGN KEY(cashier_id) REFERENCES cashier(id),
    FOREIGN KEY(bill_no) REFERENCES bill(bill_no)
);

-- Pays
CREATE TABLE pays(
    bill_no BIGINT NOT NULL,
    phone VARCHAR(20) NOT NULL,
    FOREIGN KEY(phone) REFERENCES customer(phone),
    FOREIGN KEY(bill_no) REFERENCES bill(bill_no)
);

-- Places
CREATE TABLE places(
    phone VARCHAR(20) NOT NULL,
    order_no BIGINT NOT NULL,
    FOREIGN KEY(phone) REFERENCES customer(phone),
    FOREIGN KEY(order_no) REFERENCES "order"(order_no)
);

-- Assigned delivery
CREATE TABLE assigned_delivery(
    phone VARCHAR(20) NOT NULL,
    delivery_person_id BIGINT NOT NULL,
    FOREIGN KEY(phone) REFERENCES customer(phone),
    FOREIGN KEY(delivery_person_id) REFERENCES delivery_person(id)
);

-- Assigned waiter
CREATE TABLE assigned_waiter(
    phone VARCHAR(20) NOT NULL,
    waiter_id BIGINT NOT NULL,
    FOREIGN KEY(phone) REFERENCES customer(phone),
    FOREIGN KEY(waiter_id) REFERENCES waiter(waiter_id)
);

-- Taken by
CREATE TABLE taken_by(
    waiter_id BIGINT NOT NULL,
    order_no BIGINT NOT NULL,
    FOREIGN KEY (waiter_id) REFERENCES waiter(waiter_id),
    FOREIGN KEY(order_no) REFERENCES "order"(order_no)
);

-- Contains
CREATE TABLE contains(
    item_no BIGINT NOT NULL,
    order_no BIGINT NOT NULL,
    FOREIGN KEY(item_no) REFERENCES item(item_no),
    FOREIGN KEY(order_no) REFERENCES "order"(order_no)
);

-- Prepare
CREATE TABLE prepare(
    chef_id BIGINT NOT NULL,
    order_no BIGINT NOT NULL,
    FOREIGN KEY(chef_id) REFERENCES chef(chef_id),
    FOREIGN KEY(order_no) REFERENCES "order"(order_no)
);

