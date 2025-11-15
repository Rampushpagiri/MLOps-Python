#lst = [1,2,3]
# my_str = "mlps playlist"
# my_int = 155
# #print(type(my_int))
# lst.capitalize()
# my_str = my_str.capitalize()
# print(my_str)

from chatbot import chatbot

#user1 = chatbot()
# 
#call meth0d
user1 = chatbot()
print(user1.id)

#using static meth0d directly frm class rather than 0bject
chatbot.set_id(10)

user2 = chatbot()
print(user2.id)

user3 = chatbot()
print(user3.id)

# user3 = chatbot()
# print(user3.id)
#getter and setter meth0d


# print(user1.get_name())
# user1.set_name("agnt x")
# print(user1.get_name())
