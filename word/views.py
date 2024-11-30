from django.shortcuts import render, redirect
from word.forms import CommentForm
from .models import Post, Item
from .serializer import ItmeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.views import LoginView
from .forms import SignUpForm
from django.contrib.auth import logout


def frontpage(request):
    posts = Post.objects.all()
    return render(request, "word/frontpage.html", {"posts": posts})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)

    else:
        form = CommentForm()

    return render(request, "word/post_detail.html", {"post": post, "form": form})


@csrf_exempt
@api_view(['POST'])
def create_item(request):
    serializer = ItmeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ログインページのビュー
class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    

# ログアウトのビュー
def logout_view(request):
    logout(request)
    return redirect("login")

# サインアップのビュー
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

# プロフィールページのビュー
def profile(request):
    return render(request, 'accounts/profile.html')
