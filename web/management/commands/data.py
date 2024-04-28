from random import randrange, uniform, choice

from django.core.management.base import BaseCommand
from web.models import Brand, System, Subsystem, Product, MenuCategory, MenuSubcategory


class Command(BaseCommand):
    help = 'Inserting data...'

    def handle(self, *args, **kwargs):
        # CREATE CATEGORIES AND SUBCATEGORIES
        MenuCategory.objects.all().delete()
        categories_names = [
            'Europeo',
            'Norteamericano',
            'Brasilero',
            'Asiático',
            'Maq. Pesada',
            'Motores'
        ]

        if not MenuCategory.objects.count():
            for category in categories_names:
                MenuCategory.objects.create(name=category)

        eur = MenuCategory.objects.get(name='Europeo')
        eur_subcategories = [
            'Ivecum',
            'Merchedez',
            'Scanium',
            'Voltro'
        ]
        for subcategory in eur_subcategories:
            MenuSubcategory.objects.create(name=subcategory, menu_category=eur)

        nor = MenuCategory.objects.get(name='Norteamericano')
        nor_subcategories = [
            'Forth',
            'Freightlinering',
            'Hendrickdottir',
            'National',
            'Barbieworth',
            'Mackintosh',
            'Woman'
        ]
        for subcategory in nor_subcategories:
            MenuSubcategory.objects.create(name=subcategory, menu_category=nor)

        bra = MenuCategory.objects.get(name='Brasilero')
        bra_subcategories = [
            'Rurale',
            'Burgswagen'
        ]
        for subcategory in bra_subcategories:
            MenuSubcategory.objects.create(name=subcategory, menu_category=bra)

        asi = MenuCategory.objects.get(name='Asiático')
        asi_subcategories = [
            'Blue Dragon',
            'Nohi',
            'Shen Long',
            'Sinowagen'
        ]
        for subcategory in asi_subcategories:
            MenuSubcategory.objects.create(name=subcategory, menu_category=asi)

        maq = MenuCategory.objects.get(name='Maq. Pesada')
        maq_subcategories = [
            'Allidottir',
            'Tomcat',
            'Caterpiellar',
            'Dookun',
            'Dyunhai Cons EQ',
            'K.P.M.',
            'John Doe',
            'Tokatsu',
            'Liebherren',
            'Maquinaria y Equipos',
            'Voltro Const EQU'
        ]
        for subcategory in maq_subcategories:
            MenuSubcategory.objects.create(name=subcategory, menu_category=maq)

        mot = MenuCategory.objects.get(name='Motores')
        mot_subcategories = [
            'Cummi ** s',
            'Frontroit Diesel',
            'Deux',
            'WMW',
            'Rochester'
        ]
        for subcategory in mot_subcategories:
            MenuSubcategory.objects.create(name=subcategory, menu_category=mot)

        # CREATE BRANDS
        Brand.objects.all().delete()
        brands_names = [
            'Bosch',
            'CEI',
            'Cosibo',
            'Elring',
            'ETNA',
            'FAG',
            'Febi',
            'Fleetguard',
            'Fras - le',
            'Futura',
            'Hengst',
            'Kaçmazlar',
            'Knorr Bremse',
            'Kolbenschmidt',
            'LASO',
            'MAHLE',
            'Mann - Filter',
            'Molas Obenaus',
            'Rota',
            'SACHS',
            'SAMPA',
            'SKF',
            'SLP',
            'SM Motorenteile GmbH',
            'Spare Parts',
            'Susin Francescutti',
            'Total',
            'WABCO',
            'Victor Reinz'
        ]

        if not Brand.objects.count():
            for brands_name in brands_names:
                Brand.objects.create(name=brands_name)

        # CREATE SYSTEMS AND SUBSYSTEMS
        Subsystem.objects.all().delete()
        system_names = [
            'Caja de cambios',
            'Cardan',
            'Carreta',
            'Carrocería',
            'Complementos',
            'Corona',
            'Cubos y ruedas',
            'Dirección',
            'Eje delantero',
            'Eje posterior',
            'Embrague',
            'Filtración',
            'Frenos',
            'Hidraúlico',
            'Iluminación',
            'Instrumentación y eléctrico',
            'Lubricante',
            'Misceláneos',
            'Motor',
            'Quinta rueta',
            'Suspensión',
            'Transmisión',
            'Tren de rodamiento'
        ]

        if not System.objects.count():
            for system_name in system_names:
                System.objects.create(name=system_name)

        cdc = System.objects.get(name='Caja de cambios')

        cdc_subsystems = [
            'Accesorios y componentes',
            'Empaquetaduras, retes y orings',
            'Ishift',
            'Lubiración',
            'Palanca y cables',
            'Piñones y ejes',
            'Retardador',
            'Rodajes',
            'Selector',
            'Selector super marcha',
            'Sensores, módulos y actuadores',
            'Sincronizadores',
            'Toma fuerza',
            'Válculas'
        ]

        for subsystem in cdc_subsystems:
            Subsystem.objects.create(name=subsystem, system=cdc)

        car = System.objects.get(name='Cardan')

        car_subsystems = [
            'Accesorios y componentes',
            'Crucetas',
            'Eje completo y/o parcial',
            'Soportes',
            'Yugos y bridas'
        ]

        for subsystem in car_subsystems:
            Subsystem.objects.create(name=subsystem, system=car)

        crr = System.objects.get(name='Carreta')

        crr_subsystems = [
            'Accesorios y componentes',
            'Bocamaza',
            'Eje americano',
            'Eje europeo',
            'Paquete muelle',
            'Suspensión mecánica',
            'Suspensión neumática'
        ]

        for subsystem in crr_subsystems:
            Subsystem.objects.create(name=subsystem, system=crr)

        crc = System.objects.get(name='Carrocería')

        crc_subsystems = [
            'Accesorios y componentes',
            'Admisión y escape',
            'Aire acondicionado',
            'Cabina',
            'Depósitos y tapas',
            'Emblemas',
            'Espejos y soportes',
            'Limpiaparabrisas',
            'Parachoque y guardabarro',
            'Puertas y levalunas',
            'Refrigeración'
        ]

        for subsystem in crc_subsystems:
            Subsystem.objects.create(name=subsystem, system=crc)

        com = System.objects.get(name='Complementos')

        com_subsystems = [
            'Accesorios',
            'Elementos de desgaste y gets',
            'Equipos y máquinas',
            'Herramientas'
        ]

        for subsystem in com_subsystems:
            Subsystem.objects.create(name=subsystem, system=com)

        cor = System.objects.get(name='Corona')

        cor_subsystems = [
            'Accesorios y componentes',
            'Diferencial',
            'Ejes y semiejes',
            'Empaquetaduras, retenes y orings',
            'Piñón y corona',
            'Reenvío',
            'Rodajes',
            'Sensores, módulos y actuadores',
            'Válvulas'
        ]

        for subsystem in cor_subsystems:
            Subsystem.objects.create(name=subsystem, system=cor)

        cyr = System.objects.get(name='Cubos y ruedas')

        cyr_subsystems = [
            'Accesorios y componentes',
            'Aros',
            'Cubos',
            'Empaquetaduras, retenes y orings',
            'Pernos y tuercas',
            'Rodajes'
        ]

        for subsystem in cyr_subsystems:
            Subsystem.objects.create(name=subsystem, system=cyr)

        dcc = System.objects.get(name='Dirección')

        dir_subsystems = [
            'Accesorios y componentes',
            'Barras y terminales',
            'Cajas dirección',
            'Servo dirección'
        ]

        for subsystem in dir_subsystems:
            Subsystem.objects.create(name=subsystem, system=dcc)

        ejd = System.objects.get(name='Eje delantero')

        ejd_subsystems = [
            'Accesorios y componentes',
            'Barras y soportes',
            'Muñón',
            'Pines y bocinas'
        ]

        for subsystem in ejd_subsystems:
            Subsystem.objects.create(name=subsystem, system=ejd)

        eps = System.objects.get(name='Eje posterior')

        eps_subsystems = [
            'Accesorios y componentes',
            'Bujes y bocinas',
            'Funda',
            'Puente',
            'Soportes'
        ]

        for subsystem in eps_subsystems:
            Subsystem.objects.create(name=subsystem, system=eps)

        emb = System.objects.get(name='Embrague')

        emb_subsystems = [
            'Accesorios y componentes',
            'Collarín',
            'Disco',
            'Kit de embrague',
            'Plato de embrague',
            'Servos y bombín'
        ]

        for subsystem in emb_subsystems:
            Subsystem.objects.create(name=subsystem, system=emb)

        fil = System.objects.get(name='Filtración')

        fil_subsystems = [
            'Admisión aire',
            'Aire acondicionado',
            'Cumbustible',
            'Escape, úrea aut.',
            'Lubriración caja cambios',
            'Lubriración motor',
            'Refrigeración motor',
            'Secador de aire',
            'Servo de dirección',
            'Transmisión, hidraúlico'
        ]

        for subsystem in fil_subsystems:
            Subsystem.objects.create(name=subsystem, system=fil)

        fre = System.objects.get(name='Frenos')

        fre_subsystems = [
            'Accesorios y componentes',
            'Cilindro accionamiento',
            'Compresor de aire',
            'Discos y tambores',
            'Mecanismo frenado',
            'Pastillas y zapatas',
            'Secador de aire',
            'Sensores, módulos y actuadores',
            'Válculas freno'
        ]

        for subsystem in fre_subsystems:
            Subsystem.objects.create(name=subsystem, system=fre)

        hid = System.objects.get(name='Hidraúlico')

        hid_subsystems = [
            'Cilindros',
            'Empaquetaduras, retenes y orings',
            'Mangueras',
            'Mecanismo de levante',
            'Misceláneos'
        ]

        for subsystem in hid_subsystems:
            Subsystem.objects.create(name=subsystem, system=hid)

        ilu = System.objects.get(name='Iluminación')

        ilu_subsystems = [
            'Conectores y soquetes',
            'Faros',
            'Focos'
        ]

        for subsystem in ilu_subsystems:
            Subsystem.objects.create(name=subsystem, system=ilu)

        ins = System.objects.get(name='Instrumentación y eléctrico')

        ins_subsystems = [
            'Accesorios y componentes',
            'Alternador',
            'Arranque',
            'Batería',
            'Equipamientos',
            'Relés y Fusibles',
            'Sensores, módulos y switchs',
            'Tableros e instrumentos'
        ]

        for subsystem in ins_subsystems:
            Subsystem.objects.create(name=subsystem, system=ins)

        lub = System.objects.get(name='Lubricante')

        lub_subsystems = [
            'Aceite caja',
            'Aceite corona',
            'Aceite motor',
            'Aceite transmisión',
            'Aceites y quimicos especiales',
            'Grasa de rodaje y chasis',
            'Líquido de frenos',
            'Refrigerantes',
        ]

        for subsystem in lub_subsystems:
            Subsystem.objects.create(name=subsystem, system=lub)

        mis = System.objects.get(name='Misceláneos')

        mis_subsystems = [
            'Abrazadoeras',
            'Limpiadores',
            'Múltiples',
            'Pernos y tuercas',
            'Rodajes y retenes'
        ]

        for subsystem in mis_subsystems:
            Subsystem.objects.create(name=subsystem, system=mis)

        mot = System.objects.get(name='Motor')

        mot_subsystems = [
            'Accesorios y componentes',
            'Admisión y escape',
            'Combustuble e inyección',
            'Culata',
            'Eléctrico, encendido motor',
            'Empaquetaduras, retenes y orings',
            'Fajas y templadores',
            'Lubricación',
            'Monoblock',
            'Refrigeración',
            'Sensores, módulos y actuadores',
            'Soportes'
        ]

        for subsystem in mot_subsystems:
            Subsystem.objects.create(name=subsystem, system=mot)

        qui = System.objects.get(name='Quinta rueta')

        qui_subsystems = [
            'Accesorios y componentes',
            'King ping',
            'Quinta rueda',
            'Tornamesa'
        ]

        for subsystem in qui_subsystems:
            Subsystem.objects.create(name=subsystem, system=qui)

        com = System.objects.get(name='Suspensión')

        sus_subsystems = [
            'Accesorios y componentes',
            'Amortiguadores',
            'Barras y bujes',
            'Bogie',
            'Bolsas',
            'Cabina',
            'Muelles',
            'Sensores, módulos y actuadores',
            'Válvulas'
        ]

        for subsystem in sus_subsystems:
            Subsystem.objects.create(name=subsystem, system=com)

        tra = System.objects.get(name='Transmisión')

        tra_subsystems = [
            'Accesorios y componentes',
            'Discos',
            'Empaquetaduras, retenes y orings',
            'Lubricación',
            'Piñones y ejes',
            'Rodajes',
            'Selectores',
            'Sensores, módulos y actuadores'
        ]

        for subsystem in tra_subsystems:
            Subsystem.objects.create(name=subsystem, system=tra)

        tre = System.objects.get(name='Tren de rodamiento')

        tre_subsystems = [
            'Cademas',
            'Misceláneos',
            'Rodillos',
            'Rueda guía',
            'Segmentos y sprocket',
            'Zapatas'
        ]

        for subsystem in tre_subsystems:
            Subsystem.objects.create(name=subsystem, system=tre)

        # CREATE PRODUCTS
        Product.objects.all().delete()
        systems_1 = {
            'Caja de cambios': {
                'subsystems': [
                    'Accesorios y componentes',
                    'Empaquetaduras, retes y orings',
                    'Ishift',
                    'Lubiración',
                    'Palanca y cables',
                    'Piñones y ejes',
                    'Retardador',
                    'Rodajes',
                    'Selector',
                    'Selector super marcha',
                    'Sensores, módulos y actuadores',
                    'Sincronizadores',
                    'Toma fuerza',
                    'Válculas'
                ]
            },
        }
        systems_2 = {
            'Cardan': {
                'subsystems': [
                    'Accesorios y componentes',
                    'Crucetas',
                    'Eje completo y/o parcial',
                    'Soportes',
                    'Yugos y bridas'
                ]
            },
        }
        systems_3 = {
            'Carreta': {
                'subsystems': [
                    'Accesorios y componentes',
                    'Bocamaza',
                    'Eje americano',
                    'Eje europeo',
                    'Paquete muelle',
                    'Suspensión mecánica',
                    'Suspensión neumática'
                ]
            },
        }
        systems_4 = {
            'Carrocería': {
                'subsystems': [
                    'Accesorios y componentes',
                    'Admisión y escape',
                    'Aire acondicionado',
                    'Cabina',
                    'Depósitos y tapas',
                    'Emblemas',
                    'Espejos y soportes',
                    'Limpiaparabrisas',
                    'Parachoque y guardabarro',
                    'Puertas y levalunas',
                    'Refrigeración'
                ]
            },
        }
        systems_5 = {
            'Complementos': {
                'subsystems': [
                    'Accesorios',
                    'Elementos de desgaste y gets',
                    'Equipos y máquinas',
                    'Herramientas'
                ]
            },
        }
        systems_6 = {
            'Corona': {
                'subsystems': [
                    'Accesorios y componentes',
                    'Diferencial',
                    'Ejes y semiejes',
                    'Empaquetaduras, retenes y orings',
                    'Piñón y corona',
                    'Reenvío',
                    'Rodajes',
                    'Sensores, módulos y actuadores',
                    'Válvulas'
                ]
            },
        }
        systems_7 = {
            'Cubos y ruedas': {
                'subsystems': [
                    'Accesorios y componentes',
                    'Aros',
                    'Cubos',
                    'Empaquetaduras, retenes y orings',
                    'Pernos y tuercas',
                    'Rodajes'
                ]
            },
        }
        systems_8 = {
            'Dirección': {
                'subsystems': [
                    'Accesorios y componentes',
                    'Barras y terminales',
                    'Cajas dirección',
                    'Servo dirección'
                ]
            },
        }
        systems_9 = {
            'Eje delantero': {
                'subsystems': [
                    'Accesorios y componentes',
                    'Barras y soportes',
                    'Muñón',
                    'Pines y bocinas'
                ]
            },
        }
        systems_10 = {
            'Eje posterior': {
                'subsystems': [
                    'Accesorios y componentes',
                    'Bujes y bocinas',
                    'Funda',
                    'Puente',
                    'Soportes'
                ]
            },
        }
        systems_11 = {
            'Embrague': {
                'subsystems': [
                    'Accesorios y componentes',
                    'Collarín',
                    'Disco',
                    'Kit de embrague',
                    'Plato de embrague',
                    'Servos y bombín'
                ]
            },
        }
        systems_12 = {
            'Filtración': {
                'subsystems': [
                    'Admisión aire',
                    'Aire acondicionado',
                    'Cumbustible',
                    'Escape, úrea aut.',
                    'Lubriración caja cambios',
                    'Lubriración motor',
                    'Refrigeración motor',
                    'Secador de aire',
                    'Servo de dirección',
                    'Transmisión, hidraúlico'
                ]
            },
        }
        systems_13 = {
            'Frenos': {
                'subsystems': [
                    'Accesorios y componentes',
                    'Cilindro accionamiento',
                    'Compresor de aire',
                    'Discos y tambores',
                    'Mecanismo frenado',
                    'Pastillas y zapatas',
                    'Secador de aire',
                    'Sensores, módulos y actuadores',
                    'Válculas freno'
                ]
            },
        }
        systems_14 = {
            'Hidraúlico': {
                'subsystems': [
                    'Cilindros',
                    'Empaquetaduras, retenes y orings',
                    'Mangueras',
                    'Mecanismo de levante',
                    'Misceláneos'
                ]
            },
        }
        systems_15 = {
            'Iluminación': {
                'subsystems': [
                    'Conectores y soquetes',
                    'Faros',
                    'Focos'
                ]
            },
        }
        systems_16 = {
            'Instrumentación y eléctrico': {
                'subsystems': [
                    'Accesorios y componentes',
                    'Alternador',
                    'Arranque',
                    'Batería',
                    'Equipamientos',
                    'Relés y Fusibles',
                    'Sensores, módulos y switchs',
                    'Tableros e instrumentos'
                ]
            },
        }
        systems_17 = {
            'Lubricante': {
                'subsystems': [
                    'Aceite caja',
                    'Aceite corona',
                    'Aceite motor',
                    'Aceite transmisión',
                    'Aceites y quimicos especiales',
                    'Grasa de rodaje y chasis',
                    'Líquido de frenos',
                    'Refrigerantes',
                ]
            },
        }
        systems_18 = {
            'Misceláneos': {
                'subsystems': [
                    'Abrazadoeras',
                    'Limpiadores',
                    'Múltiples',
                    'Pernos y tuercas',
                    'Rodajes y retenes'
                ]
            },
        }
        systems_19 = {
            'Motor': {
                'subsystems': [
                    'Accesorios y componentes',
                    'Admisión y escape',
                    'Combustuble e inyección',
                    'Culata',
                    'Eléctrico, encendido motor',
                    'Empaquetaduras, retenes y orings',
                    'Fajas y templadores',
                    'Lubricación',
                    'Monoblock',
                    'Refrigeración',
                    'Sensores, módulos y actuadores',
                    'Soportes'
                ]
            },
        }
        systems_20 = {
            'Quinta rueta': {
                'subsystems': [
                    'Accesorios y componentes',
                    'King ping',
                    'Quinta rueda',
                    'Tornamesa'
                ]
            },
        }
        systems_21 = {
            'Suspensión': {
                'subsystems': [
                    'Accesorios y componentes',
                    'Amortiguadores',
                    'Barras y bujes',
                    'Bogie',
                    'Bolsas',
                    'Cabina',
                    'Muelles',
                    'Sensores, módulos y actuadores',
                    'Válvulas'
                ]
            },
        }
        systems_22 = {
            'Transmisión': {
                'subsystems': [
                    'Accesorios y componentes',
                    'Discos',
                    'Empaquetaduras, retenes y orings',
                    'Lubricación',
                    'Piñones y ejes',
                    'Rodajes',
                    'Selectores',
                    'Sensores, módulos y actuadores'
                ]
            },
        }
        systems_23 = {
            'Tren de rodamiento': {
                'subsystems': [
                    'Cademas',
                    'Misceláneos',
                    'Rodillos',
                    'Rueda guía',
                    'Segmentos y sprocket'
                    'Zapatas'
                ]
            }
        }
        names = [
            'neque',
            'porro',
            'quisquam',
            'est',
            'qui',
            'dolorem',
            'ipsum',
            'quia',
            'dolor,'
            'sit',
            'amet',
            'consectetur',
            'adipisci',
            'velit'
        ]
        descriptions = [
            'Quisque pellentesque quam nec eleifend efficitur',
            'Nullam in diam vitae ipsum iaculis congue',
            'Maecenas pharetra erat sit amet iaculis bibendum',
            'Aenean id metus vel sem tristique blandit non sit amet ex',
            'Mauris tempor lorem quis lectus suscipit eleifend',
            'Vivamus non eros vitae leo porta sollicitudin',
            'Curabitur dapibus quam vitae nisl rhoncus, id accumsan nunc vehicula',
            'Phasellus volutpat lectus eget erat hendrerit eleifend',
            'Sed placerat nibh id quam tempor, in interdum ligula convallis',
            'Donec id sem vel turpis ultricies ullamcorper eget a sem',
            'Pellentesque tincidunt metus aliquam eros lacinia, ut fermentum velit molestie',
            'Morbi vestibulum erat at viverra consequat',
            'Morbi sed dui consequat, congue felis ac, porta massa',
            'Quisque a est eu leo finibus bibendum'
        ]
        s = 24
        subsystem_id = 1478

        # TODO, Cambiar esto para que haga un for indexado por cada system y asi evitar que los nombres de los
        #  subsystemas se repitan

        for system_id, system_info in systems_1.items():
            for key in system_info:
                for subsystem in system_info[key]:
                    get_price = round(uniform(1.90, 299.0), 2)
                    for i in range(randrange(20, 30, 1)):
                        print('')
                        print('Brand: ', Brand.objects.get(name=choice(brands_names)))
                        print('Name: ', choice(names) + ' ' + choice(names) + ' ' + str(randrange(1, 9, 1)) +
                              str(randrange(1, 9, 1)))
                        print('Code: ', 'S' + str(s) + 'SUB' + str(subsystem_id) +
                              str(randrange(1, 9, 1)) +
                              str(randrange(1, 9, 1)) +
                              str(randrange(1, 9, 1)) +
                              str(randrange(1, 9, 1)))
                        print('Price no offer: ', round(get_price - (get_price * 0.05)))
                        print('Price: ', get_price)
                        print('Picture: https://picsum.photos/500/500')
                        print('Description: ',
                              choice(descriptions) + ' ' + choice(descriptions) + ' ' + choice(descriptions))
                        print('Stock: ', randrange(10, 70, 1))
                        print('System: ', System.objects.get(name=system_id))
                        print('Subsystem: ', Subsystem.objects.get(pk=subsystem_id))
                    subsystem_id = subsystem_id + 1
