# Generated by Django 2.1.3 on 2018-11-26 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20181126_0708'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=50)),
                ('price', models.FloatField(default=0.0)),
                ('numbers', models.IntegerField(default=0)),
                ('pname', models.CharField(max_length=20)),
                ('parea', models.CharField(max_length=20)),
            ],
        ),
    ]
