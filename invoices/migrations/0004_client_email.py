# Generated by Django 2.2.3 on 2019-10-11 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0003_remove_invoice_proforma'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(blank=True, max_length=150, null=True),
        ),
    ]