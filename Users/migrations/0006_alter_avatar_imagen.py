# Generated by Django 4.0.3 on 2022-05-24 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_alter_avatar_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatar/% Y/% m/'),
        ),
    ]
