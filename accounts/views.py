from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

# Create your views here.
from django.template import RequestContext

from accounts.forms import UserForm


def signup(request):
    if request.method == 'POST':
        # 회원가입에 필요한 코드 작성
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/todo/list')
    else:
        # 회원가입 폼을 응답한다.
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})
