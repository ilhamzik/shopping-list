from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Muhammad Ilham Zikri',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
# Create your views here.
