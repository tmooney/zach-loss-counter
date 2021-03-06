# Generated by Django 2.1.3 on 2018-11-13 19:26

import bets.enums
from django.db import migrations, models
import enumchoicefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('wager', models.TextField()),
                ('bettor', models.CharField(max_length=100)),
                ('opponent', models.CharField(max_length=100)),
                ('deadline', models.DateTimeField(verbose_name='end date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='bet made date')),
                ('outcome', enumchoicefield.fields.EnumChoiceField(blank=True, enum_class=bets.enums.BetResultChoice, max_length=1)),
                ('state', enumchoicefield.fields.EnumChoiceField(default=bets.enums.BetStateChoice(2), enum_class=bets.enums.BetStateChoice, max_length=1)),
            ],
        ),
    ]
