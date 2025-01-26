from setuptools import setup, find_packages

setup(
    name='turtleforbeginners',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'turtleforbeginners/src'},
    install_requires=[
        # List any dependencies here, e.g., 'numpy', 'requests'
    ],
    author='Jochni',
    author_email='test@test.com',
    description='A short description of your library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/Jochni/turtleforbeginners',
)
