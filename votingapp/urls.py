from django.urls import path

from votingapp import views
from votingapp.views import ResetPasswordRequestView, ResetPasswordView, MessageSentView

app_name = 'votingapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.StudLoginView.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about, name='about'),
    path('teachers/', views.TeachersList.as_view(), name='teachers'),
    path('testVote/', views.vote_page, name='voting'),
    path('sendVote/', views.vote_result, name='vote_result'),
    path('reset/', ResetPasswordRequestView.as_view(), name='reset_request'),
    path('reset-password/<username>/<token>', ResetPasswordView.as_view(), name='reset'),
    path('reset-message/', MessageSentView.as_view(), name='reset_redirect_message'),
]
