from django.urls import path
from User.views import register
from django.contrib.auth import views as auth_views
from .views import (
    MemberCreateView, MemberDetailView, MemberListView, MemberUpdateView,_export_
)
from .models import Member

app_name = 'Members'

urlpatterns = [
    path('register/', MemberCreateView.as_view(), name='member-register'),
    path('<int:id>/', MemberDetailView.as_view(model=Member), name='member-detail'),
    path('<int:id>/update/', MemberUpdateView.as_view(model=Member),
         name='member-update'),
    path('_export_/',_export_,name='download')
]






