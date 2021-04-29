from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='1.0',
    entry_points={
         'console_scripts': ['clean-folder=clean_folder.clean:main'],
    },
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    description='Clean folder script',
)
