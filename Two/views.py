from django.db.models import Max, Avg, F, Q
from django.http import HttpResponse
from django.shortcuts import render

from Two.models import User, Order, Grade, Customer, Company, Animal


def get_user(request):
    username = 'Wanggang'
    password = '12030'
    users = User.objects.filter(u_name=username)
    print(users.count())
    if users.count():
        user = users.first()
        if user.u_password == password:
            print("获取用户信息成功")
        else:
            print("密码错误")
    else:
        print("用户名不存在")

    return HttpResponse("获取成功")


def get_users(request):
    users = User.objects.all()[1:5]
    context = {
        'users': users
    }
    return render(request, 'user_list.html', context=context)


def get_orders(request):
    orders = Order.objects.filter(o_time__month=11)
    for order in orders:
        print(order.o_num)
    return HttpResponse("获取成功")


def get_grades(request):
    grades = Grade.objects.filter(student__s_name='wanggang')
    for grade in grades:
        print(grade.g_name)
    return HttpResponse("获取成功")


def get_costs(request):
    result = Customer.objects.aggregate(Avg("c_cost"))
    print(result)
    return HttpResponse('获取成功了')


def get_company(request):
    # companies = Company.objects.filter(c_boy_num__lt=F('c_girl_num'))
    # companies = Company.objects.filter(c_boy_num__lt=F('c_girl_num')-15)
    companies = Company.objects.filter(Q(c_boy_num__gt=1) & Q(c_girl_num__gt=5))
    for company in companies:
        print(company.c_name)
    return HttpResponse("哈哈哈")


def get_animals(request):
    animals = Animal.objects.all()
    for animal in animals:
        print(animal.a_name)
    return HttpResponse("获取成功")