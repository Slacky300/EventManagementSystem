# Generated by Django 4.1.7 on 2023-03-11 14:05

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventApp', '0005_createvent_evetyp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=300)),
                ('img', models.ImageField(blank=True, null=True, upload_to='venues/')),
                ('cpcty', models.PositiveIntegerField()),
                ('bkngPrice', models.PositiveIntegerField()),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('areaSpecs', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=400)),
                ('availabililty', models.BooleanField(default=True)),
                ('speciality', models.CharField(blank=True, choices=[('WeddingAnniversary', 'Wedding Anniversary'), ('BirthDay Party', 'BirthDay Party'), ('Conference', 'Conference'), ('CelebrationParty', 'Celebration Party')], max_length=100, null=True)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, default=None, editable=False, null=True, populate_from='name', unique=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eventApp.city')),
            ],
        ),
        migrations.AlterField(
            model_name='createvent',
            name='venue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eventApp.venues'),
        ),
        migrations.DeleteModel(
            name='EventPlace',
        ),
    ]