DROP TABLE members;
DROP TABLE sessions;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    last_name VARCHAR (255),
    first_name VARCHAR (255),
    premium BOOLEAN,
    bookings INT
);

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    capacity INT,
    premium BOOLEAN
);