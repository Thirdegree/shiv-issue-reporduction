import setuptools 
setuptools.setup(
    name='shiv-issue-reproduction',
    packages=['reproduce'],
    entry_points={
        'console_scripts': [
            'example=reproduce.main:main',
            ]
        }
)
