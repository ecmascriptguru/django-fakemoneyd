# Generated by Django 3.0.6 on 2020-10-31 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fakemoneyd', '0002_currency_meta_ordering'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemoFakeMoneyModelBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='amount')),
                ('currency', models.ForeignKey(help_text='this can be real world currency or virtual currency.', on_delete=django.db.models.deletion.CASCADE, to='fakemoneyd.Currency', verbose_name='currency')),
            ],
            options={
                'verbose_name': 'demo fake money',
                'verbose_name_plural': 'demo fake monies',
            },
        ),
    ]
