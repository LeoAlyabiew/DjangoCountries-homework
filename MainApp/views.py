from django.shortcuts import render, HttpResponse

def home(request):
    result = """
    <h1 style="color:#34495E;
        font-size:50px">DjangoCountries</h1>
    
    <h2 style="color:#85929E;
        font-size:30px;font-family:Arial">Приветствие</h2>
    """
    return HttpResponse(result)
