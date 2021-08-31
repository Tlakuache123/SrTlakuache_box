from setuptools import setup
setup(
    name='main',
    version='0.1.0',
    py_modules=['main'],
    install_requires=[
        'Click',
        'Rich'
    ],
    entry_points={
        'console_scripts': [
            'main = main:horario',
        ],
    },
)