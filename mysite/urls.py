from django.urls import path

from . import views

urlpatterns=[
   path('xml',views.xmlview,name='xmlview'),
   path('html',views.htmlview,name='htmlview'),
   path('pdf',views.pdfview,name='pdfview'),
]