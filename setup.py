from setuptools import setup, find_packages

setup(
    name='sphinx_mochi_theme',
    version='2023.03.01',
    packages=find_packages('sphinx_mochi_theme'),
    entry_points={
        'sphinx.html_themes': [
            'sphinx_mochi_theme = sphinx_mochi_theme',
        ]
    }
)
