# Generated by Django 3.0.1 on 2020-01-01 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_name', models.CharField(max_length=50)),
                ('acc_price', models.IntegerField()),
                ('acc_image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Individualaccessories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_1', models.CharField(max_length=50)),
                ('feature_2', models.CharField(max_length=50)),
                ('feature_3', models.CharField(max_length=50)),
                ('feature_4', models.CharField(max_length=50)),
                ('feature_5', models.CharField(max_length=50)),
                ('iaccessories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capo.Guitar')),
            ],
        ),
    ]
