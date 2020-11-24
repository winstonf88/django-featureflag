from setuptools import find_packages, setup

version = "0.0"

setup(
    name="django_featureflag",
    version=version,
    description="",
    long_description="",
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords="",
    author="",
    author_email="",
    url="",
    license="",
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=["django"],
    extras_require={"dev": ["pytest", "pytest-django", "pytest-mock", "factory-boy"]},
    entry_points="""
        # -*- Entry points: -*-
    """,
)
