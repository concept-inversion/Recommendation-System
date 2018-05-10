from django.shortcuts import render

def recommend(request):
    return render(request, 'home.html', {'name': 'bindeep'})