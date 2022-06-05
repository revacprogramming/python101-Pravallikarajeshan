#databases
CREATE TABLE yy( 
  name VARCHAR(128), 
  age INTEGER
);
DELETE FROM yy;
INSERT INTO yy(name, age) VALUES ('Amylee', 21);
INSERT INTO yy(name, age) VALUES ('Samy', 25);
INSERT INTO yy (name, age) VALUES ('Krish', 14);
INSERT INTO yy(name, age) VALUES ('Reggie', 27);
INSERT INTO Age (name, age) VALUES ('Praise', 36);
SELECT hex(name || age) AS X FROM yy ORDER BY X