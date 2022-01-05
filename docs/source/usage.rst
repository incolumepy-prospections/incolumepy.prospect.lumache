Usage
=====

.. _installation:

Installation
------------

To use Lumache, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache

or install it using poetry:

.. code-block:: console

   poetry add lumache

.. _creating_recipes:

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: incolumepy.prospect.lumache.lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: incolumepy.prospect.lumache.lumache.InvalidKindError

**Exemple**


>>> from incolumepy.prospect.lumache import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']
