from django.urls import path
from .views import poll_list, PollList, PollView, PollVote

urlpatterns = [
  path("", poll_list),#專案的處理規則都要列在專案中(poll/urls)
  path("list", PollList.as_view(), name = 'poll_list'),
  #路徑可以埋參數，統一在同一條路徑
  path("<int:pk>/", PollView.as_view(), name = 'poll_view'),
  #如果是整數，擷取，撈參數
  #poll_list中的{% url 'poll_view' poll.id %}方便更改<int:pk>/
  path('<int:oid>/vote/', PollVote.as_view(), name = 'poll_vote'),
  #'<int:自選名稱>/vote/'
  #name參數，來命名
]