# Generated by Django 2.2.6 on 2019-11-25 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0003_loanapplication_loan_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanapplication',
            name='loan_id',
            field=models.FloatField(default=10000000, max_length=150),
        ),
    ]
