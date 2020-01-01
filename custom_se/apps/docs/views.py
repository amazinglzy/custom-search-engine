from django.shortcuts import render

# Create your views here.


def docs_view(req):
    return render(req, 'index.html')