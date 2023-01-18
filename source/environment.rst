.. _sec_environment:

Environment
===========

In the :json:`"environment"` section, the composition of the atmosphere can be described, as well as the environment temperature.

.. code-block:: json-object
  :linenos:
  :lineno-start: 15

  "environment": {
    "material_id": "Air",
    "temperature": {
      "value": 20, "unit": "C",
      "uncertainty": {"value": 0.5, "unit": "C"}
    }
  }