# Generated by Django 3.2.6 on 2021-08-09 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='likes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='release_date',
            field=models.DateField(null=True),
        ),
    ]