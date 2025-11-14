class chatbot:
    def __init__(self):
        self.username = ''
        self.pwd = ''
        self.lgdin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcme t chatbt !! hw wld like t prceed?
                            1. press 1 t signup
                            2. press 2 t signin
                            3. press 3 t write a pst
                            4. press 4 t msg a friend
                            5. press any ther key t exit""")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
#meet = chatbot()
    def signup(self):
        email = input("enter yur email here ->")
        passwd = input("setup ypur passwrd ->")
        self.username = email
        self.pwd = passwd
        print("yu have singedup succesfully")
        print("\n")
        self.menu()
    def signin(self):
        if self.username=='' and self.pwd=='':
            print("please signup fiest by pressing 1 in the main menu")
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
meet = chatbot()
