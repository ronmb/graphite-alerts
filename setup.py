#!/usr/bin/env python
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def run_setup():
    setup(
        name='graphitealerts',
        version='0.0.1',
        description='',
        keywords = '',
        url='http://github.com/ronmb/graphite-alerts',
        author='Aybars Badur',
        author_email='aybars.badur@gmail.com',
        license='BSD',
        # packages=['graphitealerts'],
        install_requires=[
            'Jinja2==2.6',
            'PyYAML==3.10',
            'distribute==0.6.28',
            'pagerduty==0.2.1',
            'redis==2.6.2',
            'requests==0.14.0',
            'python-simple-hipchat==0.1',
        ],
        test_suite='tests',
        # long_description=read('README.md'),
        entry_points="""
        [console_scripts]
        graphite-alerts=graphitealerts.worker:run
        alerts-dev-server=graphitealerts.app:run
        """,
    )

if __name__ == '__main__':
    run_setup()
