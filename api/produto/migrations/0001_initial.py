# Generated by Django 4.2 on 2024-03-05 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('titulo', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
