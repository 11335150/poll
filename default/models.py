from django.db import models

# Create your models here.
class poll(models.Model): #poll為名稱;models.model借已有來擴充
    subject = models.CharField("投票主題",max_length=64)#單行文字形欄位;("標籤文字",max_length=最多文字數)
    desc = models.TextField("說明")#多行文字欄位
    created = models.DateField("建立日期",auto_now_add=True)

    #設定將subject直接作為顯示之名稱
    def __str__(self): #這個類跌(class)的方法
        return self.subject#顯示什麼

class option(models.Model):
    titles = models.CharField("選項文字",max_length=64)
    votes = models.IntegerField("票數",default = 0)
    poll_id = models.IntegerField("投票主題編號")#讓兩個class相連，配合投票主題
    #他會給編號 從1開始

    def __str__(self): 
        return "{}-{}".format(self.poll_id,self.titles) #顯示什麼
        