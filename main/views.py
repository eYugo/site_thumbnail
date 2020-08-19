from django.shortcuts import render, redirect, get_object_or_404
from .forms import VoteForm, PostCreateForm, ThumbnailCreateForm
from .models import Thumbnail, Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test


def home(request):
    context = {
        'hey': 'ola'
    }
    return render(request, 'main/home.html', context)


def PostDetailView(request, pk):
    post_request = get_object_or_404(Post, id=pk)
    thumbnails = Thumbnail.objects.filter(post=post_request).all()
    context = {
        'thumbnails': thumbnails,
        'post': post_request
    }
    return render(request, 'main/post_detail.html', context)


def VoteConfirm(request, pk):
    thumb_voted = Thumbnail.objects.get(id=pk)
    if request.method == 'POST':
        thumb_voted.num_votos += 1
        thumb_voted.save()
        messages.success(
            request, f'Thanks for voting!')
        return redirect('home')
    context = {
        'thumb': thumb_voted
    }
    return render(request, 'main/vote_confirm.html', context)


@login_required
def PostCreate(request):
    p_form = PostCreateForm()
    t_form = ThumbnailCreateForm()
    if 'thumbnail' in request.POST:
        t_form = ThumbnailCreateForm(request.POST, request.FILES)
        if t_form.is_valid():
            autor = request.user
            if Thumbnail.objects.filter(autor=autor).count() == 6:
                messages.error(request, 'Max 6 thumbnails allowed!')
                return redirect('/post/new/')
            else:
                t_form.instance.autor = autor
                t_form.save()
                return redirect('/post/new/')

    elif 'post' in request.POST:
        p_form = PostCreateForm(request.POST)
        if p_form.is_valid():
            p_form.instance.autor = request.user
            post = p_form.save(commit=False)
            post.save()
            fila = Thumbnail.objects.filter(autor=request.user).all()

            for thumb in fila:
                thumb.post = post
                thumb.autor = None
                thumb.save()

            messages.success(
                request, f'Congratulations for creating a Post!')

            post_id = post.id
            return redirect('/post/{}/'.format(post_id))

    context = {'p_form': p_form, 't_form': t_form,
               'thumbnails': Thumbnail.objects.filter(autor=request.user).all()}
    return render(request, 'main/post_create.html', context)

# arrumar para que outros usuários não deletem suas thumbs
@login_required
def ThumbDelete(request, pk):
    thumb_del = Thumbnail.objects.get(id=pk)
    if thumb_del.post.autor != request.user:
        messages.error(
            request,  "You are not the author of this Post! You can't delete it!")
        return redirect('my-posts')
    thumb_del.delete()
    return redirect('/post/new/')


@login_required
def MyPostsView(request):
    posts = Post.objects.filter(autor=request.user).order_by('-data')
    dict = {}
    thumbnails = []
    for post in posts:
        thumbnails = Thumbnail.objects.filter(post=post).all()
        dict[post.id] = thumbnails
    context = {
        'posts': posts,
        'dict': dict,
    }
    return render(request, 'main/my_posts.html', context)


@login_required
def PostResultView(request, pk):
    post_request = get_object_or_404(Post, id=pk)
    if post_request.autor != request.user:
        messages.error(
            request,  "You are not the author of this Post! You can't view the result!")
        return redirect('my-posts')
    else:
        thumbnails = Thumbnail.objects.filter(
            post=post_request).order_by('-num_votos')
        context = {
            'thumbnails': thumbnails,
            'post': post_request
        }
        return render(request, 'main/post_result.html', context)


@login_required
def PostDeleteView(request, pk):
    post_del = get_object_or_404(Post, id=pk)
    if post_del.autor != request.user:
        messages.error(
            request,  "You are not the author of this Post! You can't delete it!")
        return redirect('my-posts')
    else:
        thumbnails = Thumbnail.objects.filter(post=post_del).all()
        if request.method == 'POST':
            post_del.delete()
            messages.success(
                request, f'Your Post has been deleted successfully!')
            return redirect('my-posts')
        context = {
            'thumbnails': thumbnails,
            'post': post_del
        }
        return render(request, 'main/post_confirm_delete.html', context)
