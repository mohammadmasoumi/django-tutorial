import sqlite3, os
from pathlib import Path
import time

try:
    db_path = os.path.join(Path(__file__).resolve().parent, 'db.sqlite3') 
    seed_sql = os.path.join(Path(__file__).resolve().parent, "seed.sql") 

    print("Database created and Successfully Connected to SQLite")
    # print(BASE_DIR)
    with open(seed_sql, "r") as f:
        sqlite_select_Query = ""
        
        new_cmd = 0
        for line in f.readlines():
            line = line.strip() 
            # print(line)
            # time.sleep(0.5)
            if line.startswith("insert into "):
                if new_cmd:
                    try:
                        new_cmd -= 1
                        # print(sqlite_select_Query[:1000])
                        sqliteConnection = sqlite3.connect(db_path)
                        cursor = sqliteConnection.cursor()
                        cursor.execute(sqlite_select_Query)
                        cursor.close()
                        sqlite_select_Query = ""
                    except Exception as e:
                        print("------------------------------")
                        print(e)
                else:
                    new_cmd += 1

            sqlite_select_Query += line.strip()

    # print(sqlite_select_Query)
    # cursor.execute(sqlite_select_Query)
    # sqlite_select_Query = "select sqlite_version();"
except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")