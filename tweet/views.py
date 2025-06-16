from django.shortcuts import render, get_object_or_404, redirect
from .models import tweet , Like
from .forms import tweetForm , UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout

def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets = tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})
@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = tweetForm(request.POST, request.FILES) 
        if form.is_valid():
            tweet = form.save(commit=False) 
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = tweetForm()
    return render(request, 'tweet_form.html', {'form': form})
@login_required
def tweet_edit(request, tweet_id):
    T = get_object_or_404(tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        form = tweetForm(request.POST, request.FILES, instance=T)
        if form.is_valid():
            T = form.save(commit=False)
            T.user = request.user
            T.save()
            return redirect('tweet_list')
    else:
        form = tweetForm(instance=T) 
    return render(request, 'tweet_form.html', {'form': form})
@login_required
def tweet_del(request, tweet_id):
    T = get_object_or_404(tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        T.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_conf_del.html', {'tweet': T})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ✅ Logs in the user after registration
            return redirect('tweet_list')  # ✅ Redirect to correct URL
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def tweet_detail(request , tweet_id):
    t = get_object_or_404(tweet, pk=tweet_id)
    return render(request, 'tweet_detail.html', {'tweet': t})

@login_required
def toggle_like(request, tweet_id):
    t = get_object_or_404(tweet, pk=tweet_id)
    like, created = Like.objects.get_or_create(user=request.user, tweet=t)
    if not created:
        like.delete()  # Unlike
    return redirect('tweet_list')