from django.shortcuts import render
from .models import poll,option
from django.views.generic import ListView, DetailView,RedirectView
from django.urls import reverse
# Create your views here.

#處理函式
def poll_list(req):#接收django 傳給你的使用者請求 名稱(req)
    polls = poll.objects.all()#poll的所有東西回傳，收在polls
    return render(req, "default/list.html", {'poll_list' : polls,'msg':'Hello!'})
    #回報 繪製(運算) (參數,位置,{可用變數:變數(名稱可不同),msg})，字典 對應關係

class PollList(ListView):
    model = poll
    #從poll這個資料模型撈資料
    #通用去改(不用字典)
    #應用程式名稱/資料模型_list.html
    #所以跑到default/poll_list.html撈資料
    #預設名稱 葉面範本黨名
    #PollList 繼承 ListView

class PollView(DetailView):
    model = poll
    #default/poll_detail.html

    def get_context_data(self, **kwargs):
                        #自己,關鍵藏數
        ctx = super().get_context_data(**kwargs)#字典(detailview 原本要傳的)
        ctx['option_list'] = option.objects.filter(poll_id = self.object.id)
        #變數option_list會=option.object之中篩選完的資料(用filter來篩選==>當poll_id = self.object.id將這個資料保留，傳到葉面範本)
        return ctx #回傳
    
class PollVote(RedirectView):
                #會跳轉回來的
    #redirect_url = "網址" 故定網址

    def get_redirect_url(self, *args, **kwargs):
        options = option.objects.get(id = self.kwargs['oid'])
        #get:一筆資料;filter:多筆資料
        options.votes += 1
        options.save()
        return reverse('poll_view', args=[options.poll_id])