from django.shortcuts import render


# Website views here.
def home(request):
    return render(request, 'website/index.html')


# Workarea views here.
def workarea(request):
    return render(request, 'workarea/index.html', {

    })

