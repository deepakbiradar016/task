# Generated by Django 2.2.15 on 2020-10-25 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_jsondata_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jsondata',
            name='json_id',
        ),
        migrations.AlterField(
            model_name='jsondata',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
