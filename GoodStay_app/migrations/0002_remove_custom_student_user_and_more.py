# Generated by Django 5.0.7 on 2024-08-02 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GoodStay_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custom_student',
            name='user',
        ),
        migrations.RemoveField(
            model_name='custom_warden',
            name='user1',
        ),
    ]
