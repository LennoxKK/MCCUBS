from django.db import models
from django.urls import reverse

# Create your models here.


RESIDENCE = (
    ('CHIROMO', 'CHIROMO'),
    ('MAIN', 'MAIN'),
    ('HOME', 'HOME'),
)


class Member(models.Model):
    reg_no = models.CharField('Registration number',
                              max_length=18, unique=True)
    first_name = models.CharField('First name', max_length=30)
    sir_middle_name = models.CharField('Sir plus middle name', max_length=100)
    level = models.IntegerField('Year of study')
    date_registered = models.DateField(auto_now_add=True)
    phone_number = models.CharField(max_length=12, default='0720000000')
    place_of_residence = models.CharField(max_length=7, choices=RESIDENCE)
    group_number = models.PositiveBigIntegerField(default=0)

    def get_absolute_url(self):
        return reverse("Members:member-detail", kwargs={"id": self.id})

    def __str__(self):
        return self.first_name + " " + self.sir_middle_name


# m = Members(reg_no = "F17/1759/2019",first_name = 'Lennox',sir_middle_name = " Kahati Kanyoe",level = 1,date_registered = 122, phone_number = '0794401700",place_of_residence = choice_set.CHIROMO,group_number = 7)
#
