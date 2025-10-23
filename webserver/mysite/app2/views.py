from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_app2(request):
    html = """
    <html>
        <head>
            <title>Hello</title>
        </head>
        <body>
            <h1>Hello from app2</h1>
        </body>
    </html>
    """
    return HttpResponse(html)
