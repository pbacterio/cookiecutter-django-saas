from setuptools import setup

setup(
    name='{{cookiecutter.project_name}}',
    install_requires=['Django', 'waitress', 'dj-paas-env>=0.5', 'dj-static', 'psycopg2'],
)
