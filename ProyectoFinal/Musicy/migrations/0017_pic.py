# Generated by Django 4.0.3 on 2022-04-19 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Musicy', '0016_remove_blogentry_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='images')),
                ('Musico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Musicy.musician')),
            ],
        ),
    ]