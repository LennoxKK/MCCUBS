# Generated by Django 4.1.7 on 2023-02-26 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0007_members_delete_member'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Members',
            new_name='Member',
        ),
    ]
