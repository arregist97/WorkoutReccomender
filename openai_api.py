import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def create_workout(name, date_of_birth, sex, height, weight):
    prompt = """My name is {}. I want to start working out. Here is some information about me:
date of birth: {}
sex: {}
height: {}cm
weigth: {}kg

Give me a workout routine for me to start getting in shape.""".format(
        name.capitalize(),
        date_of_birth,
        sex,
        height,
        weight,
    )
    workout = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6,
        )
    return workout