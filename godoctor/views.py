import pymysql.cursors

from django.db.backends import mysql
from django.http import HttpResponse
from django.shortcuts import render
from .models import Question


def index(request):
    return render(request, 'godoctor/index.html')


# Create your views here.
def home(request):
    return render(request, 'godoctor/home.html')


def genre(request):
    return render(request, 'godoctor/genre.html')


def age(request):
    return render(request, 'godoctor/age.html')


def login(request):
    return render(request, 'godoctor/login.html')


def register(request):
    return render(request, 'godoctor/register.html')


def symptomes(request):
    connect = pymysql.connect(host='127.0.0.1', user='root', password='', db='godoctor', charset='utf8mb4')
    cur = connect.cursor()
    cur.execute("SELECT DISTINCT symptom FROM symptoms")
    symptom = cur.fetchall()
    result = []
    for elem in symptom:
        result.append(elem[0])
    return render(request, 'godoctor/symptomes.html', {'symptom': result})
