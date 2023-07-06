PRAGMA foreign_keys = off;

BEGIN TRANSACTION;

DROP TABLE IF EXISTS student;

CREATE TABLE
    student (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
        name VARCHAR (32)
    );

INSERT INTO student (id, name) VALUES (1, 'Ivan');

INSERT INTO student (id, name) VALUES (2, 'Boris');

INSERT INTO student (id, name) VALUES (3, 'Roman');

COMMIT TRANSACTION;

PRAGMA foreign_keys = on;