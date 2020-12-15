from django.shortcuts import render
from .models import feed

# Create your views here.

def ck(request):
    f=feed()
    dict = {'feed': f}
    return render(request, 'feedback/fdk.html',dict)

def gvfdk(request):
    f=feed()
    f.c_id = request.POST['c_id']
    f.feedbacks = request.POST['feedbacks']
    f.save(using="feedback")
    
    return render(request, 'feedback/tnx.html')
