from django.core.management.base import BaseCommand
from web.models import System, Subsystem


class Command(BaseCommand):
    help = 'Insert subsystems'

    def handle(self, *args, **kwargs):
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

        #
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

        #
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

        #
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

        #
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

        #
        com = System.objects.get(name='Complementos')

        com_subsystems = [
            'Accesorios',
            'Elementos de desgaste y gets',
            'Equipos y máquinas',
            'Herramientas'
        ]

        for subsystem in com_subsystems:
            Subsystem.objects.create(name=subsystem, system=com)

        #
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

        #
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

        #
        dir = System.objects.get(name='Dirección')

        dir_subsystems = [
            'Accesorios y componentes',
            'Barras y terminales',
            'Cajas dirección',
            'Servo dirección'
        ]

        for subsystem in dir_subsystems:
            Subsystem.objects.create(name=subsystem, system=dir)

        #
        ejd = System.objects.get(name='Eje delantero')

        ejd_subsystems = [
            'Accesorios y componentes',
            'Barras y soportes',
            'Muñón',
            'Pines y bocinas'
        ]

        for subsystem in ejd_subsystems:
            Subsystem.objects.create(name=subsystem, system=ejd)

        #
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

        #
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

        #
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

        #
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

        #
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

        #
        ilu = System.objects.get(name='Iluminación')

        ilu_subsystems = [
            'Conectores y soquetes',
            'Faros',
            'Focos'
        ]

        for subsystem in ilu_subsystems:
            Subsystem.objects.create(name=subsystem, system=ilu)

        #
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

        #
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

        #
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

        #
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

        #
        qui = System.objects.get(name='Quinta rueta')

        qui_subsystems = [
            'Accesorios y componentes',
            'King ping',
            'Quinta rueda',
            'Tornamesa'
        ]

        for subsystem in qui_subsystems:
            Subsystem.objects.create(name=subsystem, system=qui)

        #
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

        #
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

        #
        tre = System.objects.get(name='Tren de rodamiento')

        tre_subsystems = [
            'Cademas',
            'Misceláneos',
            'Rodillos',
            'Rueda guía',
            'Segmentos y ,sprocket'
            'Zapatas'
        ]

        for subsystem in tre_subsystems:
            Subsystem.objects.create(name=subsystem, system=tre)
