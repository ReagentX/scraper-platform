from setuptools import setup, find_packages


setup(
    name='scraper_platform',
    version='1.0',
    description='A versatile Python 3 scraper platform.',
    author='Christopher Sardegna',
    author_email='github@reagentx.net',
    install_requires=['requests', 'requests-cache'],
    packages=find_packages(),
    scripts=['scripts/test.py']
)
