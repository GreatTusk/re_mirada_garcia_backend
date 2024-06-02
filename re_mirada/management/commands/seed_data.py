from django.core.management.base import BaseCommand

from re_mirada.models import PlanFoto, Servicios


class Command(BaseCommand):
    help = 'Seeds the database with PlanFoto and Servicios data'

    def handle(self, *args, **options):
        # Define the data
        plans_data = [
            {
                "id": "1",
                "titulo": "Plan Xpress",
                "precio": 260000,
                "incluye": [
                    "Sesión documental del evento",
                    "Edición profesional de las fotografías",
                    "Entrega de 100 fotografías digitales en alta resolución",
                    "2 horas de cobertura",
                ],
                "no_incluye": [
                    "Fotógrafo adicional",
                    "Sesión artística en exteriores",
                    "Sesión pre-evento",
                    "Fotografías originales sin editar",
                ],
            },
            {
                "id": "2",
                "titulo": "Plan Petite",
                "precio": 480000,
                "incluye": [
                    "Sesión documental del evento",
                    "Sesión artística en exteriores",
                    "Edición profesional de las fotografías",
                    "Entrega de 200 fotografías digitales en alta resolución",
                    "Fotógrafo adicional",
                    "4 horas de cobertura",
                ],
                "no_incluye": [
                    "Sesión pre-evento",
                    "Fotografías originales sin editar",
                ],
            },
            {
                "id": "3",
                "titulo": "Plan Plus",
                "precio": 1550000,
                "incluye": [
                    "Sesión documental desde los preparativos hasta la celebración del evento",
                    "Sesión artística en exteriores",
                    "Edición profesional de las fotografías",
                    "Entrega de 650 fotografías digitales en alta resolución",
                    "2 Fotógrafos adicionales",
                    "10 horas de cobertura",
                    "Fotografías originales sin editar",
                ],
                "no_incluye": [],
            },
        ]

        # Create the PlanFoto and Servicios instances
        for plan_data in plans_data:
            incluye = Servicios()
            incluye.set_servicios(plan_data['incluye'])
            incluye.save()

            no_incluye = Servicios()
            no_incluye.set_servicios(plan_data['no_incluye'])
            no_incluye.save()

            PlanFoto.objects.create(
                id=plan_data['id'],
                titulo=plan_data['titulo'],
                precio=plan_data['precio'],
                incluye=incluye,
                no_incluye=no_incluye,
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))
