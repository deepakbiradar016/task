# Generated by Django 2.2.15 on 2020-09-01 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=250)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=20, null=True)),
                ('mother_tongue', models.CharField(max_length=255)),
                ('profile', models.ImageField(blank=True, null=True, upload_to='profile_pics')),
                ('phone', models.CharField(max_length=15)),
                ('category', models.CharField(choices=[('Owner', 'Owner'), ('Customer', 'Customer'), ('Admin', 'Admin'), ('Tenant', 'Tenant')], default='customer', max_length=20)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]