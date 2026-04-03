import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

def govt_schemes(request):

    url = "https://www.india.gov.in/topics/agriculture"

    schemes = []

    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        links = soup.find_all("a")

        for link in links[:15]:
            title = link.text.strip()
            href = link.get("href")

            if title and href:
                schemes.append({
                    "name": title,
                    "link": href
                })

    except Exception as e:
        print(e)

    return render(request,"schemes.html",{"schemes":schemes})