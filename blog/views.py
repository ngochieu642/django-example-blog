from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author": "hieu thai",
        "title": "blog post 1",
        "content": "hello world",
        "date_posted": "Dec 2019",
    },
    {
        "author": "Khoa Dam",
        "title": "blog post 2",
        "content": "hello react",
        "date_posted": "Jan 2020",
    },
]


def home(request):
    context = {
        'posts':posts
    }
    return render(request, "blog/home.html", context=context)


def about(request):
    return render(request, "blog/about.html", context={'title':'About'})

