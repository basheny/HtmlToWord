from distutils.core import setup

setup(
    name='word',
    version='0.5',
    packages=['word'],
    url='https://github.com/orf/HtmlToWord',
    license='',
    author='Tom',
    author_email='tom@tomforb.es',
    description='Render HTML to a specific portion of a word document',
    install_requires=["BeautifulSoup4"],
    include_package_data=True,
    long_description="""\
Render HTML to a word document using win32com.
Check out the github repo for more information and code samples.
"""
)
