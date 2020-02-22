from django.shortcuts import render
from django.http import HttpResponse
from .models import Message
from .forms import PostForm

# Create your views here.

def index(request):
    data = Message.objects.all()
    params = {
        'title': 'Hello',
        'message': 'ここにコメントを打ってください',
        'data': data,
         }
    return render(request, 'hello/index.html', params)


def create(request):
    params = {
        'form': 'PostForm()'
    }
    if  (request.method == 'POST'):
        comment = request.POST['content']
        message = Message(comment = comment)
        message.save()
    return render(request, 'hello/index.html', params)

