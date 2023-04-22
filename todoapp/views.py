from django.shortcuts import render, redirect
from todoapp.models import TodoItem, TodoUsers
from django.http import HttpResponse
import json


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

    items = TodoItem.objects.all()
    return render(request, 'index.html', {'items': items})
    return render(request, 'log_in.html')

def authentification(request):
    pass

def delete(request, item):
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
            else:
                for i in range(len(TodoItem.objects.all())):
                    try:
                        TodoItem.objects.get(item_id = text + str(i))
                    except TodoItem.DoesNotExist:
                        item = TodoItem(item_id = text + str(i), text = text)
                        item.save()
                        break

    
        print(f"Добавлено: {request.POST['text']}") 
    return redirect('index')

def account(request):
    return render(request, 'account.html')

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
    item_to_switch = TodoItem.objects.get(item_id = item)
    print(f'Выполнено "{item_to_switch.item_id}"')
    item_to_switch.completed = True
    item_to_switch.save()
    return redirect('index')

def turn_Off(request, item):
    item_to_switch = TodoItem.objects.get(item_id = item)
    print(f'Ошибочка, не выполнено "{item_to_switch.item_id}"')
    item_to_switch.completed = False
    item_to_switch.save()
    return redirect('index')

# def create_cookie(request):
#     html = HttpResponse("Welcome to django website")
#     html.set_cookie('django', "created", max_age = None)
#     print("created")
#     return html

# def get_cookie(request):
#     print("got")
#     show = request.COOKIES['django']
#     print(show)
#     # html = "New Page {0}".format(show)
#     # return HttpResponse(html)