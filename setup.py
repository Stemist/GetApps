from setuptools import setup, find_packages

setup(
    name="GetApps",
    version="0.1",
    packages=find_packages(),
    scripts=['get_apps.py'],
    platforms='any'

    # Project uses os and wget. Ensure these dependencies get installed.
    install_requires=['wget', 'os'],

    # Metadata.
    author="Christian Pearson",
    description="Tool for Computer Service Technicians to aid downloading basic applications on workstation or user computers.",
    url="https://github.com/Stemist/GetApps.git"
)