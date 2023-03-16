


import sqlite3
class DataBase:

    def __init__(self, db_file):
        self.connect = sqlite3.connect(db_file)
        self.cursor = self.connect.cursor()

    async def add_users(self, user_id):
        with self.connect:
            return self.cursor.execute("""INSERT OR IGNORE INTO users (user_id) VALUES (?)""",
                                           [user_id])

    async def wiev_user_id(self, user_id):
        with self.connect:
            return self.cursor.execute("""SELECT user_id FROM users WHERE user_id=(?)""",
                                           [user_id]).fetchall()

    async def wiev_admin(self, user_id):
        with self.connect:
            return self.cursor.execute("""SELECT admin FROM users WHERE user_id=(?)""",
                                           [user_id]).fetchall()

    async def wiev_user_class(self, user_id):
        with self.connect:
            return self.cursor.execute("""SELECT class FROM users WHERE user_id=(?)""",
                                           [user_id]).fetchall()

    async def add_class(self, classes, user_id):
        with self.connect:
            return self.cursor.execute("""UPDATE users SET class=(?) WHERE user_id=(?)""",
                                       [classes, user_id])

    async def wiev_classes(self):
        with self.connect:
            return self.cursor.execute("""SELECT class FROM class""").fetchall()

    async def wiev_rasspisanie_y0(self, clas):
        with self.connect:
            return self.cursor.execute("""SELECT pn FROM class WHERE class=(?)""", [clas])\
                .fetchall()
    async def wiev_rasspisanie_y1(self, clas):
        with self.connect:
            return self.cursor.execute("""SELECT vt FROM class WHERE class=(?)""", [clas])\
                .fetchall()
    async def wiev_rasspisanie_y2(self, clas):
        with self.connect:
            return self.cursor.execute("""SELECT sr FROM class WHERE class=(?)""", [clas])\
                .fetchall()
    async def wiev_rasspisanie_y3(self, clas):
        with self.connect:
            return self.cursor.execute("""SELECT cht FROM class WHERE class=(?)""", [clas])\
                .fetchall()
    async def wiev_rasspisanie_y4(self, clas):
        with self.connect:
            return self.cursor.execute("""SELECT pt FROM class WHERE class=(?)""", [clas])\
                .fetchall()


    async def wiev_rasspisanie_z_vse(self):
        with self.connect:
            return self.cursor.execute("""SELECT * FROM rass WHERE id=1 """)\
                .fetchall()

    async def wiev_rasspisanie_z_pn(self):
        with self.connect:
            return self.cursor.execute("""SELECT * FROM rass WHERE id=0""")\
                .fetchall()

    async def wiev_homework(self, user_id):
        with self.connect:
            return self.cursor.execute("""SELECT homework FROM users WHERE user_id=(?)""", [user_id]).fetchall()

    async def add_homework(self, homework, clas):
        with self.connect:
            return self.cursor.execute("""UPDATE users SET homework=(?) WHERE class=(?) """, [homework, clas])\
                .fetchall()

    async def update_label(self, label, user_id):
        with self.connect:
            return self.cursor.execute("""UPDATE users SET label=(?) WHERE user_id=(?)""",
                                       [label, user_id])

    async def get_payment_status(self, user_id):
        with self.connect:
            return self.cursor.execute("""SELECT bought, label FROM users WHERE user_id=(?)""",
                                       [user_id]).fetchall()

    async def update_payment_status(self, user_id):
        with self.connect:
            return self.cursor.execute("""UPDATE users SET bought=(?) WHERE user_id=(?)""",
                                       [True, user_id])

    async def unupdate_payment_status(self, user_id):
        with self.connect:
            return self.cursor.execute("""UPDATE users SET bought=(?) WHERE user_id=(?)""", [False, user_id])