# Generated by Django 3.2.6 on 2021-08-26 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_rename_description_contact_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.TextField(default=''),
        ),
    ]
