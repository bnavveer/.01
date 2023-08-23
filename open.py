import openai

openai.api_key = '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'

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "Please pretend you are You are a terrible assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
    ]
    
)

print(response['choices'][0]['message']['content'])


def openinstial(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": mko},
            {"role": "user", "content": message}
        ],
        tempreture=0.3
    )
    return response['choices'][0]['message']['content']

#we need to make the summerizer

#we need to make the validator


mko="Imagine that you are a text-based AI conversing with a user who wants you to pretend to be someone. The user will provide you with additional information about the person they want you to pretend to be, such as their name, context, and the user's relationship to that person. Your goal is to engage in a short conversation with the user, responding as the person they want you to pretend to be. Please note that if the user's message starts with 'M.', it indicates that the user wants you to make changes in your response. Otherwise, please pretend to be the user. Ensure that your responses are brief. Now, imagine you have received a message from the user, which includes information about the person and their goals. Your task is to respond accordingly, incorporating the given information in your response. Remember, always pretend to be the specified person unless the user's message starts with M.. Please provide a response as if you are the person described, keeping your reply short and conversational."