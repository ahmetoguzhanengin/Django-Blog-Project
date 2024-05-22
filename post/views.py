from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.utils.text import slugify

# Create your views here.

def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html' , {'posts' : posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post' : post,
    }
    return render(request, 'post/detail.html', context)

#alternatif 1:
# if request.method == "POST":
      #  print(request.POST)
    #title = request.POST.get ('title')
    #content = request.POST.get ('content')
    #Post.objects.create(title= title, content= content)

#alternatif 2:
    # if request.method == "POST":
        #FORMDAN GELEN BİLGİLERİ KAYDET
        #form = PostForm(request.POST)
       # if form.is_valid():
           # form.save()
       # else:
            #FORMDAN GELEN BİLGİLERİ KULLANICIYA GÖSTER
           # form = PostForm()


def post_create(request):

    if not request.user.is_authenticated:
        raise Http404()


    form = PostForm (request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save()

        messages.success(request, 'Başarılı bir şekilde oluşturuldu!', extra_tags= "mesaj-basarili")
        return HttpResponseRedirect (post.get_absolute_url())
    context = {
            'form': form,
        }
    return render(request, 'post/form.html', context)


def post_update(request, slug):

    if not request.user.is_authenticated:
        raise Http404()

    post = get_object_or_404(Post, slug=slug)
    form = PostForm (request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, 'Başarılı bir şekilde güncellendi!')

        return HttpResponseRedirect (post.get_absolute_url())

    context = {
        'form': form,
    }
    return render(request, 'post/form.html', context)


def post_delete(request,slug):
    if not request.user.is_authenticated:
        raise Http404()

    post = get_object_or_404(Post, slug=slug)
    post.delete()

    return redirect('post:index')