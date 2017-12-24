from setuptools import setup
import os


def _parse_requirements(filename):
    result = set()
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        filename)

    for line in open(path):
        line = line.strip()

        if not line:
            continue

        if line.startswith('-r'):
            result = result.union(_parse_requirements(line.split(' ')[1]))

        else:
            result.add(line)

    return result


setup(
    name='pymodoro',
    version='0.0.1',
    author='Roman M. Remizov',
    author_email='rremizov@yandex.ru',

    license='MIT',
    platforms=['any'],
    description="Pomodoro timer",
    long_description=open('README.rst').read(),
    url='http://github.com/rremizov/pymodoro',

    entry_points={
        'console_scripts': ['pymodoro=pymodoro.core:entry_point'],
    },

    packages=[
        'pymodoro',
    ],
    install_requires=_parse_requirements('requirements.txt'),

    # test_suite='tests.run_tests.run_all',
    # tests_require=_parse_requirements('requirements_test.txt'),

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

