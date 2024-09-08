import sqlite3 as sql
from typing import List


class UserDb:
    def __init__(self, db_name: str = 'users.db') -> None:
        self.db_name = db_name
        self.create_table()

    def create_table(self) -> None:
        with sql.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Users (
                    user_id INTEGER PRIMARY KEY NOT NULL
                );
            """)
            conn.commit()

    def add_user(self, user_id: int) -> None:
        with sql.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Users (user_id) VALUES (?);", (user_id,))
            conn.commit()

    def get_users(self) -> List[int]:
        with sql.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT user_id FROM Users;")
            return [row[0] for row in cursor.fetchall()]

    def delete_user(self, user_id: int) -> None:
        with sql.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Users WHERE user_id = ?;", (user_id,))
            conn.commit()
