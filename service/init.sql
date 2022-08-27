-- System
DROP TABLE IF EXISTS sessions;

CREATE TABLE IF NOT EXISTS sessions (
--  One to Many
    session_id integer,
    session_date timestamp with time zone,
--  пометка отправки
    city_id integer,
    web_url text,
    hall_name text,
    movie_id integer,
    movie_name text,
    movie_poster_url text,
    movie_duration integer,
    status text default 'in process',
    deleted boolean default false
);

CREATE TABLE IF NOT EXISTS channels (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ext_id integer,
--  One to Many
    city_id integer,
    is_active boolean default false,
    deleted boolean default false
);

CREATE TABLE IF NOT EXISTS admins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ext_id integer,
--  One to Many
    city_id integer,
    is_active boolean default false,
    deleted boolean default false
);

---- Dictionaries
--CREATE TABLE IF NOT EXISTS cities (
--    id INTEGER PRIMARY KEY AUTOINCREMENT,
--    ext_id integer,
--    title text,
--    deleted boolean default false
--);

----Inserts
--INSERT OR IGNORE INTO cities
--VALUES (1, 1, 'Астана', false);
--INSERT OR IGNORE INTO cities
--VALUES (2, 2, 'Алматы', false);
--INSERT OR IGNORE INTO cities
--VALUES (3, 3, 'Шимкент', false);