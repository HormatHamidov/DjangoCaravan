from django.shortcuts import render,redirect, get_object_or_404
from .forms import ArticleForm
from .models import Article
# Create your views here.

from functools import wraps
from django.shortcuts import render

def my_message(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Additional decorator logic or processing can be added here
        message = "Hello, World!"
        context = {
            'message': message
        }
        return render(request, 'index.html', context)
    
    return wrapper

@my_message
def home_view(request):
    pass


def list_view(request):
    context = {
        "articles" : Article.objects.all(),
    }
    return render(request, 'list.html', context)



def create_view(request):
    form = ArticleForm
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect("list")
        
                
        else: 
            print(form.errors)
    
    context={
        'form': form,
    }
    return render(request, 'create.html',context)


def update_view(request,id):
    product = get_object_or_404(Article,id=id)
    form = ArticleForm(instance=product)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=product)
        
        if form.is_valid():
            form.save()
            
            return redirect("list")

    
    context={
        'form': form,
    }
    return render(request, 'create.html',context)


def detail_view(request,id):
    context = {
        "article" : Article.objects.get(id=id)
    }
    return render(request, 'detail.html', context)


def delete_view(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    return redirect('list')