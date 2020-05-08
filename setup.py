import sys
from setuptools import setup


try:
    from setuptools_rust import RustExtension
except ImportError:
    import subprocess

    errno = subprocess.call([sys.executable, '-m', 'pip', 'install', 'setuptools-rust'])
    if errno:
        print("Please install setuptools-rust package")
        raise SystemExit(errno)

    from setuptools_rust import RustExtension


setup(
    name='nathello',
    version='0.0.1',  # specified elsewhere
    url='localhost',
    author='root',
    author_email='root@localhost',
    install_requires=['setuptools-rust'],
    packages=[],
    rust_extensions=[RustExtension('nathello')],
)
