import json
with open("C:\\coding\\Python lab\\nayi.json") as f:
    data=json.load(f)

current_temp=data['main']['temp']
humidity=data['main']['humidity']
weather_desc=data['weather']['desc']

print(f"Current temperature: {current_temp} celsius")
print(f"Humidity:{humidity}%")
print(f"Weather description: {weather_desc}")