# Generated by Django 4.2.14 on 2024-07-21 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='data',
            new_name='date',
        ),
    ]
