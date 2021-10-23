from django.shortcuts import render,HttpResponse,redirect

def index(request):
    return HttpResponse('Placeholder to later display a list of all blogs')
def new(request):
    return HttpResponse('Placeholder to later display a new form to create a new blog')
def create(request):
    return redirect('blogs:main_page')
def show(request,id):
    return HttpResponse(f'Placeholder to display blog number {id}')
def edit(request,id):
    return HttpResponse(f'Placeholder to edit blog {id}')
def destroy(request,id):
    return redirect('blogs:main_page')