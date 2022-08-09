from django.shortcuts import render
import requests
API_KEY = 'fdf27bc7aebb4bd7a6d274af5bc2ab08'

def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    context = {
        'articles': articles
    }
    return render(request, 'home.html', context)
