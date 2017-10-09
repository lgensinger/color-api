from setuptools import setup, find_packages

packages=[find_packages()]

reqs = [
    "flask", "flask_restful", "psycopg2"
]

setup(
    name="color-api",
    version="1.0.0",
    url="",
    install_requires=reqs
)