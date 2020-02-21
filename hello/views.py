from django.shortcuts import render
from django.http import HttpResponse
from .models import Message
from .forms import PostForm

# Create your views here.

def index(request):
    params = {
        'title': 'Hello',
        'message': 'ここにコメントを打ってください',
        'form':PostForm(),
        'data':[],
         }
    if (request.method == 'POST'):
        comment=request.POST['content']
        item = Message.objects.all
        params['data'] = [item]
        params['form'] = PostForm(request.POST)
    else:
        params['data'] = Message.objects.all

    return render(request, 'hello/index.html', params)