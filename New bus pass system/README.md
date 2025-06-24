# Online Bus Pass System

A web-based application to apply for and manage bus passes using Python and Flask.

## Features
- User can apply for bus passes.
- Admin can view and update application status.

## Setup
```bash
pip install flask
python app.py
```

## DB Initialization
Run the following SQL in SQLite:

```sql
CREATE TABLE bus_passes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    route TEXT,
    date_applied DATE,
    status TEXT
);
```