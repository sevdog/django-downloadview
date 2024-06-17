"""Tests around project's distribution and packaging."""
import unittest
from pathlib import Path
import importlib.metadata

tests_dir = Path(__file__).parent
project_dir = tests_dir.parent
build_dir = project_dir / "var" / "docs" / "html"


class VersionTestCase(unittest.TestCase):
    """Various checks around project's version info."""

    def get_version(self):
        """Return django_downloadview.__version__."""
        from django_downloadview import __version__

        return __version__

    def test_version_present(self):
        """:PEP:`396` - django_downloadview has __version__ attribute."""
        try:
            self.get_version()
        except ImportError:
            self.fail("django_downloadview package has no __version__.")

    def test_version_match(self):
        """django_downloadview.__version__ matches metadata info."""
        installed_version = importlib.metadata.version("django-downloadview")
        self.assertEqual(
            installed_version,
            self.get_version(),
            "Version mismatch: django_downloadview.__version__ "
            f'is "{self.get_version()}" whereas '
            f'importlib.metadata tells "{installed_version}". '
            "You may need to run ``make develop`` to update the "
            "installed version in development environment."
        )
