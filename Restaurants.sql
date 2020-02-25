CREATE database restaurantpath;

CREATE TABLE Restaurants (id INT(10),hotelname VARCHAR(50));

CREATE TABLE Users (id INT(10) null,username VARCHAR(50));

CREATE TABLE traffic (id INT(10),traficplace VARCHAR(30),possiblity VARCHAR(30));

CREATE TABLE actualtiming(id INT(10),hotelid INT(10),userid INT(10),distance VARCHAR(30),time VARCHAR(30));

CREATE TABLE probability (id INT(10),hotelid INT(10),trafficid INT(10));


INSERT INTO Restaurants VALUES (100, 'Hyat');
INSERT INTO Restaurants VALUES (101, 'Park Plaza');
INSERT INTO Restaurants VALUES (102, 'Hilton');
INSERT INTO Restaurants VALUES (103, 'Hablies');

INSERT INTO Users VALUES (1, 'Dhivya');



INSERT INTO traffic values (1000, 'School',50);
INSERT INTO traffic values (1001, 'Hospital',70);
INSERT INTO traffic values (1002, 'Mall',40);
INSERT INTO traffic values (1003, 'It',55);
INSERT INTO traffic values (1004, 'Accidents',25);
INSERT INTO traffic values (1005, 'Free',100);


INSERT INTO actualtiming values (2000, '100','1',500,30);
INSERT INTO actualtiming values (2001, '101','1',600,40);
INSERT INTO actualtiming values (2002, '102','1',700,50);
INSERT INTO actualtiming values (2003, '103','1',800,60);

insert into probability values(3000,100,1000);
insert into probability values(3001,100,1001);
insert into probability values(3002,100,1003);
insert into probability values(3003,100,1004);

insert into probability values(3004,101,1000);
insert into probability values(3005,101,1002);
insert into probability values(3006,101,1003);

insert into probability values(3007,102,1002);
insert into probability values(3008,102,1004);

insert into probability values(3009,103,1000);


select * from Users;
select * from Restaurants;
select * from traffic;
select * from actualtiming;
select * from probability;



