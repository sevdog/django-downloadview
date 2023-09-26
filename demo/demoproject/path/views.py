from pathlib import Path

from django_downloadview import PathDownloadView

# Let's initialize some fixtures.
app_dir = Path(__file__).parent
project_dir = app_dir.parent
fixtures_dir = project_dir / "fixtures"
#: Path to a text file that says 'Hello world!'.
hello_world_path = fixtures_dir / "hello-world.txt"

#: Serve ``fixtures/hello-world.txt`` file.
static_path = PathDownloadView.as_view(path=hello_world_path)


class DynamicPathDownloadView(PathDownloadView):
    """Serve file in ``settings.MEDIA_ROOT``.

    .. warning::

       Make sure to prevent "../" in path via URL patterns.

    .. note::

       This particular setup would be easier to perform with
       :class:`StorageDownloadView`

    """

    def get_path(self):
        """Return path inside fixtures directory."""
        # Get path from URL resolvers or as_view kwarg.
        relative_path = super().get_path()
        # Make it absolute.
        absolute_path = fixtures_dir / relative_path
        return absolute_path


dynamic_path = DynamicPathDownloadView.as_view()
