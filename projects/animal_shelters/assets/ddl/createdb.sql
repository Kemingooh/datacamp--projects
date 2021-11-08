DROP TABLE IF EXISTS "animals";
DROP TABLE IF EXISTS "age_costs";
DROP TABLE IF EXISTS "location_costs";
DROP TABLE IF EXISTS "sponsored_animals";
DROP TABLE IF EXISTS "size_costs";

CREATE TABLE animals (
    animalid VARCHAR(50) PRIMARY KEY,
    birthdate VARCHAR(50),
    animaltype VARCHAR(50),
    color VARCHAR(50),
    weight REAL,
    location VARCHAR(50)
);

CREATE TABLE age_costs (
    age VARCHAR(50) PRIMARY KEY,
    costs INT
);

CREATE TABLE location_costs (
    location VARCHAR(50) PRIMARY KEY,
    costs INT
);

CREATE TABLE sponsored_animals (
    sponsorid varchar(50) PRIMARY KEY,
    animaltype VARCHAR(50),
    location VARCHAR(50)
);

CREATE TABLE size_costs (
    sizeid VARCHAR(50) PRIMARY KEY,
    animaltype VARCHAR(50),
    size VARCHAR(50),
    costs INT
);
