# Generated by Django 3.2.18 on 2023-10-12 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='age',
            field=models.PositiveIntegerField(default=1),
        ),
    ]