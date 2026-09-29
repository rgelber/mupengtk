from setuptools import setup, find_packages

setup(
    name='mupengtksettings',
    version='0.2.0',
    description='Settings library for MupenGTK',
    url='https://github.com/rcgelber/mupengtk',
    author='Ryan Gelber',
    author_email='ryangelber@gmail.com',
    license='GPLv3',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=['PyYAML>=5.1'],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Emulators',
    ],
)
