# Generated by Django 4.0.3 on 2022-03-28 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Knapsack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.IntegerField(default=0.0, verbose_name='体积')),
                ('worth', models.IntegerField(default=0.0, verbose_name='价值')),
            ],
            options={
                'verbose_name': '背包数据',
                'verbose_name_plural': '背包数据',
                'ordering': ('id',),
            },
        ),
    ]
