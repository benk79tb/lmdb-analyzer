from setuptools import setup, find_packages

setup(
    name='lmdb_analyzer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'lmdb',
    ],
    entry_points={
        'console_scripts': [
            'lmdb-analyzer=lmdb_analyzer.lmdb_analyzer:main',
        ],
    },
    author='Benjamin Keller',
    author_email='benkeller1979@gmail.com',
    description='Une application pour analyser le contenu des bases de données LMDB.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/benk79tb/lmdb-analyzer',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
