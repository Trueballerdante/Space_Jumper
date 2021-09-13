#creates the database and and tables. This script should only be ran once
import sqlite3

conn = sqlite3.connect("top_time.db")

c = conn.cursor()

#c.execute("""CREATE TABLE top_times(
#             name TEXT,
#             time REAL
#            )        
#            """)

conn.commit()
conn.close()