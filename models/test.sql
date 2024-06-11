Bin Amin
12:15 PM
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bio TEXT,
    user_id INTEGER UNIQUE,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO users (username, email) VALUES ('JohnDoe', 'john@example.com');

SELECT * FROM users;

UPDATE users SET email = 'john.doe@example.com' WHERE username = 'JohnDoe';

DELETE FROM users WHERE username = 'JohnDoe';