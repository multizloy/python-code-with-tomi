from django.shortcuts import render
import json
import urllib.request

# Create your views here.


def index(request):
    if request.method == "POST":
        city = request.POST["city"]
        res = urllib.request.urlopen(
            "http://api.openweathermap.org/data/2.5/weather?q="
            + city
            + "&appid=c7ae91e5a77f41a63df87b45441f0dfb"
        ).read()
        jsonData = json.loads(res)
        data = {
            "countryCode": str(jsonData["sys"]["country"]),
            "coordinate": str(jsonData["coord"]["lon"])
            + " "
            + str(jsonData["coord"]["lat"]),
            "temperature": str(jsonData["main"]["temp"]) + "k",
            "pressure": str(jsonData["main"]["pressure"]),
            "humidity": str(jsonData["main"]["humidity"]),
        }
    else:
        city = ""
        data = {}

    return render(request, "base/index.html", {"city": city, "data": data})
