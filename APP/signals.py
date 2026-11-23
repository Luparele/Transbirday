import os
from django.db import models, transaction
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


def _delete_file_if_unreferenced(model_class, field_name, file_name, file_path, exclude_pk=None):
    """Remove arquivo do disco apenas se nenhum outro registro do model o referenciar."""
    if not file_name or not file_path:
        return
    qs = model_class.objects.filter(**{field_name: file_name})
    if exclude_pk is not None:
        qs = qs.exclude(pk=exclude_pk)
    if qs.exists():
        return

    def _remove():
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except OSError:
            pass

    transaction.on_commit(_remove)


@receiver(post_delete)
def auto_delete_files_on_delete(sender, instance, **kwargs):
    """Apaga arquivos de FileField/ImageField ao excluir um registro do APP."""
    if sender._meta.app_label != 'APP':
        return
    for field in sender._meta.concrete_fields:
        if isinstance(field, models.FileField):
            file_val = getattr(instance, field.name)
            if file_val and file_val.name:
                try:
                    file_path = file_val.path
                except Exception:
                    continue
                _delete_file_if_unreferenced(sender, field.name, file_val.name, file_path, exclude_pk=instance.pk)


@receiver(pre_save)
def auto_delete_old_file_on_change(sender, instance, **kwargs):
    """Apaga o arquivo anterior do disco quando um FileField é substituído."""
    if sender._meta.app_label != 'APP' or not instance.pk:
        return
    file_fields = [f for f in sender._meta.concrete_fields if isinstance(f, models.FileField)]
    if not file_fields:
        return
    try:
        old_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return

    for field in file_fields:
        old_file = getattr(old_instance, field.name)
        new_file = getattr(instance, field.name)
        old_name = old_file.name if old_file else ''
        new_name = new_file.name if new_file else ''
        if old_name and old_name != new_name:
            try:
                old_path = old_file.path
            except Exception:
                continue
            _delete_file_if_unreferenced(sender, field.name, old_name, old_path, exclude_pk=instance.pk)

