# Generated by Django 4.2 on 2024-03-05 01:46

from django.db import migrations, models
import produto.validators


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='codigo',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=8, validators=[produto.validators.validar_nao_zero]),
        ),
        migrations.AlterField(
            model_name='produto',
            name='titulo',
            field=models.CharField(max_length=200, validators=[produto.validators.validar_nao_zero]),
        ),
    ]
