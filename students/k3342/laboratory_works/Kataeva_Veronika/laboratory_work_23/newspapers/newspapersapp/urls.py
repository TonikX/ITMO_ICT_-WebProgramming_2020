from django.contrib import admin
from django.urls import path
from newspapersapp.views import *


urlpatterns = [
    path('postoffices/', PostOfficeView.as_view()),
    path('certificate/', CertificateView.as_view()),
    path('report/', ReportView.as_view()),
    path('request1/', Request1View.as_view()),
    path('request2/', Request2View.as_view()),
    path('request3/', Request3View.as_view()),
    path('request4/', Request4View.as_view()),
    path('request5/', Request5View.as_view()),
    path('newspapers/', Newspapers.as_view()),
    path('houses/', Houses.as_view()),
    path('addresses/', Addresses.as_view()),
    path('postoffice/', OfficeView.as_view()),
    path('editors/', EditorsView.as_view()),
    path('editor/', EditorView.as_view()),
    path('printinghouses/', PrintingHouses.as_view()),
    path('printinghouse/', PrintingHouseView.as_view()),
    path('papers/', Papers.as_view()),
    path('paper/', Paper.as_view()),
    path('editorslist/', EditorsListView.as_view()),
    path('instocks/', InStockView.as_view()),
    path('instock/', StockView.as_view()),
    path('offices/', Offices.as_view())
]


