Usage
=====

.. _installation:

Installation
------------

To use dj-apis-allauth, first install it using pip:

.. code-block:: console

    $ pip install dj-apis-allauth

Creating Registration and login API Endpoints
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import dj_apis_allauth
>>> dj_apis_allauth.views


