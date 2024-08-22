import sqlite3

zoo = "zoo.db"
conn = sqlite3.connect(zoo)
cursor = conn.cursor()

#createing animal table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Animals (
    id INTEGER PRIMERY KEY,
    name TEXT NOT NULL,
    age  INTEGER NOT NULL,
    species TEXT NOT NULL,
    diet TEXT NOT NULL,
    fur_color TEXT,
    feather_color TEXT,
    scales TEXT,
    enclosure_id INTEGER,
    FOREIGN KEY(enclosure_id) REFERENCES Enclosures(id)           
    );
''')

cursor.execute(''' 
CREATE TABLE Enclosures(
    id INTEGER PRIMERY KEY,
    name TEXT NOT NULL,
    size REAL NOT NULL,
    capacity INTEGER NOT NULL,
    type TEXT NOT NULL    
                              
    );

''')

#ZOOkeeper table
cursor.execute(''' 
CREATE TABLE Zookeepers(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    experience INTEGER NOT NULL              
               
);

''')

#CREATING zookeeper_animal_assignments table
cursor.execute('''  
CREATE TABLE Zookeeper_animal_assignments(
    zookeeper_id INTEGER,
    animal_id INTEGER,
    PRIMARY KEY(zookeeper_id, animal_id),
    FOREIGN KEY(zookeeper_id) REFERENCES Zookeepers(id),
    FOREIGN KEY(animal_id) REFERENCES Animals(id)
);
''')

conn.commit()
conn.close()

class DatabaseManager:
    def __init__(self,zoo):
        self.conn = sqlite3.connect(zoo)
        self.cursor = self.conn.cursor()

