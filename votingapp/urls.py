from django.urls import path

from votingapp import views
from votingapp.views import TeachersList

app_name = 'votingapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about, name='about'),
    path('teachers/', views.TeachersList.as_view(), name='teachers'),
    path('testVote/', views.vote_page, name='voting'),
    path('sendVote/', views.vote_result, name='vote_result'),

]
