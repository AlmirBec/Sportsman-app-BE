# Generated by Django 4.2 on 2023-05-22 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsman', '0013_merge_20230523_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sporthall',
            name='pictures',
            field=models.TextField(null=True),
        ),
    ]
