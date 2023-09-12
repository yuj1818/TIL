from django.shortcuts import render

age = range(25,31)
grade = ['a','b','c','s']

# Create your views here.
def certification1(request):
    context = {
        'name': 'student1',
        'age': age,
        'grade': grade
    }
    return render(request, 'certifications/certification1.html', context)

def certification2(request):
    context = {
        'name': 'student2',
        'age': age,
        'grade': grade
    }
    return render(request, 'certifications/certification2.html', context)

def certification3(request):
    context = {
        'name': 'student3',
        'age': age,
        'grade': grade
    }
    return render(request, 'certifications/certification3.html', context)