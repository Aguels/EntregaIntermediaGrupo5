# Generated by Django 4.0.3 on 2022-05-24 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_blogentry_imagen_delete_blogpicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='blog/% Y/% m/% d/% H/% M/% S/'),
        ),
    ]
