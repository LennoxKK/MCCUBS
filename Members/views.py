
from .forms import MembersForm
from django.shortcuts import get_object_or_404
from .models import Member

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,

)

# Create your views here.


class MemberCreateView(CreateView):
    template_name = "Members/the_member_create.html"
    form_class = MembersForm
    # success_url='/'

    def form_valid(self, form):
        return super().form_valid(form)


class MemberListView(ListView):
    template_name = "Members/the_member_list.html"
    context_object_name = "list"
    queryset = Member.objects.all()


class MemberDetailView(DetailView):
    template_name = "Members/the_member_detail.html"
   # queryset=The_member.objects.all()
    model = None

    def get_object(self, queryset=None):
        return queryset.get(model=self.model)

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(self.model, id=id)


class MemberUpdateView(UpdateView):
    template_name = "Members/the_member_update.html"
    form_class = MembersForm
    model = Member
