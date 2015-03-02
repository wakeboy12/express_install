from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='digicert_express',
    version='1.0',
    description='Express Install for DigiCert, Inc.',
    long_description=readme(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Security',
    ],
    url='http://github.com/digicert/digicert_express',
    author='DigiCert, Inc.',
    author_email='support@digicert.com',
    license='MIT',
    zip_safe=False,
    packages=find_packages(exclude=['tests.*', '*.tests.*', '*.tests', 'tests', 'scripts']),
    include_package_data=True,
)
