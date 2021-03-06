# Generated by Django 3.2.8 on 2021-10-13 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pic', models.ImageField(upload_to='blog-img/')),
                ('subtitle', models.CharField(max_length=250)),
                ('text', models.TextField(max_length=2500)),
            ],
        ),
    ]
