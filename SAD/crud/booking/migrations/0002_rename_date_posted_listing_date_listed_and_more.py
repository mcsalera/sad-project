# Generated by Django 4.0.3 on 2022-03-31 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='date_posted',
            new_name='date_listed',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='content',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='author',
            new_name='owner',
        ),
    ]
