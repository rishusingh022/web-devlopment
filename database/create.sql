CREATE TABLE flight(
	id SERIAL PRIMARY KEY,
	origin VARCHAR NOT NULL,
	destination VARCHAR NOT NULL,
	duration INTEGER NOT NULL
);

 INSERT INTO flight
     (origin, destination, duration)
     VALUES ('New York', 'London', 415);

insert.sql
INSERT INTO flight (origin, destination, duration) VALUES ('New York', 'London', 415);
INSERT INTO flight (origin, destination, duration) VALUES ('Shanghai', 'paris', 760);
INSERT INTO flight (origin, destination, duration) VALUES ('istanbul', 'tokyo', 700);
INSERT INTO flight (origin, destination, duration) VALUES ('New York', 'paris', 435);     
INSERT INTO flight (origin, destination, duration) VALUES ('moscow', 'paris', 245);
INSERT INTO flight (origin, destination, duration) VALUES ('lima', 'New York', 455);
INSERT INTO flight (origin, destination, duration) VALUES ('New York', 'London', 415);
INSERT INTO flight (origin, destination, duration) VALUES ('New York', 'London', 415);


select.sql
SELECT * FROM flight;
SELECT origin, destination FROM flight;
SELECT * FROM flight WHERE id = 3;
SELECT * FROM flight WHERE origin = 'New York';
SELECT * FROM flight WHERE duration > 500;
SELECT * FROM flight WHERE destination = 'Paris' AND duration > 500;
SELECT * FROM flight WHERE destination = 'Paris' OR duration > 500;
SELECT AVG(duration) FROM flight WHERE origin = 'New York';
SELECT * FROM flight WHERE origin LIKE '%a%';
SELECT * FROM flight LIMIT 2;
SELECT * FROM flight ORDER BY duration ASC;
SELECT * FROM flight ORDER BY duration ASC LIMIT 3;
SELECT origin, COUNT(*) FROM flight GROUP BY origin;
SELECT origin, COUNT(*) FROM flight GROUP BY origin HAVING COUNT(*) > 1;

UPDATE flight SET duration = 430 WHERE origin = 'New York' AND destination = 'London';

Deleting data from a table:

      DELETE FROM flight WHERE destination = 'Tokyo'

creting passengers table
postgres=# CREATE TABLE passengers(
postgres(#    id SERIAL PRIMARY KEY,
postgres(#    name VARCHAR NOT NULL,
postgres(#    flight_id INTEGER REFERENCES flight

inserting data into passengers table
INSERT INTO passengers (name,flight_id) VALUES ('alice',1);
INSERT INTO passengers (name,flight_id) VALUES ('bob',1);
INSERT INTO passengers (name,flight_id) VALUES ('charlie',2);
INSERT INTO passengers (name,flight_id) VALUES ('dava',2);     
INSERT INTO passengers (name,flight_id) VALUES ('erin',4);
INSERT INTO passengers (name,flight_id) VALUES ('frank',5);
INSERT INTO passengers (name,flight_id) VALUES ('grace',6);

now quering two diiferent tablr using join keyword
SELECT origin, destination, name FROM flight JOIN passengers ON passengers.flight_id = flight.id;
SELECT origin, destination, name FROM flight JOIN passengers ON passengers.flight_id = flight.id WHERE name = 'Alice';
SELECT origin, destination, name FROM flight LEFT JOIN passengers ON passengers.flight_id = flight.id;

Nested queries are yet another way to make more complex selections: #where id is from the resulted queer
SELECT * FROM flight WHERE id IN
(SELECT flight_id FROM passengers GROUP BY flight_id HAVING COUNT(*) > 1);
