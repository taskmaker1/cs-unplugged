"""Module for the custom Django loadresources command."""

from django.core.management.base import BaseCommand
from django.conf import settings
from utils.LoaderFactory import LoaderFactory


class Command(BaseCommand):
    """Required command class for the custom Django loadresources command."""

    help = "Reads resource data and adds to database"

    def handle(self, *args, **options):
        """Automatically called when the loadresources command is given."""
        base_path = settings.RESOURCES_CONTENT_BASE_PATH
        resource_structure_file = "resources.yaml"
        factory = LoaderFactory()

        factory.create_resources_loader(
            structure_filename=resource_structure_file,
            base_path=base_path
        ).load()
