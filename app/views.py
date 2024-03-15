from django.shortcuts import render

# Create your views here.
def cond(request):
    d={'a':400,'b':300,'c':300}
    return render(request,'cond.html',context=d)
