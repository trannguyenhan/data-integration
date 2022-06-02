CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_name text NOT NULL,
    destination text NOT NULL,
    is_initialized bit default 0,
    connection_str text);