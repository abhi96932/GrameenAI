import requests
import json

# Load rural knowledge database
with open("database/rural_data.json", "r", encoding="utf-8") as f:
    rural_data = json.load(f)

# Load farmer advisory database
with open("database/farmer_advisory.json", "r", encoding="utf-8") as f:
    farmer_data = json.load(f)

# Conversation memory
conversation_history = ""

# System prompt
system_prompt = """
You are GrameenAI, an assistant designed to help rural communities.
Give simple and clear answers.
Explain things related to farming, education, health, and government schemes.
Use simple English.
"""


# Search rural knowledge database
def search_rural_data(query):

    query = query.lower()

    for key in rural_data:
        if key in query:
            return rural_data[key]

    return None


# Search farmer advisory database
def get_farmer_advice(query):

    query = query.lower()

    for crop in farmer_data:
        if crop in query:

            info = farmer_data[crop]

            response = f"{crop.capitalize()} farming information:\n"
            response += f"Season: {info['season']}\n"
            response += f"Sowing Time: {info['sowing_time']}\n"
            response += f"Soil: {info['soil']}\n"
            response += f"Irrigation: {info['irrigation']}\n"
            response += f"Fertilizer: {info['fertilizer']}\n"
            response += f"Harvest Time: {info['harvest_time']}"

            return response

    return None


# Main AI response function
def get_response(user_input):

    global conversation_history

    # Check farmer advisory first
    advice = get_farmer_advice(user_input)
    if advice:
        return advice

    # Check rural knowledge database
    rural_answer = search_rural_data(user_input)
    if rural_answer:
        return rural_answer

    # Add conversation memory
    conversation_history += f"\nUser: {user_input}\nAI:"

    prompt = system_prompt + conversation_history

    try:

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "tinyllama",
                "prompt": prompt,
                "stream": False,
                "options":{
                    "num_predict":120
                }
            }
        )

        result = response.json()["response"]

        conversation_history += result

        # Limit memory size
        conversation_history = conversation_history[-2000:]

        return result.strip()

    except:

        return "Sorry, I cannot think right now."