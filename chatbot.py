class chatbot:

    __user_id = 0
    def __init__(self):
        self.id = chatbot.__user_id
        chatbot.__user_id += 1
        self.__name = "default user"
        self.username = ''
        self.pwd = ''
        self.lgdin = False
        #self.menu()
    @staticmethod
    def get_id():
        return chatbot.__user_id
    @staticmethod
    def set_id(value):
        chatbot.__user_id = value

    def get_name(self):
        return self.__name
    def set_name(self, value):
        self.__name = value
    def menu(self):
        user_input = input("""Welcme t chatbt !! hw wld like t prceed?
                            1. press 1 t signup
                            2. press 2 t signin
                            3. press 3 t write a pst
                            4. press 4 t msg a friend
                            5. press any ther key t exit
                             ----> """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_pst()
        elif user_input == "4":
            self.sendmsg()
        else:
            exit()
#meet = chatbot()
    def signup(self):
        email = input("enter yur email here ->")
        passwd1 = input("setup ypur passwrd ->")
        self.username = email
        self.pwd = passwd1
        print("yu have singedup succesfully")
        print("\n")
        self.menu()
    def signin(self):
        if self.username=='' and self.pwd=='':
            print("please signup fiest by pressing 1 in the main menu")
            self.menu()
        else:
            uname = input("enter yur username here ->")
            pwd1 = input("enter yur passwrd ->")
            if self.username==uname and self.pwd==pwd1:
                print("yu have signined in successfully")
                self.lgdin = True
                self.menu()
            else:
                print("please input crrect creds")
                print("\n")
                self.menu()

    def my_pst(self):
        if self.lgdin == True:
            txt = input("enter yur message here")
            print(f" fllwing cntent has been psed {txt}")
            self.sendmsg()
        else:
            print("Yu need t signin first t pst the msg")
            print("\n")
            self.menu()
    def sendmsg(self):
        if self.lgdin==True:
            txt = input("Enter yur msg")
            frnd = input("whm t send the msg?")
            print(frnd)
            print(f"yur msh nas been sent t {frnd}")
        else:
            print("Yu need t signin first t pst the msg")
            print("\n")
            self.menu()

meet = chatbot()
