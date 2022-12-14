CREATE TABLE CITIES(
    id_city NUMBER(8) NOT NULL PRIMARY KEY,
    name VARCHAR(255)
);


CREATE TABLE CLIENTS (
    id_clients NUMBER(8) NOT NULL PRIMARY KEY,
    id_type NUMBER(8),
    name VARCHAR(255),
    id_city NUMBER(8) NOT NULL,
    FOREIGN KEY (id_city) REFERENCES CITIES(id_city)
);


CREATE TABLE TRANSACTIONS(
    trx_id NUMBER(8) PRIMARY KEY,
    trx_customer_id NUMBER(16),
    trx_id_type NUMBER(65),
    trx_date NUMBER(16),
    trx_total_amount NUMBER(20),
    trx_type VARCHAR,
    cant NUMBER(8),
    city NUMBER(8) NOT NULL,


    FOREIGN KEY (city) REFERENCES CITIES(id_city)
    CHECK( trx_type = "In" or trx_type = "Out")
);