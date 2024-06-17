"""Serve files with Django and reverse proxies."""
import importlib.metadata
from django_downloadview.api import *  # NoQA

#: Module version, as defined in PEP-0396.
__version__ = importlib.metadata.version(__package__.replace("-", "_"))
