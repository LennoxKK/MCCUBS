# Generated by Django 4.1.7 on 2023-02-25 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='id',
        ),
        migrations.AlterField(
            model_name='members',
            name='reg_no',
            field=models.CharField(max_length=18, primary_key=True, serialize=False, verbose_name='Registration number'),
        ),
    ]
