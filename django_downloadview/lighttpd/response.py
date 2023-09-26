"""Lighttpd's specific responses."""
from pathlib import Path

from django_downloadview.response import ProxiedDownloadResponse, content_disposition


class XSendfileResponse(ProxiedDownloadResponse):
    "Delegates serving file to Lighttpd via X-Sendfile header."

    def __init__(self, file_path, content_type, basename=None, attachment=True):
        """Return a HttpResponse with headers for Lighttpd X-Sendfile."""
        super(XSendfileResponse, self).__init__(content_type=content_type)
        if attachment:
            self.basename = basename or Path(file_path).name
            self["Content-Disposition"] = content_disposition(self.basename)
        self["X-Sendfile"] = file_path
