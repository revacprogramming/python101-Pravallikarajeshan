#databases
CREATE TABLE yyy( 
  name VARCHAR(128), 
  age INTEGER
);
DELETE FROM yyy;
INSERT INTO yyy (name, age) VALUES ('Amylee', 21);
INSERT INTO yyy(name, age) VALUES ('Samy', 25);
INSERT INTO yyy (name, age) VALUES ('Krish', 14);
INSERT INTO yyy (name, age) VALUES ('Reggie', 27);
INSERT INTO Age (name, age) VALUES ('Praise', 36);
SELECT hex(name || age) AS X FROM yyy ORDER BY X