from django.shortcuts import render,HttpResponse

def register(request):
    return HttpResponse('Placeholder for users to create a new user record.')
def login(request):
    return HttpResponse('Placeholder for users to login.')
def user_list(request):
    return HttpResponse('Placeholder to display list of all users.')