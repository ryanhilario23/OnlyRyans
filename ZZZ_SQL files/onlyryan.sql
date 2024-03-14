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

-- CREATE TABLE ryan_entrys
-- (
--   entry_id INT          NOT NULL AUTO_INCREMENT,
--   name     VARCHAR(255) NULL    ,
--   email    VARCHAR(255) NULL    ,
--   PRIMARY KEY (entry_id)
-- );

-- CREATE TABLE ryans
-- (
--   ryan_id INT         NOT NULL AUTO_INCREMENT,
--   name    VARCHAR(45) NULL    ,
--   PRIMARY KEY (ryan_id)
-- );

-- INSERT INTO ryans (name)
-- VALUES ('Ryan'),('Rian'), ('Ryon'), ('Ryen'), ('Ryin'), ('Rhean'), ('Rhyan'), ('Rien'), ('Ryann'), ('Ryein'), ('Ryeon');

-- CREATE TABLE postings
-- (
--   post_id INT          NOT NULL AUTO_INCREMENT,
--   post    VARCHAR(500) NULL    ,
--   likes   INT          NULL    ,
--   user_id VARCHAR(255) NULL    ,
--   PRIMARY KEY (post_id)
-- );

-- ALTER TABLE postings
--   ADD CONSTRAINT FK_users_TO_postings
--     FOREIGN KEY (user_id)
--     REFERENCES users (user_id);


-- CREATE TABLE accounts
-- (
--   user_id   INT          NULL    ,
--   facebook  VARCHAR(255) NULL    ,
--   instagram VARCHAR(255) NULL    ,
--   twitter   VARCHAR(255) NULL    ,
--   snapchat  VARCHAR(255) NULL    
-- );

-- ALTER TABLE accounts
--   ADD CONSTRAINT FK_users_TO_accounts
--     FOREIGN KEY (user_id)
--     REFERENCES users (user_id);

				SELECT users.user_id, first_name, last_name, facebook, instagram, twitter, snapchat
                FROM users
                JOIN accounts ON accounts.user_id = users.user_id
                WHERE users.user_id = 1