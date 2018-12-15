DROP Table if exists Profile;

Create Table if not exists Profile  (
    Name  TEXT PRIMARY KEY,
    Email Text NOT NULL UNIQUE,
    Password TEXT NOT NULL,
    Age INTEGER NOT NULL
)
