from django.shortcuts import render, get_object_or_404, redirect
from .models import Post #model import 해주기
from django.utils import timezone

# Create your views here.

def home(request):
    #db에서 갖고오는 query set을 받을 변수 선언
    posts = Post.objects.all() #이게 query set,, 이걸 home.html에 보여주기 위해 dictionary 이용 .all()까지 있어야 객체들 모두 갖고온다 볼수있다. __str__에 해당하는게 보인다
    #객체 내부의 내용들을 모두갖고오는건 아니다
    return render(request, "home.html", {'posts' : posts})  #return값을 줌으로 써 queryset을 갖고오고, 출력가능

#detail page 연결해주기 urls.py에서 post_id로 넘겨줬어
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "detail.html", {'post':post})

def new(request):
    if request.method  == "POST":
        # 글을 저장하는 객체/공간 생성
        post = Post()
        post.author = request.user
        post.content = request.POST['content']

        if 'image' in request.FILES:
            post.image = request.FILES['image']
        
        post.pub_date = timezone.datetime.now()
        post.save()
        #post.save()를 하지 않으면 제대로 저장이 되지 않는다.
        return redirect('/detail/' + str(post.id))
        #render는 template을 보여주기 위해서 사용
        #redirect는 특정 url로 접속
    return render(request, "new.html")