# Generated by Django 5.2 on 2025-04-10 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_delete_profiles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='OnePiece',
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='luffy.jpg', upload_to='avatars'),
        ),
    ]
