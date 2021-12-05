.. _file:

File
====

The :json:`"file":` section leaves room for specifying a scenario :json:`"name":` and a short :json:`"description":`. Further meta data such as a :json:`"contact":` person, dates of creation and modification, and a file :json:`"version":` can be added here.

The :json:`"file_type":` is a constant string to identify this as a CTSimU scenario and must not be changed. The :json:`"file_format_version":` states which issue of the file format specification is used.

.. code-block:: json-object
  :linenos:
  :lineno-start: 2

  "file":
  {
    "name": "Example Scenario",
    "description": "Step cylinder in a rigid frame.",

    "contact": "David Plotzki",
    "date_created": "2020-04-23",
    "date_changed": "2020-05-15",
    "version": {"major": 1, "minor": 4},

    "file_type": "CTSimU Scenario",
    "file_format_version": {"major": 0, "minor": 9}
  }