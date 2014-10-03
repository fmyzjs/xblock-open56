from setuptools import setup

setup(
    name='xblock-open56',
    version='0.1',
    description='open56 XBlock Tutorial Sample',
    py_modules=['open56'],
    install_requires=['XBlock'],
    entry_points={
        'xblock.v1': [
            'open56 = open56:Open56Block',
        ]
    }
)
