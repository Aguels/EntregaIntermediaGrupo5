# Generated by Django 4.0.3 on 2022-03-22 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Musicy', '0002_blogentry_musicians_delete_nolyric_delete_poetry'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Musicians',
            new_name='Musician',
        ),
    ]
