# Generated by Django 3.0.7 on 2020-10-12 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
