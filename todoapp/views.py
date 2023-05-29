from django.shortcuts import render, redirect
from todoapp.models import TodoItem, TodoUsers
from django.http import HttpResponse, JsonResponse
import os

def index(request):
    # if request.COOKIES.get("log_in") == True:
    #     adress = request.COOKIES.get("adress")
    #     password = request.COOKIES.get("password")
    #     items = [TodoItem.objects.get(mail = adress, password = password)]
    #     return render(request, 'index.html', {'items': items})
    # else:
    #     return render(request, 'log_in.html')
    # print(prof)
    # create_cookie(request, prof, "Hello World")

    # print(request.COOKIES[prof])
    # get_cookie(request, prof)
    key = 'mail'
    value = 'kopilovnik@gmail.com'
    # remove_localstorage(request, key)
    # save_localstorage(request, key, value)

    items = TodoItem.objects.all()
    return render(request, 'index.html', {'items': items})
    # return render(request, 'log_in.html')

def authentification(request):
    pass

def delete(request, item):
    try:
        TodoItem.objects.get(item_id = item)
    except TodoItem.DoesNotExist:
        return redirect('index')
    else:
        item_to_delete = TodoItem.objects.get(item_id = item)
        print(f"Удалено: {item_to_delete.item_id}")
        item_to_delete.delete()
        return redirect('index')

def add_item(request):
    # user = request.user
    if request.method == 'POST':
        text = request.POST['text']
        if text.strip():
            try:
                TodoItem.objects.get(item_id = text)
            except TodoItem.DoesNotExist:
                item = TodoItem(item_id = text, text = text)
                item.save()
                print(f"Добавлено: {request.POST['text']}") 
            else:
                for i in range(len(TodoItem.objects.all())):
                    try:
                        TodoItem.objects.get(item_id = text + str(i))
                    except TodoItem.DoesNotExist:
                        item = TodoItem(item_id = text + str(i), text = text)
                        item.save()
                        print(f"Добавлено: {request.POST['text']}") 
                        break

    return redirect('index')

def account(request):
    return render(request, 'account.html')

def exit_user(request):
    # return redirect('log_in')
    return redirect('account')

def add_user(request):
#     if request.method == 'POST':
#         adress = request.POST.get('adress')
#         password = request.POST.get('password')
#         try:
#             TodoUsers.objects.get(mail = adress)
#         except TodoUsers.DoesNotExist:
#             User = TodoUsers(mail = adress, password = password)
#             User.save()
        
#         create_cookie("log_in", True)
#         create_cookie("adress", adress)
#         create_cookie("password", password)

    return redirect('index')

def turn_On(request, item):
    try:
        TodoItem.objects.get(item_id = item)
    except TodoItem.DoesNotExist:
        return redirect('index')
    else:
        item_to_switch = TodoItem.objects.get(item_id = item)
        item_to_switch.completed = True
        item_to_switch.save()
        print(f'Выполнено "{item_to_switch.item_id}"')
        return redirect('index')

def turn_Off(request, item):
    try:
        TodoItem.objects.get(item_id = item)
    except TodoItem.DoesNotExist:
        return redirect('index')
    else:
        item_to_switch = TodoItem.objects.get(item_id = item)
        item_to_switch.completed = False
        item_to_switch.save()
        print(f'Ошибочка, не выполнено "{item_to_switch.item_id}"')
        return redirect('index')


def my_view(request):
    data = {'theme': 'auto'}
    return render(request, 'index.html', {'data': data})

def save_localstorage(request, key, value):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    localstorage_file_path = os.path.join(current_directory, 'static', 'js', 'save_localstorage.js')

    javascript_code = f'''localStorage.setItem('{key}', '{value}');\nconsole.log('{key}',': ', '{value}');'''

    with open(localstorage_file_path, 'w') as file:
        file.write(javascript_code)

    return HttpResponse('Data saved to LocalStorage.')

def get_localstorage(request, key, value):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    localstorage_file_path = os.path.join(current_directory, 'static', 'js', 'remove_localstorage.js')

    javascript_code = f'''return localStorage.getItem('{key}');'''

    with open(localstorage_file_path, 'w') as file:
        file.write(javascript_code)

    return HttpResponse('Data saved to LocalStorage.')

def remove_localstorage(request, key):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    localstorage_file_path = os.path.join(current_directory, 'static', 'js', 'remove_localstorage.js')

    javascript_code = f'''localStorage.removeItem('{key}');'''

    with open(localstorage_file_path, 'w') as file:
        file.write(javascript_code)

    return HttpResponse('Data saved to LocalStorage.')

# def log_in(request):
#     return render(request, 'log_in.html')