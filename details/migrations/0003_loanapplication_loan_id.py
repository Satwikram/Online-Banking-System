# Generated by Django 2.2.6 on 2019-11-25 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0002_useraccount_cashback'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanapplication',
            name='loan_id',
            field=models.IntegerField(default=10000000),
        ),
    ]
