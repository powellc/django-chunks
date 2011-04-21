from setuptools import setup, find_packages

setup(
    name='django-chunks',
    version=__import__('chunks').__version__,
    license="BSD",

    install_requires = ['django-markup-mixin',],

    description='Keyed chunks of conetnt for Django, now with Markup options.',
    long_description=open('README.md').read(),

    author='Colin Powell',
    author_email='colin@onecardinal.com',

    url='http://github.com/powellc/django-chunks',
    download_url='http://github.com/powellc/django-chunks/downloads',

    include_package_data=True,

    packages=['chunks'],

    zip_safe=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
