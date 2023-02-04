.. _sec_materials:

Materials
=========

In all previous declarations, materials are referred by their :json:`"material_id"`. The last section of the JSON file, the materials array, finally contains the specifications for all materials used throughout the scenario description. Each element of the :json:`"materials"` array must have the following properties:

:json:`"id":`
  names the material ID that is used to refer to the material from the other sections of the file.

:json:`"name":`
  is a trivial name that can be given to the material for better identification.

:json:`"density":`
  provides the mass density of the material. The density of a material may drift during the CT scan.

:json:`"composition":`
  gives the chemical composition. It is a JSON array that provides the empirical :json:`"formula"` and :json:`"mass_fraction"` for each component of the material. See examples below.

  * The :json:`"formula"` is a string of chemical symbols, each followed by their corresponding **number fraction** (integers or floating-point numbers) within the material. White space between symbols and numbers is allowed, but has no meaning. If the number fraction of an element is 1, the number can be omitted and the next chemical symbol can follow right away. All chemical symbols start with a capital letter, potentially followed by lower-case letters.

  * A component's :json:`"mass_fraction"` in a compound material can be specified by a number. All **mass fractions** of a material should add up to :code:`1`, but this is not required. A simulation software is assumed to re-normalize the sum of a material's mass ratios to :code:`1` if this condition is not met.

  The :json:`"formula"` and :json:`"mass_fraction"` may drift during a CT scan.


Single-component materials
--------------------------

The following gives an example of a single-component material: pure copper.

.. code-block:: json-object
  :linenos:
  :lineno-start: 412

  {
    "id":   "Cu",
    "name": "Copper",
    "density": {"value": 8.92, "unit": "g/cm^3"},
    "composition": [
      {
        "formula": {"value": "Cu"},
        "mass_fraction": {"value": 1}
      }
    ]
  }


Multi-component materials
-------------------------

Simple multi-component materials with known number fractions can be modeled using only the :json:`"formula"` parameter.

.. code-block:: json-object
  :linenos:
  :lineno-start: 401

  {
    "id":   "Brass",
    "name": "Brass",
    "density": {"value": 8860, "unit": "kg/m^3"},
    "composition": [
      {
        "formula": {"value": "CuZn5"},
        "mass_fraction": {"value": 1}
      }
    ]
  }

Multi-component materials with different **mass fractions** can be modeled by adding further components with their proper mass ratios to the :json:`"composition"` array. The following example defines a glass ceramic with a mass ratio of 40% |nbsp| Al\ :sub:`2`\ O\ :sub:`3` and 60% |nbsp| SiO\ :sub:`2`\ :

.. code-block:: json-object
  :linenos:
  :lineno-start: 434

  {
    "id":   "Glass Ceramic",
    "name": "Glass Ceramic",
    "density": {"value": 2.53, "unit": "g/cm^3", "drifts": null},
    "composition": [
      {
        "formula": {"value": "Al2O3", "drifts": null},
        "mass_fraction": {"value": 0.4, "drifts": null}
      },
      {
        "formula": {"value": "SiO2", "drifts": null},
        "mass_fraction": {"value": 0.6, "drifts": null}
      }
    ]
  }

Another example for a multi-component material would be the environment's air:

.. code-block:: json-object
  :linenos:
  :lineno-start: 345

  {
    "id":   "Air",
    "name": "Air",
    "density": {"value": 1.293, "unit": "kg/m^3"},
    "composition": [
      {
        "formula": {"value": "N2"},
        "mass_fraction": {"value": 0.7552}
      },
      {
        "formula": {"value": "O2"},
        "mass_fraction": {"value": 0.2314}
      },
      {
        "formula": {"value": "Ar"},
        "mass_fraction": {"value": 0.0128}
      },
      {
        "formula": {"value": "CO2"},
        "mass_fraction": {"value": 0.0006}
      }
    ]
  }