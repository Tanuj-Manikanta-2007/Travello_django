from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
  return  render(request,'Home.html',{'name' : 'Tanuj'})

def add(request):
    if request.method == "POST":
        val1 = request.POST.get('num1')
        val2 = request.POST.get('num2')

        

        res = int(val1) + int(val2)
        return render(request, 'result.html', {'result': res})

    return HttpResponse("Use POST only.")
