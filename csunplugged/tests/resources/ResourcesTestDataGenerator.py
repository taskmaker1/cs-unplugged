"""Create test data for resource tests."""

from resources.models import Resource


class ResourcesTestDataGenerator:
    """Class for generating test data for resource tests."""

    def create_resource(self, slug, name, webpage_template, generator_module):
        """Create resource object.

        Args:
            slug: Resource slug (str).
            name: Resource name (str).
            webpage_template: Path to HTML form template (str).
            generator_module: Resource generator class filename (str).

        Returns:
            Resource object.
        """
        resource = Resource(
            slug="resource-{}".format(slug),
            name="Resource {}".format(name),
            webpage_template=webpage_template,
            generator_module=generator_module,
            thumbnail_static_path="static/images/thumbnail-{}".format(slug),
            copies=False,
        )
        resource.save()
        return resource
