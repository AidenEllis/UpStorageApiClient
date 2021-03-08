from setuptools import setup, find_packages
import os
import setuptools
import subprocess

project_version = subprocess.run(['git', 'describe', '--tags'], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()
assert "." in project_version

assert os.path.isfile("UpStorageApiClient/version.py")
with open("UpStorageApiClient/VERSION", "w", encoding="utf-8") as fh:
    fh.write(f"{project_version}\n")


def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()


# Setting up
setup(
    name="UpStorageApiClient",
    version=project_version,
    author="Sakib (Florian Dedov)",
    author_email="<mail@neuralnine.com>",
    long_description_content_type="text/markdown",
    long_description=read_file('README.md'),
    description='UpStorage Api Client.',
    packages=find_packages(),
    url='https://github.com/QuackCoding/UpStorageApiClient',
    package_data={'UpStorageApiClient': ['VERSION']},
    install_requires=['requests'],
    keywords=['python', 'storage', 'api', 'upstorage', 'UpStorageApiClient'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)