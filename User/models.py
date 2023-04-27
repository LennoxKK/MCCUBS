from django.db import models
from django.urls import reverse
from PIL import Image
from django.contrib.auth.models import User as Ad
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


RESIDENCE = (
    (None, "Place of residence"),
    ('CHIROMO', 'CHIROMO'),
    ('MAIN', 'MAIN'),
    ('HOME', 'HOME'),
)
GENDER = (
    (None, 'Choose   Gender'),
    ('M', 'M'),
    ('F', 'F'),
)


class User(models.Model):
    reg_no = models.CharField('Registration number',
                              max_length=30, unique=True,default='Registration number')
    first_name = models.CharField('First name', max_length=30)
    sir_middle_name = models.CharField('Sir plus middle name', max_length=100)
    level = models.IntegerField('Year of study')
    date_registered = models.DateField(auto_now_add=True)
    phone_number = models.CharField(max_length=12, default='0720000000',unique=True)
    place_of_residence = models.CharField(max_length=7, choices=RESIDENCE)
    group_number = models.PositiveBigIntegerField(default=0)
    gender = models.CharField(max_length=1, choices=GENDER)

    def get_absolute_url(self):
        return reverse("Members:member-detail", kwargs={"id": self.id})

    def __str__(self):
        return self.first_name + " " + self.sir_middle_name


class Profile(models.Model):
    user = models.OneToOneField(Ad, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # Override the save method of the model
    def save(self):
        super().save()

        img = Image.open(self.image.path) # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) # Save it again and override the larger image

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.first_name} Profile'

    # Override the save method of the model
    def save(self):
        super().save()

        img = Image.open(self.image.path) # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) # Save it again and override the larger image





class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        raise ValueError('CustomUser does not support superuser creation')

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
