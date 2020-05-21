from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    
    path('', views.index, name='index'),
    path('category/', views.category, name='category'),
    path('category/<int:category_id>/', views.detail, name='detail'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('contact/', views.contact, name='contact'),
    path('quiz/', views.quizcat, name='quizcat'),
    path('quiz/<str:category_name>/', views.sets, name='sets'),
    path('quiz/set/<int:set_id>/', views.quiz, name='quiz'),
    
]