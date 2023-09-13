from django.shortcuts import render

# Create your views here.
def first(request):
    msg = request.GET.get('msg')
    context = {
        'message': msg
    }
    return render(request, 'throw_catch/first.html', context)

def second(request):
    msg = request.GET.get('msg')
    context = {
        'message': msg
    }
    return render(request, 'throw_catch/second.html', context)
