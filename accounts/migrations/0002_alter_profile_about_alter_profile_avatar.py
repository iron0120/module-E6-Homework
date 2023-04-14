# Generated by Django 4.1.7 on 2023-03-25 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.CharField(blank=True, default='Write a bit about yourself', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='Load', null=True, upload_to='avatars'),
        ),
    ]