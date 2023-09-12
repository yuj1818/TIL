from django.shortcuts import render

# Create your views here.
def calculation(request):
    return render(request, 'calculators/calculation.html')

def result(request):
    num1 = int(request.GET.get('num1'))
    num2 = int(request.GET.get('num2'))
    results = [
        num1 - num2,
        num1 * num2,
        num1 / num2 if num2 != 0 else None
    ]
    operators = ['*', '-',  '/']
    context = {
        'num1': num1,
        'num2': num2,
        'results': zip(results, operators)
    }
    return render(request, 'calculators/result.html', context)