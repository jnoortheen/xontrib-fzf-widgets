from setuptools import setup

setup(
    name='xontrib-fzf-widgets',
    version='0.0.4',
    url='https://github.com/laloch/xontrib-fzf-widgets',
    license='GPLv3',
    author='David Strobach',
    author_email='lalochcz@gmail.com',
    description="fzf widgets for xonsh",
    install_requires=['xonsh>=0.10'],
    packages=['xontrib'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.xsh']},
    platforms='any',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Desktop Environment',
        'Topic :: System :: Shells',
        'Topic :: System :: System Shells',
    ]
)
