from django.shortcuts import render, redirect
import requests
import uuid
from .voice import listen_voice, speak

##    api_key = "c4c2829891234580814235307262903"
def chatbot(request):

    chats = request.session.get('chats', {})

    chat_id = request.GET.get('chat')

    if not chat_id:
        chat_id = str(uuid.uuid4())
        chats[chat_id] = []

    chat_history = chats.get(chat_id, [])

    if request.method == "POST":

        user_message = request.POST.get("message")

        # Weather detection
        if "weather" in user_message.lower():

            city = user_message.lower().replace("weather", "").strip()

            if not city:
                city = "Ahmedabad"

            bot_response = get_weather(city)

        else:

            try:
                prompt = f"""
You are Smart Krishi Mitra AI.

User Question:
{user_message}
"""

                response = requests.post(
                    "http://127.0.0.1:11434/api/generate",
                    json={
                        "model": "phi3",
                        "prompt": prompt,
                        "stream": False
                    },
                    timeout=60
                )

                bot_response = response.json().get("response", "No response")

            except Exception as e:
                bot_response = f"Error: {str(e)}"

        chat_history.append({
            "user": user_message,
            "bot": bot_response
        })

        chats[chat_id] = chat_history
        request.session['chats'] = chats

        return redirect(f"/chatbot/?chat={chat_id}")

    return render(request, "chatbot/chatbot.html", {
        "chat_history": chat_history,
        "chats": chats,
        "current_chat": chat_id
    })

def get_weather(city):

    api_key = "c4c2829891234580814235307262903"

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(url)
    data = response.json()

    if "current" in data:
        temp = data["current"]["temp_c"]
        desc = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]

        return f"""
🌦 Weather in {city}

🌡 Temperature: {temp}°C
☁ Condition: {desc}
💧 Humidity: {humidity}%
"""

    return "Weather not found"

# Voice Assistant
def voice_assistant(request):

    text = listen_voice()

    reply = "आप यूरिया और डीएपी का उपयोग करें"

    speak(reply)

    return render(request, "chatbot/chatbot.html", {
        'text': text,
        'reply': reply
    })