from setuptools import setup, find_packages
import os
import codecs


def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()


VERSION = '0.4'

# Setting up
setup(
    name="UpStorageApiClient",
    version=VERSION,
    author="Sakib (Florian Dedov)",
    author_email="<mail@neuralnine.com>",
    long_description_content_type="text/markdown",
    long_description=read_file('README.md'),
    description='UpStorage Api Client.',
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'storage', 'api', 'upstorage', 'UpStorageApiClient'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)