.. _sec_materials:

Materials
=========

In all previous declarations, materials are referred by their :json:`"material_id"`. The last section of the JSON file, the materials array, finally contains the specifications for all materials used throughout the scenario description. Each element of the materials array must have the following properties:

:json:`"id":`
  names the material ID that is used to refer to the material from the other sections of the file.

:json:`"name":`
  is a trivial name that can be given to the material for better identification.

:json:`"density":`
  provides the mass density of the material.

:json:`"composition":`
  gives the chemical composition: a string of chemical symbols, each followed by their corresponding **number fraction** (integers or floating-point numbers) within the material. White space between symbols and numbers is allowed. If the number fraction of an element is 1, the number can be omitted and the next chemical symbol can follow right away. All chemical symbols start with a capital letter, potentially followed by lower-case letters.

Example for a multi-component material:

.. code-block:: json-object
  :linenos:
  :lineno-start: 371

  {
    "id":   "Brass",
    "name": "Brass",
    "density": {"value": 8860, "unit": "kg/m^3"},
    "composition": {"value": "CuZn5"}
  }

Example for a material with unusual number fractions, derived from a mass ratio of 40% |nbsp| Al\ :sub:`2`\ O\ :sub:`3` and 60% |nbsp| SiO\ :sub:`2`\ :

.. code-block:: json-object
  :linenos:
  :lineno-start: 389

  {
    "id":   "Glass Ceramic",
    "name": "Glass Ceramic",
    "density": {"value": 2.53, "unit": "g/cm^3"},
    "composition": {"value": "Al 0.21172 Si 0.28044 O 0.50784"}
  }
