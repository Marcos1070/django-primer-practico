from django.shortcuts import render

def inicio_blog(request):
    return render(request, 'blog/index.html')