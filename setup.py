from setuptools import setup ,find_packages

setup(
    name='sysbot',
    version='0.1',
    description='Notify Developers of server activities',
    author='Nitigya Sharma',
    email='nsharma@dimagi.com',
    packages=find_packages(),
    scripts=['sysbot.py'],
    install_requires=[
        'requests',
    ]
)
