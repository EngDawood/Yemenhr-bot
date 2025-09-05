from setuptools import setup, find_packages

setup(
    name='yemen-jobs-rss',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'yemen-jobs-rss = src.entrypoint:main',
        ],
    },
)