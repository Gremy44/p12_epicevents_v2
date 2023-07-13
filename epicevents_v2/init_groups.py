from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

def init_groups():
    # Créer les groupes
    group_sale, created = Group.objects.get_or_create(name='group_sale')
    group_support, created = Group.objects.get_or_create(name='group_support')
    group_gestion, created = Group.objects.get_or_create(name='group_gestion')

    # Récupérer les permissions communes
    app_labels = ['custom_cms_auth', 'customer_management', 'events_management']
    models = ['user', 'client', 'contract', 'event']
    content_types_common = ContentType.objects.filter(app_label__in=app_labels, model__in=models)
    permissions_common = Permission.objects.filter(content_type__in=content_types_common, codename__in=['view_client', 'view_contract', 'view_event'])

    # Associer les permissions communes à tous les groupes
    group_sale.permissions.add(*permissions_common)
    group_support.permissions.add(*permissions_common)
    group_gestion.permissions.add(*permissions_common)

    # Associer les permissions individuelles à chaque groupe
    # Groupe 'group_sale'
    permissions_sale = Permission.objects.filter(content_type__in=content_types_common, codename__in=['add_client', 'change_client', 'change_contract', 'add_event'])
    group_sale.permissions.add(*permissions_sale)

    # Groupe 'group_support'
    permissions_support = Permission.objects.filter(content_type__in=content_types_common, codename='change_event')
    group_support.permissions.add(*permissions_support)

    # Groupe 'group_gestion'
    permissions_gestion = Permission.objects.filter(content_type__in=content_types_common, codename__in=['add_user', 'view_user', 'change_user', 'delete_user', 'add_contract', 'change_contract', 'change_event'])
    group_gestion.permissions.add(*permissions_gestion)

if __name__ == '__main__':
    init_groups()
