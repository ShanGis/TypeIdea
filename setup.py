from setuptools import setup, find_packages

packages = find_packages('typeidea')

setup(
    name='typeidea',
    version='0.3',
    description='Blog based on Django',
    author='ShanGis',
    author_email='583306676@qq.com',
    url='https://github.com/ShanGis/TypeIdea',
    packages=packages,
    package_dir={'': 'typeidea'},
    include_package_data=True,
    # package_data={'':['*.html', '*.js', '*.css']},
    install_requires=['django==2.2.5',
                      "django-autocomplete-light==3.4.1",
                      "django-ckeditor==5.7.1",
                      "django-debug-toolbar==2.0",
                      "djangorestframework==3.10.3",
                      'xadmin2==2.0.1',
                      'coreapi==2.3.3',
                      'markdown==3.1.1',
                      'gunicorn==20.0.0',
                      ],
    scripts=['typeidea/manage.py', ],
),
