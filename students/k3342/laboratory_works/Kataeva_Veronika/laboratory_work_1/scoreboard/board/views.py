from django.shortcuts import render, get_object_or_404, redirect
from board.models import Racer, Comment, Race, Team, Car
from board.forms import CommentForm
# from datetime import datetime, timedelta

def show_board(request):
    context = {}
    context['racers'] = Racer.objects.all()
    context['teams'] = Team.objects.all()
    context['cars'] = Car.objects.all()
    context['races'] = Race.objects.all()
    return render(request, 'racers_list.html', context)


def see_comments(request, pk):
    context = {}
    context['racer'] = get_object_or_404(Racer, id=pk)
    context['teams'] = Team.objects.all()
    context['cars'] = Car.objects.all()
    context['races'] = Race.objects.all()
    context['comments'] = Comment.objects.filter(racer_id=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.racer_id = pk
            form.save()
            context['form'] = form
            return redirect(see_comments, pk)
    else:
        form = CommentForm()
        context['form'] = form
    return render(request, 'racers_comments.html', context)

"""

def new_single(request, pk):

    new = get_object_or_404(News, id=pk)
    comment = Comments.objects.filter(new=pk, moderation=True)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.new = new
            form.save()
            return redirect(new_single, pk)
    else:
        form = CommentForm()
    return render(request, "news/new_single.html",
                  {"new": new,
                   "comments": comment,
                   "form": form})
"""

