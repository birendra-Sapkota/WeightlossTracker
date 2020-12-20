from django.urls import path
from .views import home, user_home,index, weeklyReportView,contact, aboutus, edit_profile, user_dashboard, add_cf, recommend_plan,get_data, Weekly_Rep, admin_home,adm_user_dashboard,adm_verify_user, adm_addfood, adm_view_all_user, adm_view_allfood, user_profile

app_name = 'home'
urlpatterns = [
    path('', home, name='home'),

    path('userhome', user_home, name='userhome'),
    path('editprofile', edit_profile, name='editprofile'),
    path('userdashboard', user_dashboard, name='user_dashboard'),
    path('addcf', add_cf, name='addcf'),
    path('recommend_plan', recommend_plan, name='recommend_plan'),
    path('weekly_rep', weeklyReportView.as_view(), name='weekly_rep'),
    path('weekly_rep/data', get_data, name='weekly_rep-data'),
    path('weekly_rep/chat/data', Weekly_Rep.as_view()),

    path('viewallfood', adm_view_allfood, name='viewallfood'),
    path('aboutus', aboutus, name='aboutus'),
    path('contact', contact, name='contact'),
    path('index', index, name='index'),
    path('adminhome', admin_home, name='adminhome'),
    path('updateuserprofile', edit_profile, name='updateuserprofile'),
    path('admuserdashboard', adm_user_dashboard, name='admuserdashboard'),
    path('admverifyuser', adm_verify_user, name='admverifyuser'),
    path('addfood', adm_addfood, name='addfood'),
    path('viewalluser', adm_view_all_user, name='viewalluser'),
    path('userprofile', user_profile, name='userprofile'),

]

