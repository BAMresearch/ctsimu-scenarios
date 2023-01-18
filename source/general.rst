.. _sec_general:

General structures
===================

.. _sec_file_structure:

File structure
--------------

The JSON file should be encoded and decoded using the UTF-8 character set, even though all characters in this specification are from the ASCII set to ensure compatibility with other decoding interpretations.

The scenario description consists of the following main sections:

:json:`"file":`
  General file information: scenario name, file format version.

:json:`"environment":`
  Description of the environment: temperature, atmosphere.

:json:`"geometry":`
  Location and orientation of source, detector and sample stage (rotation axis).

:json:`"detector":`
  Parameters and characteristics of the detector.

:json:`"source":`
  Parameters and characteristics of the X-ray source.

:json:`"samples":`
  Definitions of all samples: surface models, location and orientation, size.

:json:`"acquisition":`
  Parameters for the CT acquisition: angular steps, flat fields, etc.

:json:`"materials":`
  Density and chemical composition of all materials relevant to the scenario.

:json:`"simulation":`
  Proprietary parameters specific to a simulation software.


.. _sec_general_parameters:

Parameters
----------

A parameter is given by its :json:`"value"` and may have an associated physical :json:`"unit"`. Additionally, a parameter may come with a measurement :json:`"uncertainty"` and one or more :json:`"drift"` components if its value changes during the CT scan. The following listing shows a full example of a parameter definition. Note that :json:`"drifts"` is an array that may contain multiple drift components.

Depending on the situation, only the parameter properties of relevance must be specified. Irrelevant ones may be omitted or set to :json:`null` at any level.

.. code-block:: json-object

  "parameter": {
    "value": 10.0,
    "unit": "mm",
    "uncertainty": {
      "value": 0.1,
      "unit": "mm"
    }
    "drifts": [
      {
        "value": [-100, 100],
        "file":  null,
        "unit":  "mm",
        "known_to_reconstruction": true
      },
      {
        "value": null,
        "file":  "vertical_motion_deviations.csv",
        "unit":  "mm",
        "known_to_reconstruction": false
      }
    ]
  }

.. _sec_values_and_units:

Values & Units
~~~~~~~~~~~~~~

:json:`"value":`
  gives the measured value or the value that should be used by the simulation software.

:json:`"unit":`
  gives the physical unit of the value.

The following units are allowed for length, angle, time, voltage, current, density, temperature, angular velocity and the spatial frequency, and should be interpreted correctly by any parser.

.. code-block:: json-object

    "nm"  "deg"  "ms"   "MV"  "uA"  "g/cm^3"  "C"  "deg/s"    "lp/mm"  "px"  "relative"  null
    "um"  "rad"  "s"    "kV"  "mA"  "kg/m^3"  "K"  "deg/min"  "lp/cm"
    "mm"         "min"  "V"   "A"             "F"  "deg/h"    "lp/dm"
    "cm"         "h"                               "rad/s"    "lp/m" 
    "dm"                                           "rad/min"        
    "m"                                            "rad/h"         

The prefix :code:`u` represents the SI prefix µ (10\ :sup:`-6`\ ). :json:`"relative"` can be used for relative uncertainties or any values that express a fraction of a related measure. For properties without a unit, the keyword :json:`null` is used.

.. _sec_uncertainty:

Uncertainty
~~~~~~~~~~~

:json:`"uncertainty": {"value": 0.1, "unit": "mm"}`
  gives a :json:`"value"` for the standard measurement uncertainty and its physical :json:`"unit"`. The intention is to use this to document (or model) a real, physical CT machine.

.. _sec_drifts:

Drifts
~~~~~~

:json:`"drifts":`
  provides an array that may contain an arbitrary number of drift components. Typically, only one drift component is necessary, but in some cases it can be useful to provide more than one drift component for a parameter, especially if some drift contributions shall be unknown to the reconstruction software, whereas others shall be considered during the reconstruction. A typical example would be a helix scan: the vertical movement of the stage along the rotation axis can be modelled as a drift that must be known during the reconstruction. However, inhomogeneities in the vertical motion can be modelled as a second drift component unknown to the reconstruction software.

  **Drifts are applied for each frame individually** once the stage has reached its intended position as described in the :ref:`acquisiton section <sec_acquisition>` of the scenario file. Because any drift value describes an absolute deviation from the initial condition at frame |nbsp| 0, they are not accumulated over time. If multiple drift components are defined, they are applied in an additive, sequential manner in the given order.

  Each drift component must provide a range of drift values (at least one). These drift values represent absolute deviations from the initial values at the start position (frame |nbsp| 0). They can be provided in the component's :json:`"value"` array or through a single-column CSV :json:`"file"` (i.e., a simple one-column list). If a drift component provides only a single :json:`"value"` different from :json:`null`, this deviation will stay constant throughout the scan.

  For dynamic, non-constant drifts, more than one drift value can be provided in the :json:`"value"` array or CSV :json:`"file"`. Ideally, the number of rows in the CSV file would match the number of frames of the scan. If the number of provided drift values does not match the number of frames, the values are assumed to be spread in equidistant steps between start projection (first value) and last projection (last value), and a linear interpolation between neighbouring values is assumed to calculate each frame's deviation value for the parameter.

  The physical :json:`"unit"` of the drift values should be specified; otherwise, the main parameter unit is assumed. If the drift refers to a parameter that expects a string (e.g. file name of a spectrum file), the :json:`"values"` array or CSV :json:`"file"` should contain a string for each frame; otherwise, the same equidistant behaviour is assumed as for numerical parameters with the exception that no interpolation takes place. Instead, a string remains valid until the next key frame is reached.

  The parameter :json:`"known_to_reconstruction"` (either :json:`true` or :json:`false`) can be used to specify whether the drift should be considered during the reconstruction of the CT scan. This also applies to automatically generated configuration files or the calculation of projection matrices for the reconstruction software.


.. _sec_referred_data_files:

Formats of referred data files
------------------------------

A scenario description may refer to other data files.

One-dimensional data
~~~~~~~~~~~~~~~~~~~~

For one-dimensional data such as response curves, characteristics files or spectra, the CSV (comma-separated values) or TSV format (tab-separated values) shall be used, with its columns in the order specified in the corresponding sections of this guide.

Two-dimensional data
~~~~~~~~~~~~~~~~~~~~
For **two-dimensional** data such as intensity profiles or bad pixel maps, image files shall be used. The minimum set of supported image file formats should be TIFF and RAW. The image file is given by its :json:`"file"` name which specifies the file's path relative to the JSON file, or provides an absolute path.

.. code-block:: json-object
  :linenos:
  :lineno-start: 216

  "intensity_map": {
    "file": {"value": "spot_profile.raw", "drifts": null},
    "type": "float32",
    "dim_x": 301,
    "dim_y": 301,
    "endian": "little",
    "headersize": 0
  }

For the RAW format, the following additional parameters must be specified:

* The data :json:`"type"`. Valid data types are: :code:`"uint8"`, :code:`"int8"`, :code:`"uint16"`, :code:`"int16"`, :code:`"float32"`, :code:`"float64"`,
* The image size in pixels, given by :json:`"dim_x"` and :json:`"dim_y"`.
* The :json:`"endian"` can be :code:`"little"` or :code:`"big"`.
* As an optional parameter, the :json:`"headersize"` gives the number of bytes to skip at the beginning of the file, or, in other words, the byte offset of the image data.

Data shall be written row-first. For an image with :math:`n_x` columns and :math:`n_y` rows, this results in an array with the following one-dimensional index representation, with coordinates :math:`(x, y)` starting at :math:`(0, 0)`:

.. math::
  :label: eq_raw_index2d

  \text{\textsf{Index}}(x, y) = (n_x \cdot y) + x.

Bytes are assumed to be written from most-significant to least-significant bit (MSB\ :sub:`0`\ ).

Three-dimensional data
~~~~~~~~~~~~~~~~~~~~~~~
For **three-dimensional** data, such as a 3D spot intensity profile, a RAW file shall be used. The notation is the same as for 2D data, with the addition of the third voxel dimension given by :json:`"dim_z"`.

.. code-block:: json-object
  :linenos:
  :lineno-start: 216

  "intensity_map": {
    "file": {"value": "spot_profile.raw", "drifts": null},
    "type": "float32",
    "dim_x": 201,
    "dim_y": 201,
    "dim_z": 201,
    "endian": "little",
    "headersize": 0
  }

Data shall be written as row-first, column-second slices. For an image with :math:`n_x` columns, :math:`n_y` rows and :math:`n_z` slices, this results in an array with the following one-dimensional index representation, with coordinates :math:`(x, y, z)` starting at :math:`(0, 0, 0)`:

.. math::
  :label: eq_raw_index3d

  \text{\textsf{Index}}(x, y, z) = (n_x \cdot n_y \cdot z) + (n_x \cdot y) + x.

Bytes are assumed to be written from most-significant to least-significant bit (MSB\ :sub:`0`\ ).