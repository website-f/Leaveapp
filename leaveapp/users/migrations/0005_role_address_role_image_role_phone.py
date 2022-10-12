# Generated by Django 4.1 on 2022-08-29 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_delete_cawangan_role_cawangan'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='role',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='role',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]