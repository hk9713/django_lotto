from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm

# Create your views here.
def index(request):

    lottos = GuessNumbers.objects.all()

    # {"lottos":lottos} <- context
    return render(request, 'lotto/default.html', {"lottos":lottos})


def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")


def post(request):

    if request.method == 'POST':

        form = PostForm(request.POST) # 채워진 양식을 만듦
        if form.is_valid():
            lotto = form.save(commit=False) # 후처리를 하기 위해
            lotto.generate()
            return redirect('index') # index url로 이동

        # 이런 방법도 있음
        # user_name = request.POST['name']
        # user_text = request.POST['text']
        # row = GuessNumbers(name=user_name, text=user_text)
        # row.generate() # self.save() 가 있어서 db 저장됨!

    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {"form":form})


def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk=lottokey)  # pk자리에 id써도 똑같음
    return render(request, "lotto/detail.html", {"lotto":lotto})
