# Generated by Django 5.0.7 on 2024-08-06 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GoodStay_app', '0009_alter_schedule_date_out'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='user',
            new_name='user1',
        ),
    ]
