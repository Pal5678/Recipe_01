from django.urls import path
from . import views
urlpatterns=[
    path('app1/',views.htmlexample,name='htmlexample'),
    path('app1/app2/',views.htmlexample1,name="htmlexample1"),
    path('app1/app2/app3/',views.htmlexample2,name="htmlexample2"),
    path('app1/app2/app4/',views.htmlexample3,name="htmlexample3"),
    path('app1/app2/app5/',views.htmlexample4,name="htmlexample4"),

]