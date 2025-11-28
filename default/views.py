from django.shortcuts import render
from .models import poll,option
from django.views.generic import ListView, DetailView,RedirectView

# Create your views here.
def poll_list(req):#接收django 傳給你的使用者請求 名稱(req)
    polls = poll.objects.all()#poll的所有東西回傳，收在polls
    return render(req, "default/list.html", {'poll_list' : polls,'msg':'Hello!'})
    #回報 繪製(運算) (參數,位置,{可用變數:變數(名稱可不同),msg})，字典 對應關係

class PollList(ListView):
    model = poll
    #通用去改(不用字典)
    #應用程式名稱/資料模型_list.html
    #default/poll_list.html
    #預設名稱 葉面範本黨名

class PollView(DetailView):
    model = poll
    #default/poll_detail.html

    def get_context_data(self, **kwargs):
                        #自己,關鍵藏數
        ctx = super().get_context_data(**kwargs)#字典(detailview 原本要傳的)
        ctx['option_list'] = option.objects.filter(poll_id = self.object.id)
        return ctx
    
class PollVote(RedirectView):
                #會跳轉回來的
    #model = poll
    pass