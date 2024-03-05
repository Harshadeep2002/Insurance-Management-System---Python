from entity.User import User

class UserDAO(User):
    def __init__(self):
        super().__init__()

    def perform_user_actions(self):
        while True:
            print("(User 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")
            ch = int(input("Enter choice: "))
            if ch == 1:
                self.create_user_table()
            elif ch == 2:
                print(self.add_user())
            elif ch == 3:
                print(self.update_user())
            elif ch == 4:
                print(self.delete_user())
            elif ch == 5:
                self.select_user()
            elif ch == 0:
                break
            else:
                print("Enter Valid Choice")
    def create_user_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS User(
            userId INT PRIMARY KEY,
            userName VARCHAR(50),
            password VARCHAR(50) NOT NULL,
            role VARCHAR(50)
            )'''
            self.open()
            self.stmt.execute(create_str)
            self.close()
            print("User Table Created Successfully")
        except Exception as e:
            print(e)

    def add_user(self):
        try:
            self.open()
            self.userId = int(input("Enter user ID: "))
            self.userName = input("Enter UserName: ")
            self.password = input("Enter Password: ")
            self.role = input("Enter role: ")
            data = [(self.userId,self.userName,self.password,self.role)]
            insert_str = '''INSERT INTO User(userId,userName,password,role)
                            VALUES(%s,%s,%s,%s)'''
            self.stmt.executemany(insert_str,data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            print(e)

    def update_user(self):
        try:
            self.open()
            user_id = int(input("Enter userID to be updated: "))
            self.userName = input("Enter userName: ")
            self.password = input("Enter password: ")
            self.role = input("Enter new role: ")
            data = [(self.userName,self.password,self.role,user_id)]
            update_str = '''UPDATE User SET userName = %s, password = %s, role = %s
                            WHERE userId = %s'''
            self.stmt.executemany(update_str,data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            print(e)

    def delete_user(self):
        try:
            self.open()
            user_id = int(input("Enter user ID to be deleted: "))
            delete_str = f'''DELETE FROM User
                            WHERE userId = {user_id}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            print(e)

    def select_user(self):
        try:
            select_str = '''SELECT * FROM User'''
            self.open()
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            self.close()
            print("Records in Table")
            for i in records:
                print(i)
        except Exception as e:
            print(e)
