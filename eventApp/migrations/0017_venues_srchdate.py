# Generated by Django 4.1.7 on 2023-03-17 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventApp', '0016_receipt_rcptdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='venues',
            name='srchDate',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]