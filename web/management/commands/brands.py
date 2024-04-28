# from django.core.management.base import BaseCommand
# from web.models import Brand
#
#
# class Command(BaseCommand):
#     help = 'Insert brands'
#
#     def handle(self, *args, **kwargs):
#         Brand.objects.all().delete()
#         brands_names = [
#             'Bosch',
#             'CEI',
#             'Cosibo',
#             'Elring',
#             'ETNA',
#             'FAG',
#             'Febi',
#             'Fleetguard',
#             'Fras - le',
#             'Futura',
#             'Hengst',
#             'Kaçmazlar',
#             'Knorr Bremse',
#             'Kolbenschmidt',
#             'LASO',
#             'MAHLE',
#             'Mann - Filter',
#             'Molas Obenaus',
#             'Rota',
#             'SACHS',
#             'SAMPA',
#             'SKF',
#             'SLP',
#             'SM Motorenteile GmbH',
#             'Spare Parts',
#             'Susin Francescutti',
#             'Total',
#             'WABCO',
#             'Victor Reinz'
#         ]
#
#         if not Brand.objects.count():
#             for brands_name in brands_names:
#                 Brand.objects.create(name=brands_name)
