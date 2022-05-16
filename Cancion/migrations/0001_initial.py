# Generated by Django 4.0.3 on 2022-05-16 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('letra', models.TextField()),
                ('link', models.URLField()),
                ('acordes', models.CharField(max_length=200)),
                ('tono', models.CharField(max_length=3)),
            ],
        ),
    ]
