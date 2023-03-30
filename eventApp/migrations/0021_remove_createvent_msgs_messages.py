# Generated by Django 4.1.7 on 2023-03-19 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventApp', '0020_createvent_msgs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createvent',
            name='msgs',
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msgText', models.TextField()),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventApp.venues')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventApp.createvent')),
            ],
        ),
    ]