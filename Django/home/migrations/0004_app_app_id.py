# Generated by Django 3.2 on 2021-04-28 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_app_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='app_id',
            field=models.IntegerField(default=1),
        ),
    ]
