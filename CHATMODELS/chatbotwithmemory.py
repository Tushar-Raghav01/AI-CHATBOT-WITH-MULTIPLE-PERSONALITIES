#---------------------ye abhi history ko use toh kr rhaa h pr abhi messgaes mei
#--------------------drawback h bhot sare storage limit h, token excced h etc 



# from dotenv import load_dotenv
# from langchain_mistralai import ChatMistralAI
# import sys

# load_dotenv()

# model = ChatMistralAI(model="mistral-small-2506")
# # history yad rkhen ke liye ek memory bna rhe h
# messages=[]


# #emojis ko handle krne ke liye h
# sys.stdout.reconfigure(encoding="utf-8")

# print("------------------Welcome to our chatgpt-----------------")
# print("------------------Type 0 to end the convo-----------------")

# while True:
#     prompt=input("You: ")
#     messages.append(prompt)
#     if prompt =="0" :
#         break
#     response = model.invoke(messages)
#     messages.append(response.content)
#     print("Bot: "+response.content)

# print(messages)    

# ------------------ab humne ek library ka use kra h 
# -----------ai mesage ko alga human ko alag or sysytem ko bs ek hi bar dena h notes dekhi----
# -----------isme system memory fix kr di h ----

# from dotenv import load_dotenv
# from langchain_mistralai import ChatMistralAI
# from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
# import sys


# load_dotenv()

# model = ChatMistralAI(model="mistral-small-2506",temperature=0.9)

# # history yad rkhen ke liye ek memory bna rhe h
# messages=[
#     SystemMessage(content="you are a chatbot")
# ]

# #emojis ko handle krne ke liye h
# sys.stdout.reconfigure(encoding="utf-8")

# print("------------------Welcome to our chatgpt-----------------")
# print("------------------Type 0 to end the convo-----------------")

# while True:
#     prompt=input("You: ")
#     messages.append(HumanMessage(content=prompt))
#     if prompt =="0" :
#         break
#     response = model.invoke(messages)
#     messages.append(AIMessage(content=response.content))
#     print("Bot: "+response.content)

# print(messages)    



# -----------isme system memory fix nhi kri h mode choose kr skte h  ----

from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
import sys


load_dotenv()

model = ChatMistralAI(model="mistral-small-2506",temperature=0.9)

print("-------- you can choose your mode-------------")
print("chooose 1 for ai teacher")
print("chooose 2 for friend")
print("chooose 3 for angry person")
print("chooose 4 for sad person")


mode=""
choose=int(input("enter your number: "))
if choose==1:
    mode="you are an  ai teacher "
elif choose==2:
    mode="you are an  friend "
elif choose==3:
    mode="you are an  angry person "
elif choose==4:
    mode="you are an  sad person "

# history yad rkhen ke liye ek memory bna rhe h
messages=[
    SystemMessage(content=mode)
]

#emojis ko handle krne ke liye h
sys.stdout.reconfigure(encoding="utf-8")

print("------------------Welcome to our chatgpt-----------------")
print("------------------Type 0 to end the convo-----------------")

while True:
    prompt=input("You: ")
    messages.append(HumanMessage(content=prompt))
    if prompt =="0" :
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot: "+response.content)


#-----------hum yha pr ab streamlit ka use krke ek basic chatbot bna skte h
