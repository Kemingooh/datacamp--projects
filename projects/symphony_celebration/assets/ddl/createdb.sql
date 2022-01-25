DROP TABLE IF EXISTS "soloists";
DROP TABLE IF EXISTS "concerts";

CREATE TABLE soloists
(
    entry_number       INT PRIMARY KEY,
    soloist_instrument VARCHAR,
    soloist_name       VARCHAR,
    soloist_roles      VARCHAR,
    season             VARCHAR,
    program_id         INT,
    id                 VARCHAR
);

CREATE TABLE concerts
(
    concertNumber INT PRIMARY KEY,
    Date          VARCHAR,
    Location      VARCHAR,
    Time          VARCHAR,
    Venue         VARCHAR,
    eventType     VARCHAR,
    season        VARCHAR,
    programID     INT,
    orchestra     VARCHAR,
    id            VARCHAR
);
