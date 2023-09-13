from django.shortcuts import render

# Create your views here.
product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}

def price(request, thing, cnt):
    context = {
        'thing': thing,
        'cnt': cnt,
        'total_price': product_price[thing] * cnt if thing in product_price.keys() else None
    }
    return render(request, 'prices/price.html', context)