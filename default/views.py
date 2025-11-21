from django.shortcuts import render
from models import poll

# Create your views here.
def poll_list(req):#接收django 傳給你的使用者請求 名稱(req)
    polls = poll.objects.all()
    return render(req, "default/list.html", {'poll_list' : polls,'msg':'Hello!'})
    #回報 繪製(運算) (參數,位置,{可用變數:變數(名稱可不同),msg})