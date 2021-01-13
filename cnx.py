import pymysql

# connection      user/database =nodejslogin1	password =Yf3d6_1GW5e!


class DataBase:
    def __init__(self):
        try:
            self.connection = pymysql.connect(
            host='den1.mysql4.gear.host',
            user='nodejslogin1',
            password='Yf3d6_1GW5e!',
            db='nodejslogin1'

        )

            self.cursor = self.connection.cursor()
            print("great! 🍻")       
        except Exception as e:
            print(f"error on connect 😱 {e}")
        

    def get_user(self, email,password):
        self.email = email
        self.password = password
        try:
            self.cursor.execute(" call getuser('{}','{}') ".format(self.email,self.password))
            reg = self.cursor.fetchall()
            # return print(reg)
        
            # for data in reg:
        
            if self.email=="" or self.password == "":
                wrong= {
                    "status":400,
                    "description":"user or password missing or wrong"
                }
                return  wrong
            elif len(reg)==0:

                wrong= {
                    "status":400,
                    "description":"user doesn't exist"
                }
                return  wrong

            else:

                for data in reg:
                    first_name = data[0]
                    last_name = data[1]
                    password = data[2]
                    email = data[3]
                    created = data[4]
                res = {
                    "status":200,
                    "first_name":first_name,
                    "last_name":last_name,
                    "password":str(password).format('utf-8'),
                    "email" : email,
                    "created": created
                }
                return  res

        except Exception as e:
            error = {
                "status":404,
                "description":f"Function error {e}"
            }
            return error

    def user_register(self, first_name,last_name,email,password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

        try:

            self.cursor.execute(" call userinsert('{}','{}','{}','{}') ".format(self.first_name,self.last_name,self.email,self.password))
            self.connection.commit()
            
            res = {
                "status":200,
                "description":f"User: {self.first_name} with email: {self.email} are inserted."
            }
            return res
        except Exception as e:
            error = {
                "status":404,
                "description":f"Function error {e}"
            }
            return error
    
    def close(self):
        self.connection.close()


    