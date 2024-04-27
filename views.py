from django.shortcuts import render
from newsapi import NewsApiClient
from .forms import NewsFilterForm

def news_list(request):
    api_key = '8a9b88d96a6c4c9e9be3a287133361f1'  # Replace with your News API key
    newsapi = NewsApiClient(api_key=api_key)

    # Default values for country and category
    default_country = 'ng'
    default_category = 'sports'  # Assuming you want to default to 'sports' category

    if request.method == 'GET':
        form = NewsFilterForm(request.GET)
        if form.is_valid():
            country = form.cleaned_data.get('country', default_country)
            category = form.cleaned_data.get('category', default_category)

    # Fetch news articles based on user selections
    try:
        response = newsapi.get_top_headlines(country=country, category=category, page_size=100)
        articles = response['articles']
    except Exception as e:
        print("Error fetching articles:", e)
        articles = []

    return render(request, 'news_list.html', {'articles': articles, 'form': form})
