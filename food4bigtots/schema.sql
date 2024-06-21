DROP TABLE IF EXISTS recipes;
DROP TABLE IF EXISTS categories;

-- Remember: SQL hates trailing commas!
CREATE TABLE recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    date TEXT NOT NULL,
    original TEXT,
    thumbnail TEXT NOT NULL
);

CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE mapping (
    recipe_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    FOREIGN KEY (recipe_id) REFERENCES recipes (id),
    FOREIGN KEY (category_id) REFERENCES categories (id)
);

-- Indices and tables cannot have the same name!
CREATE UNIQUE INDEX recipes_name ON recipes (name);
CREATE UNIQUE INDEX categories_name ON categories (name);