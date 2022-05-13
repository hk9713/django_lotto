from django.contrib import admin
from .models import GuessNumbers  # 같은 폴더일경우 .으로 써도 됨 / 아니면 lotto.models 이렇게 작성

# Register your models here.
admin.site.register(GuessNumbers)
