# Generated by Django 3.2.5 on 2022-05-31 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_newsletterrecipients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletterrecipients',
            name='lastname',
        ),
    ]