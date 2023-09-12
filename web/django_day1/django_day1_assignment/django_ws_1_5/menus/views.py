from django.shortcuts import render
# Create your views here.
foods = ["피자","치킨","국밥","초밥", "민초흑당로제마라탕"]
drinks = ["cider","coke","miranda","fanta", "eye of finetree"]
def food(request):
    context=  {
        'food': foods
    }
    return render(request, 'menus/food.html', context)

def drink(request):
    context = {
        'drink': drinks
    }
    return render(request, 'menus/drink.html', context)

def receipt(request):
    menu = request.GET.get('selected_menu')
    context = {
        'menu_list': foods + drinks,
        'menu': menu
    }
    return render(request, 'menus/receipt.html', context)