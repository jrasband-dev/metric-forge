import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="metric-forge",
    version="0.1.0",
    description="The Ultimate Metric Library",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jrasband-dev/metric-forge",
    author="Jayden Rasband",
    author_email="jayden.rasband@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["metric_forge"],
    include_package_data=True,
    install_requires=["polars"],
)
