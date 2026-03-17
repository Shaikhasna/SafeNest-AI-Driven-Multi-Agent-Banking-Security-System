import sqlite3

class ComplianceAgent:

    def __init__(self):

        self.conn = sqlite3.connect("database/safenest.db")

        cursor = self.conn.cursor()

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS logs (user TEXT, decision TEXT)"
        )

        self.conn.commit()


    def log_event(self, user_id, decision):

        cursor = self.conn.cursor()

        cursor.execute(
            "INSERT INTO logs VALUES (?, ?)",
            (user_id, decision)
        )

        self.conn.commit()