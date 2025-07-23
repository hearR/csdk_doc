# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'QuecOS User Guide'
copyright = '2025, Quectel'
author = 'Quectel'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# 添加扩展
extensions = [
    'sphinx.ext.autodoc',       # 自动文档支持
    'sphinx.ext.viewcode',      # 查看源码支持
    'sphinx.ext.napoleon',      # 支持 Google 和 NumPy 风格 docstring
]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# 使用 ReadTheDocs 主题
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
