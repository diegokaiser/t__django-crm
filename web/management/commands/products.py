from random import randrange, uniform, choice

from django.core.management.base import BaseCommand

from web.management.commands import systems
from web.models import Product, Brand, System, Subsystem


class Command(BaseCommand):
    help = 'Insert products'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        brands = [
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
        # 25
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
        # 26
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
        # 27
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
        # 28
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
        # 29
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
        # 30
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
        # 31
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
        # 32
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
        # 33
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
        # 34
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
        # 35
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
        # 36
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
        # 37
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
        # 38
        systems_15 = {
            'Iluminación': {
                'subsystems': [
                    'Conectores y soquetes',
                    'Faros',
                    'Focos'
                ]
            },
        }
        # 39
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
        # 40
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
        # 41
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
        # 42
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
        # 43
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
        # 4$
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
        # 45
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
        # 46
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
        s = 46
        subsystem_id = 1634

        for system_id, system_info in systems_23.items():
            for key in system_info:
                for subsystem in system_info[key]:
                    for i in range(randrange(5, 35, 1)):
                        get_price = round(uniform(1.90, 299.0), 2)
                        Product.objects.create(
                            brand=Brand.objects.get(name=choice(brands)),
                            name=choice(names) + ' ' + choice(names) + ' ' + str(randrange(1, 9, 1)) +
                                 str(randrange(1, 9, 1)),
                            code='S' + str(s) + 'SUB' + str(subsystem_id) +
                                 str(randrange(1, 9, 1)) +
                                 str(randrange(1, 9, 1)) +
                                 str(randrange(1, 9, 1)) +
                                 str(randrange(1, 9, 1)),
                            price_no_offer=round(get_price - (get_price * 0.05)),
                            price=get_price,
                            picture='https://picsum.photos/500/500',
                            description=choice(descriptions) + ' ' + choice(descriptions) + ' ' + choice(descriptions),
                            stock=randrange(10, 70, 1),
                            system=System.objects.get(name=system_id),
                            subsystem=Subsystem.objects.get(id=subsystem_id)
                        )
                        # print('Inserting:', i)
                        # print('Product :', subsystem_id)
                        # print('Brand: ', Brand.objects.get(name=choice(brands)))
                        # print('Name: ', choice(names) + ' ' + choice(names) + ' ' + str(randrange(1, 9, 1)) +
                        #       str(randrange(1, 9, 1)))
                        # print('Code: ', 'S' + str(s) + 'SUB' + str(subsystem_id) +
                        #       str(randrange(1, 9, 1)) +
                        #       str(randrange(1, 9, 1)) +
                        #       str(randrange(1, 9, 1)) +
                        #       str(randrange(1, 9, 1)))
                        # print('Price no offer: ', round(get_price - (get_price * 0.05)))
                        # print('Price: ', get_price)
                        # print('Picture: https://picsum.photos/500/500')
                        # print('Description: ',
                        #       choice(descriptions) + ' ' + choice(descriptions) + ' ' + choice(descriptions))
                        # print('Stock: ', randrange(10, 70, 1))
                        # print('System: ', System.objects.get(name=system_id))
                        # print('Subsystem: ', Subsystem.objects.get(id=subsystem_id))
                        # print('')
                        # print('')
                    subsystem_id = subsystem_id + 1
        print('Done! Inserted products in system', s)
