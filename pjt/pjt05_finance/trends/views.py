from django.shortcuts import render, redirect
from .forms import KeywordForm
from .models import Keyword, Trend
from bs4 import BeautifulSoup
from selenium import webdriver
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64

plt.switch_backend('Agg')

def keyword(request):
    if request.method == 'POST':
        keyword_form = KeywordForm(request.POST)
        if keyword_form.is_valid():
            keyword_form.save()
            return redirect('trends:keyword')
    else:
        keyword_form = KeywordForm()
        keywords = Keyword.objects.all()
        context = {
            'keyword_form': keyword_form,
            'keywords': keywords,
        }
        return render(request, 'trends/keyword.html', context)

def keyword_detail(request, pk):
    keyword = Keyword.objects.get(pk=pk)
    keyword.delete()
    return redirect('trends:keyword')

def crawling(request):
    keywords = Keyword.objects.values_list('id', 'name')
    for id, keyword in keywords:
        url = f'https://www.google.com/search?q={keyword}'
        driver = webdriver.Chrome()
        driver.get(url)

        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')

        result_stats = soup.select_one('div#result-stats')
        result = ''
        for c in result_stats.text:
            if c == '개':
                break
            if c.isdigit():
                result += c

        if Trend.objects.filter(name=id, search_period='all'):
            trend = Trend.objects.get(name=id, search_period='all')
            trend.result = int(result)
            trend.save()
        else:
            trend = Trend()
            trend.name = Keyword.objects.get(pk=id)
            trend.result = int(result)
            trend.search_period = 'all'
            trend.save()
    trends = Trend.objects.filter(search_period='all')
    context = {
        'trends': trends,
    }
    return render(request, 'trends/crawling.html', context)

def crawling_histogram(request):
    trends = Trend.objects.filter(search_period='all')
    keywords = []
    results = []
    for trend in trends:
        keywords.append(trend.name.name)
        results.append(trend.result)

    plt.clf()

    x = np.arange(len(trends))
    plt.bar(x, results, color='C0')
    plt.xticks(x, keywords)
    plt.xticks(rotation=45)
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.legend(['Trends'], loc='upper right')
    plt.title('Technology Trend Analysis')
    plt.grid(True)
    
    buffer = BytesIO()

    plt.savefig(buffer, format='png')

    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')

    buffer.close()

    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }

    return render(request, 'trends/crawling_histogram.html', context)


def crawling_advanced(request):
    keywords = Keyword.objects.all()
    for keyword in keywords:
        url = f'https://www.google.com/search?q={keyword.name}&tbs=qdr:y'
        driver = webdriver.Chrome()
        driver.get(url)

        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')

        result_stats = soup.select_one('div#result-stats')
        result = ''
        for c in result_stats.text:
            if c == '개':
                break
            if c.isdigit():
                result += c

        if Trend.objects.filter(name=keyword.id, search_period='year'):
            trend = Trend.objects.get(name=keyword.id, search_period='year')
            trend.result = int(result)
            trend.save()
        else:
            trend = Trend()
            trend.name = Keyword.objects.get(pk=keyword.id)
            trend.result = int(result)
            trend.search_period = 'year'
            trend.save()

    trends = Trend.objects.filter(search_period='year')
    keywords = []
    results = []
    for trend in trends:
        keywords.append(trend.name.name)
        results.append(trend.result)

    plt.clf()

    x = np.arange(len(trends))
    plt.bar(x, results, color='C0')
    plt.xticks(x, keywords)
    plt.xticks(rotation=45)
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.legend(['Trends'], loc='upper right')
    plt.title('Technology Trend Analysis')
    plt.grid(True)
    
    buffer = BytesIO()

    plt.savefig(buffer, format='png')

    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')

    buffer.close()

    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }

    return render(request, 'trends/crawling_advanced.html', context)