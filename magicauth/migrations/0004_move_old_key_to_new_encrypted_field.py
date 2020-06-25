# Generated by Django 2.2.13 on 2020-06-25 13:59

from django.db import migrations


def forwards_encrypted_key(apps, schema_editor):
    MagicToken = apps.get_model("magicauth", "MagicToken")
    for token in MagicToken.objects.all():
        token.key = token.old_key
        token.save(update_fields=["key"])


def reverse_encrypted_key(apps, schema_editor):
    MagicToken = apps.get_model("magicauth", "MagicToken")
    for token in MagicToken.objects.all():
        token.old_key = token.key
        token.save(update_fields=["old_key"])


class Migration(migrations.Migration):

    dependencies = [
        ('magicauth', '0003_add_encrypted_key'),
    ]

    operations = [
        migrations.RunPython(forwards_encrypted_key, reverse_encrypted_key),
    ]