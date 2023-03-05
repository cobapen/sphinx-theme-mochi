======================
sample docs
======================


Tree
===========

This section displays a toctree and sub-toctrees

.. toctree::
    :maxdepth: 1
    :caption: ToC Tree

    doc/tree/page1
    doc/tree/page2


Navigation
==========

This is the most important part of a documentation theme. If you like
the general look of the theme, please make sure that it is possible to
easily navigate through this sample documentation.

Ideally, the pages listed below should also be reachable via links
somewhere else on this page (like the sidebar, or a topbar). If they are
not, then this theme might need additional configuration to provide the
sort of site navigation that's necessary for "real" documentation.

.. toctree::
    :caption: This is a caption
    :titlesonly:

    doc/placeholder-one
    doc/placeholder-two
    doc/really-long-title
    doc/long-page
    External Link <https://www.sphinx-doc.org>

.. toctree::
    :hidden:
    :caption: Additional "hidden" Pages

    doc/placeholder-three
    doc/placeholder-four
    Sphinx Theme Gallery <https://sphinx-themes.org>

:doc:`doc/placeholder-three` is part of "hidden" toctree. It is not shown above, but do exists.

Index
===========
The :doc:`doc/kitchen-sink/index` section contains pages that contains basically
everything that you can with Sphinx "out-of-the-box".


.. toctree::
    :titlesonly:

    doc/kitchen-sink/index