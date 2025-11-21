from django.urls import path
from views import poll_list

urlpatterns = [
  path("", poll_list),#專案的處理規則都要列在專案中(poll/urls)

]