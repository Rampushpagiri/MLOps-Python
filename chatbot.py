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
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
meet = chatbot()