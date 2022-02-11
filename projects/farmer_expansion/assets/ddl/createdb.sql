DROP TABLE IF EXISTS "purchases_2019";
DROP TABLE IF EXISTS "purchases_2020";
DROP TABLE IF EXISTS "categories";

CREATE TABLE purchases_2019
(
    member_id   INT,
    full_date   VARCHAR(50),
    year        INT,
    month       INT,
    day         INT,
    day_of_week INT,
    purchase_id VARCHAR PRIMARY KEY
);

CREATE TABLE purchases_2020
(
    MemberID   INT,
    FullDate   VARCHAR(50),
    DayofWeek  INT,
    PurchaseID VARCHAR PRIMARY KEY
);

CREATE TABLE categories
(
    purchase_id VARCHAR PRIMARY KEY,
    category    VARCHAR
);
