from setuptools import setup, find_packages

with open('README.rst') as file:
    long_description = file.read()

setup(name="aco2sass",
      version="0.1",
      description=long_description,
      py_modules=['aco2sass'],
      author="Kostas Papadimitriou",
      author_email="vinilios@gmail.com",
      entry_points = {
          'console_scripts': [
            'aco2sass = aco2sass:main'
          ]
      },
      keywords="aco swatch sass convert",
      license="MIT",
      url="https://github.com/vinilios/aco2sass")

