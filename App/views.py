import random

from django.http import HttpResponse
from django.shortcuts import render

from App.models import Person


def add_persons(request):
    for i in range(15):
        person = Person()
        flag = random.randrange(100)
        person.p_name = 'Tom%d' % i
        person.p_age = flag
        person.p_sex = flag % 2
        person.save()
    return HttpResponse("创建成功！")


def get_persons(request):
    persons = Person.objects.exclude(p_age__lt=30).filter(p_age__lt=50)
    print(type(persons))
    context = {
        'persons': persons,

    }
    return render(request, 'person_list.html', context=context)


def add_person(request):
    # person = Person.objects.create(p_name='WangGang', p_age=20, p_sex=False)
    # person = Person(p_age=28)
    person = Person.create('Jack')

    person.save()

    return HttpResponse('创建成功！')


def get_person(request):
    # person = Person.objects.get(p_age=20)
    # print(person)
    person = Person.objects.all().first()
    print(person.p_name)

    person = Person.objects.all().last()
    print(person.p_age)
    return HttpResponse("获取成功")
