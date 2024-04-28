# from django.core.management.base import BaseCommand
# from web.models import MenuCategory, MenuSubcategory
#
#
# class Command(BaseCommand):
#     help = 'Insert menu categories and subcategories'
#
#     def handle(self, *args, **kwargs):
#         MenuCategory.objects.all().delete()
#         categories_names = [
#             'Europeo',
#             'Norteamericano',
#             'Brasilero',
#             'Asiático',
#             'Maq. Pesada',
#             'Motores'
#         ]
#
#         if not MenuCategory.objects.count():
#             for category in categories_names:
#                 MenuCategory.objects.create(name=category)
#
#         eur = MenuCategory.objects.get(name='Europeo')
#         eur_subcategories = [
#             'Ivecum',
#             'Merchedez',
#             'Scanium',
#             'Voltro'
#         ]
#         for subcategory in eur_subcategories:
#             MenuSubcategory.objects.create(name=subcategory, menu_category=eur)
#
#         nor = MenuCategory.objects.get(name='Norteamericano')
#         nor_subcategories = [
#             'Forth',
#             'Freightlinering',
#             'Hendrickdottir',
#             'National',
#             'Barbieworth',
#             'Mackintosh',
#             'Woman'
#         ]
#         for subcategory in nor_subcategories:
#             MenuSubcategory.objects.create(name=subcategory, menu_category=nor)
#
#         bra = MenuCategory.objects.get(name='Brasilero')
#         bra_subcategories = [
#             'Rurale',
#             'Burgswagen'
#         ]
#         for subcategory in bra_subcategories:
#             MenuSubcategory.objects.create(name=subcategory, menu_category=bra)
#
#         asi = MenuCategory.objects.get(name='Asiático')
#         asi_subcategories = [
#             'Blue Dragon',
#             'Nohi',
#             'Shen Long',
#             'Sinowagen'
#         ]
#         for subcategory in asi_subcategories:
#             MenuSubcategory.objects.create(name=subcategory, menu_category=asi)
#
#         maq = MenuCategory.objects.get(name='Maq. Pesada')
#         maq_subcategories = [
#             'Allidottir',
#             'Tomcat',
#             'Caterpiellar',
#             'Dookun',
#             'Dyunhai Cons EQ',
#             'K.P.M.',
#             'John Doe',
#             'Tokatsu',
#             'Liebherren',
#             'Maquinaria y Equipos',
#             'Voltro Const EQU'
#         ]
#         for subcategory in maq_subcategories:
#             MenuSubcategory.objects.create(name=subcategory, menu_category=maq)
#
#         mot = MenuCategory.objects.get(name='Motores')
#         mot_subcategories = [
#             'Cummi ** s',
#             'Frontroit Diesel',
#             'Deux',
#             'WMW',
#             'Rochester'
#         ]
#         for subcategory in mot_subcategories:
#             MenuSubcategory.objects.create(name=subcategory, menu_category=mot)
