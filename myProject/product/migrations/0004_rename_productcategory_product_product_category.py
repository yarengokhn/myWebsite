# Generated by Django 5.1.2 on 2024-11-12 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_category_create_at_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='productCategory',
            new_name='product_category',
        ),
    ]
