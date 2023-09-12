from django.shortcuts import render
import random

# Create your views here.
def first(request):
    msg = request.GET.get('msg')
    context = {
        'msg': msg
    }
    return render(request, 'throw_loops/first.html', context)

def second(request):
    msg = request.GET.get('msg')
    context = {
        'msg': msg  
    }
    return render(request, 'throw_loops/second.html', context)

def third(request):
    msg1 = request.GET.get('msg1')
    msg2 = request.GET.get('msg2')
    context = {
        'msg': random.choice([msg1, msg2])
    }
    return render(request, 'throw_loops/third.html', context)