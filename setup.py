from setuptools import setup

setup(
    name='scikit-text',
    version='0.0.2',
    author='Christopher Brown',
    author_email='chrisbrown@utexas.edu',
    packages=['sktext'],
    include_package_data=False,
    zip_safe=True,
    install_requires=[
        'setuptools',
    ],
    entry_points={
        'console_scripts': [
        ],
    },
)
