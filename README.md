# Health Hamlet – SQLite Database & Python Application

This project was developed as part of the **INF403 – Conception de Bases de Données** course (L2, Université Grenoble Alpes).

It consists of a **relational database designed in SQLite** and a **Python console application** allowing users to interact with the database through insertion, deletion, updates, and SQL queries.

The project theme is a *health hamlet*, managing patients, medical staff, services, diseases, and consultations.

---

## Features

- Relational database designed from a conceptual model (UML → relational schema)
- SQLite database with:
  - Tables, primary keys, foreign keys, and integrity constraints
  - Views for aggregated and derived information
- SQL scripts:
  - Schema creation
  - Valid data insertion
  - Invalid data insertion (to test constraints)
- Python console interface to:
  - Insert, update, and delete data
  - Execute various SQL queries (selection, joins, aggregations)
- Tabular display of query results using `PrettyTable`
- Safe service deletion using a default service ("Non affecté") to preserve personnel and consultation history


---

## Project Structure

```text
.
├── main.py # Python console application
├── utils/
│ └── db.py # SQLite connection and SQL script execution
├── data/
│ ├── Projet.sql # Database schema (tables, constraints, views)
│ ├── Insert_OK.sql # Valid data insertion script
│ └── Insert_NOK.sql # Invalid data insertion script
├── doc/
│ └── Projet.pdf # Project report (models and explanations)
├── requirements.txt # Python dependencies
└── README.md
```

---

## Requirements

- Python 3.x
- SQLite (included with Python)
- Python dependency:
  - `prettytable`

Install dependencies:
```bash
pip install -r requirements.txt
``` 

---

## How to Run
The SQLite database is automatically created and initialized from SQL scripts on first execution.

From the project root:
```bash
python3 main.py
```
On Windows you may need:
```bash
py main.py
```

Follow the on-screen menu to interact with the database.

---

## Notes
- `Insert_NOK.sql` contains intentionally invalid insertions to demonstrate database constraint enforcement.
- The database file (`data/Projet.db`) is generated automatically on first run. If you want a fresh start, delete `data/Projet.db` and run the program again.
- Foreign key constraints are enabled in the SQLite connection.
- The database schema follows a relational design derived from a UML conceptual model.
- When a service is deleted, all related personnel and consultations are automatically reassigned to a default service ("Non affecté") to preserve data integrity and history.

---

## Reset the database
Delete the generated database file and run again:
- Remove `data/Projet.db`
- Run `python3 main.py` (or `py main.py` on Windows)

---

## Authors
- Mariam Fathallah
- Isra Kucuksullu

