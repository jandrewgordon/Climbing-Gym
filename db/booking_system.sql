DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS sessions;

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
    member_id SERIAL REFERENCES members(id),
    session_id SERIAL REFERENCES sessions(id),
);