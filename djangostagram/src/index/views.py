from django.shortcuts import redirect, render

# Default URL Mapping
def index(request):
    return render(request, 'base.html')