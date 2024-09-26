from django.contrib import admin
from django.urls import path
from kursovik.views import *
urlpatterns=[
    path('rooms/', RoomView.as_view()),
    path('clients/', ClientView.as_view()),
    path('workers/', WorkerView.as_view()),
    path('worktable/',WorktableView.as_view()),
    path('journal/',JournalView.as_view()),
    path('request1/',Request1View.as_view()),
    path('report/',ReportView.as_view()),
    path('request2/',Request2View.as_view()),
    path('request3/',Request3View.as_view()),
    path('request4/',Request4View.as_view()),
    path('request5/',Request5View.as_view()),
    path('worktableq/',WorktableQ.as_view()),
    path('journalq/',JournalQ.as_view()),
]