from django.contrib.auth.management.commands.createsuperuser import Command as CreateSuperUserCommand
from django.core.management import CommandError


class Command(CreateSuperUserCommand):
    def handle(self, *args, **options):
        first_name = options.get('first_name')
        last_name = options.get('last_name')
        if not first_name or not last_name:
            raise CommandError("You must provide first_name and last_name.")
        super().handle(*args, **options)

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument('--first_name', type=str,
                            help='First name of the superuser')
        parser.add_argument('--last_name', type=str,
                            help='Last name of the superuser')

    def get_input_data(self, *args, **options):
        data = super().get_input_data(*args, **options)
        first_name = options.get('first_name') or input('First name: ')
        last_name = options.get('last_name') or input('Last name: ')
        data['first_name'] = first_name
        data['last_name'] = last_name
        return data
