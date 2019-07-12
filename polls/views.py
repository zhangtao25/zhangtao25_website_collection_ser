from django.http import HttpResponse
import json
import os

def add_data(request):
    if request.method == 'POST':
        string = str(request.body, 'utf-8')
        write_request(string)
    return HttpResponse('ok')

def get_data(request):
    if request.method == 'GET':
        f2 = open(
            'D:\\Users\\tzhangm\\Desktop\\zhangtao25_website_collection\\zhangtao25_website_collection_ser\\website_files.txt',
            'r+')
        str = f2.read()
    return HttpResponse(str)

def write_request(str):
    f2 = open('D:\\Users\\tzhangm\\Desktop\\zhangtao25_website_collection\\zhangtao25_website_collection_ser\\website_files.txt','r+')
    f2.read()
    f2.write('\n' + str)
    f2.close()