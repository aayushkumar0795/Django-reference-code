# Generated by Django 3.0.5 on 2020-05-04 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('O', 'Others'), ('F', 'Female')], max_length=1)),
                ('cars', models.ManyToManyField(to='main.Car')),
            ],
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_id', models.CharField(max_length=8)),
                ('issue_date', models.DateField(auto_now_add=True)),
                ('expire_date', models.DateField(auto_now_add=True)),
                ('country', models.CharField(max_length=50)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Person')),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_no', models.IntegerField()),
                ('landmark', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=100)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Person')),
            ],
        ),
    ]
