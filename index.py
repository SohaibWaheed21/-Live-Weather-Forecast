from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
#this listTrainer forms a list that contains the best possible respones
from flask import Flask, render_template, request
import requests


#to use chatterbotcorpus following must be downloaded
# chatterbot 
# chatterbot-corpus
# pyyaml
# spacy    #python -m spacy download en
# jupyter
# notebook
# pint


app = Flask(__name__)

bot = ChatBot("chatbot",read_only=False, 
              logic_adapters=[
                {  
                  "import_path":"chatterbot.logic.BestMatch",
                   "default_response":"Sorry I don't have an answer",
                  "maximum_similarity_threshold": 0.9 
                  #it's gonna searcg for an answer with 90% similarity, if not found it will return default answer
                }

                ]) 
#first is the name of the chatterbot, second is what allows the chater bot to learn from our responses when true it does not learn

#calmandcode.com
list_to_train = [
                "hi",
                "hi there",
                "what courses do you have?",
                "please visit this link for more info https://CalmAndCode.com/go/unlimited",
                "What is your contact page?",
                "head on over to https://CalmAndCode.com/contact"                 

] 

# list_to_train2 = [
#                 "hi",
#                 "hi mate!",
#                 "What's your name?",
#                 "I'm a your assistant, the name is Chatbot",
#                 "How old are you?",
#                 "I'm 30 years old",
#                 "why are you so mad?",
#                 "Because of You!",
#                 "Do you have iPhone?",
#                 "Ofcourse I do",
#                 "What's your favorite food?",
#                 "Pizza",
#                 "What's your job?",
#                  "I'm an assistant",
#                 "I don't know what you're talking about"                     

# ] 


# list_trainer = ListTrainer(bot)

# list_trainer.train(list_to_train)
# list_trainer.train(list_to_train2)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

@app.route("/")
def main():
    try:
        return render_template("index.html")
        #return "Hello World! (Flask is working)"
    except Exception as e:
        print("🔥 ERROR:", e)  # Check terminal for this error
        return str(e)  # Display error in browser
        



# while True:
#     user_response= input("User: ")

#     print("Chatbot: " + str(bot.get_response(user_response)) )


@app.route("/get")
def get_chatbot_response():
    userText = request.args.get('userMessage')
    raw_data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+userText+"&appid=bbc89cdfd9370ef7032feefc6a46e4f2")
    result = raw_data.json()
    return result
    #return str(bot.get_response(userText))

if __name__ == "__main__":
    app.run(debug=True)