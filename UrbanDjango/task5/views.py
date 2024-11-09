from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.
def sign_up_by_html(request):
    users = ["user1", "user2", "user3"]
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if password == repeat_password and username not in users and int(age) >= 18:
            return f"Приветствуем, {username}!"
        else:
            info['error'] = "Некорректные данные"

        print(f'Username: {username}')
        print(f'Password: {password}')
        print(f'Password again: {repeat_password}')
        print(f'Age: {age}')
        return HttpResponse('Форма успешно отправлена')

    return render(request, 'fifth_task/registration_page.html', context=info)


def sign_up_by_django(request):
    users = ["user1", "user2", "user3"]
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and username not in users:
                return f"Приветствуем, {username}!"
            else:
                info['error'] = "Некорректные данные"
    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', context=info)

