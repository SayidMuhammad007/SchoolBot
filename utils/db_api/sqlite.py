import sqlite3


class Database:
    def init(self, path_to_db="sqlite.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        # connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def addGrade(self, grade: int, type: str):

        sql = """
        INSERT INTO grades(grade, type) VALUES(?, ?)
        """
        self.execute(sql, parameters=(grade, type), commit=True)


    def select_product_by_user(self, user_id):
        sql = "SELECT * FROM Products WHERE user_id = ?"
        return self.execute(sql,(user_id,), fetchall=True)

    def check(self, user_id, id):
        sql = "SELECT * FROM Products WHERE user_id = ? AND product_id = ?"
        return self.execute(sql,(user_id, id,), fetchall=True)

    def update_product(self, quantity, user_id, product_id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Products SET quantity=? WHERE user_id=? AND product_id=?
        """
        return self.execute(sql, parameters=(quantity, user_id, product_id), commit=True)

    def delete_products_by_user(self,user_id):
        sql = f"DELETE FROM Products WHERE user_id = {user_id}"
        return self.execute(sql,  commit=True)

