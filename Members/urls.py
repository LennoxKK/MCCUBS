from django.urls import path
from .views import (
    MemberCreateView, MemberDetailView, MemberListView, MemberUpdateView
)
from .models import Member

app_name = 'Members'

urlpatterns = [
    path('register/', MemberCreateView.as_view(), name='member-register'),
    path('list/', MemberListView.as_view(), name='member-list'),
    path('<int:id>/', MemberDetailView.as_view(model=Member), name='member-detail'),
    path('<pk>/update/', MemberUpdateView.as_view(model=Member),
         name='member-update'),
]
