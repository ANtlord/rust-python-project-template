import sys
from setuptools import setup


try:
    from setuptools_rust import RustExtension
except ImportError:
    import subprocess

    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'setuptools-rust'])
    except Exception as e:
        print(
            'Fail installing setuptools-rust. Reason: %s. Install it manually from %s' % (
                e, 'https://pypi.org/project/setuptools-rust/',
            )
        )
        exit(1)

    from setuptools_rust import RustExtension


setup(
    name='nathello',
    version='0.0.1',  # specified elsewhere
    url='localhost',
    author='root',
    author_email='root@localhost',
    install_requires=[],
    packages=[],
    rust_extensions=[RustExtension('nathello')],
)
