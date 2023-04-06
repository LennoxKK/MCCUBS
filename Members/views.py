
from .forms import MembersForm
import csv
from django.shortcuts import get_object_or_404,HttpResponse
from .models import Member


from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,

)

# Create your views here.

def _export_(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['first_name',
            'sir_middle_name',
            'reg_no',
            'level',
            'phone_number',
            'place_of_residence',
            'gender'])
    for member in Member.objects.all():
        member = [member.first_name,member.sir_middle_name,member.reg_no,member.level,member.phone_number,member.place_of_residence,member.gender]
        writer.writerow(member)

    response['Content-Disposition']='attachment;filename="members.csv"'
    return response

class MemberCreateView(CreateView):
    template_name = "Members/game.html"
    form_class = MembersForm
    # success_url='/'

    def form_valid(self, form):
        return super().form_valid(form)


class MemberListView(ListView):
    template_name = "Members/the_member_list.html"
    context_object_name = "list"
    queryset = Member.objects.order_by('place_of_residence')


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
    # queryset=BStudyMember.objects.all()

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Member, id=id)

    def form_valid(self, form):
        return super().form_valid(form)
