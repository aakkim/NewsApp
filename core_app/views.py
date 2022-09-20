from django.shortcuts import render
import requests
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()

def home(request):
    configure()
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={os.getenv('API_KEY')}"
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f"https://newsapi.org/v2/top-headlines?category={category}&apiKey={os.getenv('API_KEY')}"
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    context = {
        'articles': articles
    }
    return render(request, 'home.html', context)
