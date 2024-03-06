from django.urls import path
from .import views

urlpatterns=[
    path('index',views.index,name='index'),
    path('register',views.register,name='register'),
    path('client',views.client,name='client'),
    path('contact',views.contact,name='contact'),
    path('health',views.health,name='health'),
    path('medicine',views.medicine,name='medicine'),
    path('news',views.news,name='news'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name="logout"),
    path('diabetes',views.diabetes,name='diabetes'),
    path('diabetespredict',views.diabetespredict,name='diabetespredict')

]