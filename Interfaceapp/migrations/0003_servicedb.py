# Generated by Django 4.2.4 on 2023-10-17 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Interfaceapp', '0002_signupdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Email', models.CharField(blank=True, max_length=50, null=True)),
                ('Select', models.CharField(blank=True, max_length=50, null=True)),
                ('Phone', models.CharField(blank=True, max_length=50, null=True)),
                ('Request', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]