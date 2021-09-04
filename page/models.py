from django.db import models
# 유저 정보 import
from django.conf import settings

# Create your models here.
class Post(models.Model):
    # title = models.CharField(max_length = 20)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('publish')
    #이미지 업로드를 위한 필드 생성
    image = models.ImageField(upload_to='images/', blank = True)  #blank는 이미지가 없어서 db상에 문제가 없게하기 위함
    content = models.TextField()    #내용이 들어갈 공간이라 max같은건 필요 x

    def __str__(self): #여기서 말하는 self 는 post 객체겠지
        # return self.title
        return self.content[:20]


    def summary(self):
        return self.content[:100]