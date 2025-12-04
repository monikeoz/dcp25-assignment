# Data Centric Programming Assignment 2025

- [Assignment Brief](assignment.md)

Name: Monike Ozeias Santos

Student Number: C24300243

# Screenshots

### 1. GUI Interface
![GUI Screenshot](images/Screenshot 2025-12-04 164753.png)

### 2. Tune Details View
![Tune Details](images/Screenshot 2025-12-04 164845.png)

### 3. Terminal Output (Database Build)
![Build Output](images/Screenshot 2025-12-04 164825.png)

# Description of the project
This project is a Python application:

1. It loads and parses **ABC music notation files** from book folders.
2. Extracts metadata such as tune number (X), title (T), meter (M), key (K), and type (R).
3. Stores all parsed tunes into a SQLite Database.
4. Loads the data into pandas for analysis.
5. Provides an interactive Tkinter GUI allowing the user to:
   - Search tunes by title
   - Filter tunes by book or tune type
   - View tune details and tune body (notation)

The project demonstrates file parsing, data cleaning, SQL database creation, pandas-based analysis, and GUI design.

# Instructions for use
### 1. Build the database
Run this command:
```bash 
python build_dp.py

# How it works:
file_loader.py searches the abc_books directory and retrieves all ABC files along with their book number.

parser.py reads each ABC line by line. A new tune begins when a line starts with X: All metadata is extracted, and the remaining text is stored as the tune body

db_manager.py creates the SQLite tables, inserts parsed tunes, and manages favourite tunes

analysis.py uses pandas to filter by title, book and type. It also contains the matplotlib function that plots Tunes per Key

app.py provides an interface where users can interact with all the stored data

# List of files in the project

| Files | Source |
|-----------|-----------|
| analysis.py | Self written |
| app.py | Self written |
| build_db.py | Self written |
| db_manager.py | Self written |
| file_loader.py | Self written |
| parser.py| Self written |
| readme.md | Provided |
| abc_books/| Provided |
| tunes.db | Generated |
| images/ | Self written (screenshots for README) |


# References
* ABC Notation Standard — https://abcnotation.com
* Tkinter Documentation — https://docs.python.org/3/library/tkinter.html
* pandas Documentation — https://pandas.pydata.org/
* Matplotlib Documentation — https://matplotlib.org/
* SQLite Documentation — https://www.sqlite.org/
* Original assignment repository — https://github.com/skooter500/dcp25-assignment

# What I am most proud of in the assignment

Building a complete pipeline from raw text files to database to pandas to GUI
Creating an intuitive graphical interface
Implementing bonus features like favourites and data visualisation
Understanding how modular Python programs communicate across files

# What I learned

How to parse text formats, design and populate SQLite database, analyse data using pandas, build GUIs in Tkinter, handle larger projects with multiple modules, how to use Git and Github effectively 
