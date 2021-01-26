from setuptools import setup
try:
    import multiprocessing
except ImportError:
    pass


setup(
    name='httpie-edgegrid',
    description='Edgegrid plugin for HTTPie.',
    python_requires=">=2.7.10",
    long_description=open('README.rst').read().strip(),
    version='1.0.2',
    author='Kirsten Hunter',
    author_email='khunter@akamai.com',
    license='Apache 2.0',
    url='https://github.com/akamai-open/httpie-astra',
    download_url='https://github.com/akamai-open/httpie-astra',
    py_modules=['httpie_astra'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.auth.v1': [
            'httpie_oauth1 = httpie_astra:AstraPlugin'
        ]
    },
    install_requires=[
        'httpie >= 0.9.2',
	    'astra-python >= 0.0.1'
    ],
)
