# Generated by Django 2.2.6 on 2019-11-13 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('duty', '0005_flat_sqare'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='flat',
            unique_together={('number', 'address')},
        ),
    ]