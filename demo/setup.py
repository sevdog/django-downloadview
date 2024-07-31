from pathlib import Path
from setuptools import setup

here = Path(__file__).parent.absolute()

setup(
    name="django-downloadview-demo",
    version="1.0",
    description="Serve files with Django and reverse-proxies.",
    long_description=(here / "README.rst").open().read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Framework :: Django",
    ],
    author="Benoît Bryon",
    author_email="benoit@marmelune.net",
    url="https://django-downloadview.readthedocs.io/",
    license="BSD",
    packages=["demoproject"],
    include_package_data=True,
    zip_safe=False,
    install_requires=["django-downloadview", "pytest-django"],
    entry_points={"console_scripts": ["demo = demoproject.manage:main"]},
)
