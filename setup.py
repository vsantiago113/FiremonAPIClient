from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='FiremonAPIWrapper',
    packages=['FiremonAPIWrapper'],
    version='0.0.1',
    license='MIT',
    description='An API Wrapper to use Firemon RESTful API.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Victor M Santiago',
    author_email='vsantiago113sec@gmail.com',
    url='https://github.com/vsantiago113/Firemon-API-Wraper',
    download_url='https://github.com/vsantiago113/Firemon-API-Wraper/archive/0.0.1.tar.gz',
    keywords=['Firemon', 'Wrapper'],
    python_requires='>=3.4.0',
    install_requires=[
        'requests',
        'urllib3'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
