from django.core.files.storage import FileSystemStorage
from django.core.signing import TimestampSigner


class SignedURLMixin:
    """
    Mixin for generating signed file URLs with compatible storage backends.

    Adds X-Signature query parameters to the normal URLs generated by the storage class.
    """

    def url(self, name):
        path = super().url(name)
        signer = TimestampSigner()
        signature = signer.sign(path)
        return f"{path}?X-Signature={signature}"


class SignedFileSystemStorage(SignedURLMixin, FileSystemStorage):
    """
    Specialized filesystem storage that signs file URLs for clients.
    """
