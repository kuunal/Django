# Generated by Django 3.0.7 on 2020-06-18 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20200617_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
