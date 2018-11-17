from django.shortcuts import render
from .models import Question
# Create your views here.

def forum(request):
    #post = post.objects.all()
    #dic = {'post': Question.objects.all() }
    return render(request,"forum/forum.html",{'post': Question.objects.all()})
