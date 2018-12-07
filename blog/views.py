from django.shortcuts import render

from .models import Post,Tag
from .forms import TagForm
from django.shortcuts import redirect

from .utils import ObjectDetailMixin

from django.views.generic import View

def index(request):
    return render(request,'index.html',{})

def posts_list(request):
    posts = Post.objects.all()
    return render(request,'post.html',context={'posts':posts})

class PostDetail(ObjectDetailMixin,View):
    model = Post
    template = 'post_detail.html'


class TagDetail(ObjectDetailMixin,View):
    model = Tag
    template = 'tag_detail.html'


class TagCreate(View):
    def get(self,request):
        form = TagForm()
        return render(request, 'tag_create.html',context={'form':form})
    def post(self,request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'tag_create.html',context={'form':bound_form})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request,'tags_list.html',context={'tags':tags})

""" 
def post_details(request,slug) :
    post = Post.objects.get(slug__iexact=slug)
    return render(request,'post_detail.html',context={'post':post})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request,'tags_list.html',context={'tags':tags}) """

""" def tag_detail(request,slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request,'tag_detail.html',context={'tag':tag}) """
# Create your views here.
