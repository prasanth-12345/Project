import sqlite3

def create_db():
    con = sqlite3.connect(database="project.db")
    cur = con.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Course (
            cid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            duration TEXT,
            charges TEXT,
            description TEXT 
        )
    """)
    
    con.commit()
    print("Table created or already exists.")  # Confirmation message
    con.close()

create_db()  # Ensure this is called
 
