# Generated by Django 4.0.4 on 2022-07-21 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApps', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productscategory',
            old_name='pc_name',
            new_name='category_name',
        ),
    ]
