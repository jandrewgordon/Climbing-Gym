DROP TABLE IF EXISTS sessions;
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS members;


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

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id),
    session_id INT REFERENCES sessions(id),
    booking_date VARCHAR (255)
);