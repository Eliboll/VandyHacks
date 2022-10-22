DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS cards;

CREATE TABLE users (
    userid INTEGER PRIMARY KEY AUTOINCREMENT,
    ccid TEXT NOT NULL,
    last_location TEXT NOT NULL,
    phone_number TEXT NOT NULL,
);

CREATE TABLE cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    specials TEXT NOT NULL,
    categories TEXT NOT NULL,
    base INTEGER NOT NULL,
    name TEXT not NULL,
    company TEXT not NULL
);