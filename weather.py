from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Weather")
root.geometry("700x50")
root.configure(background="yellow")
#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=F5D2E0FA-D21C-4676-B111-30F7EFAAF17B



try:
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=F5D2E0FA-D21C-4676-B111-30F7EFAAF17B")
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category =  api[0]['Category']['Name']
except Exception as e:
    api= "Error..."

myLabel = Label(root, text = city + " Air Quality " + str(quality) + " " + category, font=("TimesNewRoman", 20), background ="yellow")
myLabel.pack()

root.mainloop()
