-- CREATE SCHEMA solo_project_schema;

CREATE TABLE accounts
(
  user_id   INT          NULL    ,
  facebook  VARCHAR(255) NULL    ,
  instagram VARCHAR(255) NULL    ,
  twitter   VARCHAR(255) NULL    ,
  snapchat  VARCHAR(255) NULL    
);

CREATE TABLE brians
(
  brian_id INT           NOT NULL AUTO_INCREMENT,
  name     VARBINARY(45) NULL    ,
  PRIMARY KEY (brian_id)
);

CREATE TABLE entrys
(
  entry_id INT          NOT NULL AUTO_INCREMENT,
  name     VARCHAR(255) NULL    ,
  email    VARCHAR(255) NULL    ,
  PRIMARY KEY (entry_id)
);

CREATE TABLE likes
(
  likes_id INT NOT NULL AUTO_INCREMENT,
  user_id  INT NOT NULL,
  post_id  INT NOT NULL,
  PRIMARY KEY (likes_id)
);

CREATE TABLE postings
(
  post_id INT          NOT NULL AUTO_INCREMENT,
  post    VARCHAR(500) NULL    ,
  user_id INT          NULL    ,
  PRIMARY KEY (post_id)
);

CREATE TABLE ryans
(
  ryan_id INT         NOT NULL AUTO_INCREMENT,
  name    VARCHAR(45) NULL    ,
  PRIMARY KEY (ryan_id)
);

CREATE TABLE users
(
  user_id    INT          NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(255) NULL    ,
  last_name  VARCHAR(255) NULL    ,
  email      VARCHAR(255) NULL    ,
  password   VARCHAR(255) NULL    ,
  PRIMARY KEY (user_id)
);

CREATE TABLE vote
(
  vote_id  INT        NOT NULL AUTO_INCREMENT,
  entry_id INT        NULL    ,
  vote     VARCHAR(5) NULL    ,
  user_id  INT        NULL    ,
  PRIMARY KEY (vote_id)
);

ALTER TABLE postings
  ADD CONSTRAINT FK_users_TO_postings
    FOREIGN KEY (user_id)
    REFERENCES users (user_id);

ALTER TABLE accounts
  ADD CONSTRAINT FK_users_TO_accounts
    FOREIGN KEY (user_id)
    REFERENCES users (user_id);

ALTER TABLE likes
  ADD CONSTRAINT FK_users_TO_likes
    FOREIGN KEY (user_id)
    REFERENCES users (user_id);

ALTER TABLE likes
  ADD CONSTRAINT FK_postings_TO_likes
    FOREIGN KEY (post_id)
    REFERENCES postings (post_id);

ALTER TABLE vote
  ADD CONSTRAINT FK_users_TO_vote
    FOREIGN KEY (user_id)
    REFERENCES users (user_id);

ALTER TABLE vote
  ADD CONSTRAINT FK_entrys_TO_vote
    FOREIGN KEY (entry_id)
    REFERENCES entrys (entry_id);

INSERT INTO brians (name)
VALUES ('Brian'),('Bryon'),('Brion'),('Bryen'),('Bryin'),('Brien'),('Bryhan'),('Bryun'),('Briyn'),('Bryan');

INSERT INTO ryans (name)
VALUES ('Ryan'),('Rian'), ('Ryon'), ('Ryen'), ('Ryin'), ('Rhean'), ('Rhyan'), ('Rien'), ('Ryann'), ('Ryein'), ('Ryeon');