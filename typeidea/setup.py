from setuptools import setup, find_packages

packages = find_packages('typeidea')

setup(
    name='typeidea',
    version='0.1',
    description='Blog based on Django',
    author='ShanGis',
    author_email='583306676@qq.com',
    url='https://github.com/ShanGis/TypeIdea',
    packages=packages,
    package_dir={'': 'typeidea'},
    include_package_data=True,
    install_requires=['django==2.2.5'],
    scripts='typeidea/manage.py'
)