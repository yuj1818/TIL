from django.shortcuts import render

# Create your views here.
def calculator(request, num1, num2):
    results = [
        num1 * num2,
        num1 - num2,
        num1 / num2 if num2 else None
    ]
    operators = ['*', '-', '/']
    context = {
        'num1': num1,
        'num2': num2,
        'results': zip(results, operators)
    }
    return render(request, 'calculators/calculator.html', context)