import sqlite3

class DBProxy:
    # Class responsible for handling database operations
    def __init__(self, db_name: str):
        # Initializes the database connection and creates the 'dados' table if it does not exist
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.connection.execute('''
                                   CREATE TABLE IF NOT EXISTS dados(
                                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                                   name TEXT NOT NULL,
                                   score INTEGER NOT NULL,
                                   date TEXT NOT NULL) 
                                ''')

    def save(self, score_dict: dict):
        # Saves a player's score in the 'dados' table
        self.connection.execute('INSERT INTO dados (name, score, date) VALUES (:name, :score, :date)', score_dict)
        self.connection.commit()

    def retrieve_top10(self) -> list:
        # Retrieves the top 10 highest scores from the 'dados' table
        return self.connection.execute('SELECT * FROM dados ORDER BY score DESC LIMIT 10').fetchall()

    def close(self):
        # Closes the database connection
        return self.connection.close()