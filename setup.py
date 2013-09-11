from distutils.core import setup

setup(
    name='pinyin',
    version='0.2.2',
    description='Translate chinese chars to pinyin based on Mandarin.dat',
    author='Lx Yu',
    author_email='lixinfish@gmail.com',
    packages=['pinyin', ],
    package_data={'': ['LICENSE'], 'pinyin': ['Mandarin.dat'], },
    entry_points={"console_scripts": ["pinyin = pinyin.cmd:pinyin", ]},
    url='http://lxyu.github.com/pinyin/',
    license=open('LICENSE').read(),
    long_description=open('README.rst').read(),
)
