import sqlite3

class Database:
    def __init__(self, path_to_db="sqlite.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
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


    def selectGradesAll(self):
        sql = "SELECT * FROM grades WHERE status = ?"
        return self.execute(sql,(1,), fetchall=True)

    def selectOne(self, grade_id):
        sql = "SELECT * FROM grades WHERE id = ?"
        return self.execute(sql,(grade_id,), fetchall=True)

    def updateGrade(self, grade, type, gradeId):
        sql = """
        UPDATE grades SET grade=?, type=? WHERE id=?
        """
        return self.execute(sql, parameters=(grade, type, gradeId), commit=True)

    def deleteGrade(self, gradeId):
        sql = """
        UPDATE grades SET status=? WHERE id=?
        """
        return self.execute(sql, parameters=(0, gradeId), commit=True)
