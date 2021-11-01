#!/usr/bin/env python3
from distutils.core import setup

version = "0.2"

scripts = ["bin/home-assistant-desktop-receiver"]

data_files = [('/etc/xdg/autostart', ["data/home-assistant-desktop-receiver.desktop"])]

setup(name='home-assistant-desktop-receiver',
        version=version,
        description='Desktop Client for Home Assistant',
        long_description='Acts as a sensor (or switch) for HA operation',
        license='GPLv2',
        author='David Edmundson',
        author_email='david@davidedmundson.co.uk',
        url='https://github.com/davidedmundson/home-assistant-desktop-receiver',
        scripts=scripts,
        platforms='any',
        data_files = data_files)
