from setuptools import setup, find_packages
import sys
try:
    from pyqt_distutils.build_ui import build_ui
    cmdclass = {'build_ui': build_ui}
except ImportError:
    cmdclass = {}


def read_version():
    """
    Reads the version without self importing
    """
    with open("qxpatheditor/__init__.py") as f:
        lines = f.read().splitlines()
        for l in lines:
            if "__version__" in l:
                return l.split("=")[1].strip().replace('"', "").replace(
                    "'", '')


requirements = []


# Data files to install
if sys.platform == 'win32':
    data_files = []
else:
    data_files = [
        ('share/applications/', ['share/qxpatheditor.desktop']),
        ('share/pixmaps/', ['share/qxpatheditor.png'])
    ]


setup(
    name='QXpathEditor',
    version=read_version(),
    packages=find_packages(),
    data_files=data_files,
    author='Inkapa',
    author_email='Inkapable@pm.me',
    maintainer='Inkapa',
    maintainer_email='Inkapable@pm.me',
    description='PyQt Xpath editor',
    keywords=["Xpath editor"],
    install_requires=requirements,
    cmdclass=cmdclass,
    url='https://github.com/Inkapa/QXpathEditor',
    entry_points={
        'gui_scripts': [
            'QXPathEditor = qxpatheditor.app.main:main'
        ],
        'pyqt_distutils_hooks': [
            'fix_qt_imports = qxpatheditor._hooks:fix_qt_imports']
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: X11 Applications :: Qt',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Widget Sets',
    ]
)
