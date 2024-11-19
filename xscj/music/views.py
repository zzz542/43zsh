from re import search
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Music,Review
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def musichome(request):
    searchTerm = request.GET.get('searchMusic')
    if searchTerm:
        musics = Music.objects.filter(title__contains=searchTerm)
    else:
        musics = Music.objects.all()
        paginator =Paginator(musics,2)
        page_number=request.GET.get('page',1)
        musics=paginator.page(page_number)
    return render(request,'musichome.html',{'searchTerm':searchTerm,'musics':musics})

def home(request):
    return render(request,'home.html',{'name':'ZZZ'})
#
def signup(request):
    email=request.GET.get('email')
    return render(request,'signup.html',{'email':email})

def musicdetail(request, music_id):
    music = get_object_or_404(Music, pk=music_id)
    reviews = Review.objects.filter(music=music)
    return render(request, 'musicdetail.html', {'music': music, 'reviews': reviews})

@login_required
def createmusicreview(request, music_id):
    music = get_object_or_404(Music,pk=music_id)
    if request.method == 'GET' :
        return render(request, 'createmusicreview.html' ,
        {'form':ReviewForm , 'music':music})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.music = music
            newReview.save()
            return redirect('musicdetail',newReview.music.id)
        except ValueError:
            return render(request,'createmusicreview.html', {'form':ReviewForm, 'error':'非法数据'})

@login_required
def updatemusicreview(request, review_id) :
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'updatemusicreview.html', {'review':review, 'form':form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('musicdetail', review.music.id)
        except ValueError:
            return render(request, 'updatemusicreview.html', {'review':review, 'form':form, 'error':'提交非法数据'})

@login_required
def deletemusicreview(request, review_id) :
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('musicdetail', review.music.id)