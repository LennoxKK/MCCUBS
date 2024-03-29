# Generated by Django 4.1.7 on 2023-02-26 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0003_remove_members_phone_nnumber_members_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('reg_no', models.CharField(max_length=18, primary_key=True, serialize=False, verbose_name='Registration number')),
                ('first_name', models.CharField(max_length=30, verbose_name='First name')),
                ('sir_middle_name', models.CharField(max_length=100, verbose_name='Sir plus middle name')),
                ('level', models.IntegerField(verbose_name='Year of study')),
                ('date_registered', models.DateField(auto_now_add=True)),
                ('phone_number', models.CharField(default='0720000000', max_length=12)),
                ('place_of_residence', models.CharField(choices=[('CHIROMO', 'CHIROMO'), ('MAIN', 'MAIN'), ('HOME', 'HOME')], max_length=7)),
                ('group_number', models.PositiveBigIntegerField(max_length=2, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Members',
        ),
    ]
