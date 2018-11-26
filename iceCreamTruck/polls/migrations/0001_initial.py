# Generated by Django 2.1.3 on 2018-11-26 06:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_Name', models.CharField(max_length=25)),
                ('last_Name', models.CharField(max_length=25)),
                ('street_Address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2, validators=[django.core.validators.RegexValidator('.{2}$')])),
                ('zip_Code', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator('^\\d{5}$')])),
            ],
        ),
        migrations.CreateModel(
            name='OrderForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavor', models.CharField(max_length=200)),
                ('product_id', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('total_cost', models.IntegerField(default=0)),
                ('current_date', models.DateTimeField(verbose_name='current date')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.OrderForm'),
        ),
    ]
