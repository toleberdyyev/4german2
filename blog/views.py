from django.shortcuts import render
from django.utils import timezone
from .models import Post, Comment
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    comments = Comment.objects.filter(post=post).filter(parent=None)
    context = {
        'post': post,
        'form': form,
        'comments': comments
    }
    #form_r = CommentReplyForm()
    if request.method =="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.published_date = timezone.now()
            print(comment.parent)
            comment.save()
            return render(request, 'blog/container.html',context )
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', context)

def user_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            print(user.avatar)
            user.save()
            return redirect('django.contrib.auth.views.login')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'blog/reg.html', context)

@login_required
def user_profile(request,id):
    us = get_object_or_404(User, id=id)
    posts = Post.objects.filter(author=id).order_by('-published_date')
    if request.method == "POST":
        print('SEE POST REQ')
        form = PostForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            print('++++++++++++++++++++++++++++ SEEMS IT VALID ++++++++++++++++++++++++++')
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            print('asd')
            post.save()
            return render(request, 'blog/user_profile.html', {'form':form,'posts':posts,'us':us})
    else:
        form = PostForm()
    return render(request, 'blog/user_profile.html', {'form':form,'posts':posts,'us':us})


@login_required
def post_new(request,pk):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/user_profile.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})



@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog.views.post_detail', pk=pk)
@login_required
def publish(self):
    self.published_date = timezone.now()
    self.save()
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog.views.post_list')
