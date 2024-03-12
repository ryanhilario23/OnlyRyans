-- CREATE SCHEMA onlyRyans_schema

-- CREATE TABLE brians
-- (
--   brian_id INT           NOT NULL AUTO_INCREMENT,
--   name     VARCHAR(45) NULL    ,
--   PRIMARY KEY (brian_id)
-- );

-- INSERT INTO brians (name)
-- VALUES ('Brian'),('Bryon'),('Brion'),('Bryen'),('Bryin'),('Brien'),('Bryhan'),('Bryun'),('Briyn'),('Bryan');

-- CREATE TABLE users
-- (
--   user_id    INT          NOT NULL AUTO_INCREMENT,
--   first_name VARCHAR(255) NULL    ,
--   last_name  VARCHAR(255) NULL    ,
--   email      VARCHAR(255) NULL    ,
--   password   VARCHAR(255) NULL    ,
--   PRIMARY KEY (user_id)
-- );

CREATE TABLE ryan_entrys
(
  entry_id INT          NOT NULL AUTO_INCREMENT,
  name     VARCHAR(255) NULL    ,
  email    VARCHAR(255) NULL    ,
  PRIMARY KEY (entry_id)
);

CREATE TABLE ryans
(
  ryan_id INT         NOT NULL AUTO_INCREMENT,
  name    VARCHAR(45) NULL    ,
  PRIMARY KEY (ryan_id)
);