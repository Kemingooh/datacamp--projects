DROP TABLE IF EXISTS "articles";

CREATE TABLE articles (
article_key VARCHAR PRIMARY KEY,
category VARCHAR,
headline VARCHAR,
short_description VARCHAR,
release_date VARCHAR,
keywords VARCHAR
);