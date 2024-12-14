from django.shortcuts import render
from django.http import HttpResponse
from .forms import QueryForm

def index(request):
    return render(request, "core/landing_page.html")

def contact(request):
    if request.method == "POST":
        form = QueryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
    else:
        form = QueryForm()
    return render(request, "core/index.html", {
        "form": form
    })
