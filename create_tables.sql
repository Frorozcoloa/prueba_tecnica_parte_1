
--DROP TABLE ALERTA;
CREATE TABLE Alerts(
    id_trx NUMBER(8) NOT NULL PRIMARY KEY
);

--DROP TABLE TOWNS;
CREATE TABLE Towns(
    id NUMBER(8) NOT NULL PRIMARY  KEY,
    Town VARCHAR(255)
);

--DROP TABLE USER;
CREATE TABLE Users(
    id_user VARCHAR(255) PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email  VARCHAR(255),
    gender VARCHAR(10),
    Town  VARCHAR(255)
);

--DROP TABLE TRX;
CREATE TABLE Trx(
    id_trx NUMBER(8) NOT NULL PRIMARY KEY,
    id_user VARCHAR(255),
    token_id VARCHAR(255),
    value  Number(10),
    trx_city VARCHAR(255),
    ip_address VARCHAR(255),

     FOREIGN KEY(id_user) REFERENCES  USER(user_id)

);

--DROP TABLE TOKEN_ID;
CREATE TABLE Token_id(
    id_user VARCHAR(255),
    token_id VARCHAR(255),
    id_type VARCHAR(3),

    FOREIGN KEY(id_user) REFERENCES  USER(user_id)
);

/*
CREATE TABLE Master (
    id Number(8) NOT NULL PRIMARY KEY,
    id_trx NUMBER(8),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email  VARCHAR(255),
    gender VARCHAR(10),
    Town  VARCHAR(255),
    is_claim BOOLEAN;
);
*/
