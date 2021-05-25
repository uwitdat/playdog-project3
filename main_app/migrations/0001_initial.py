# Generated by Django 3.2.3 on 2021-05-24 02:03

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
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('age', models.IntegerField()),
                ('size', models.CharField(choices=[('T', 'TINY'), ('S', 'SMALL'), ('M', 'MEDIUM'), ('L', 'LARGE'), ('X', 'EXTRA LARGE')], default='M', max_length=1)),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], default='M', max_length=1)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField(verbose_name='Event date')),
                ('description', models.TextField(max_length=250)),
                ('location', models.FloatField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('attendees', models.ManyToManyField(to='main_app.Dog')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
