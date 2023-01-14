.. _sec_general:

General information
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
	Proprietary parameters specific to the simulation software.


.. _sec_general_parameters:

Parameters
----------

Most values with physical representation come with an associated physical unit and a measurement uncertainty. Additionally, many parameters may drift during a CT scan. In general, parameters are defined using a JSON object which may contain the following properties. Depending on the situation, only the ones of relevance must be specified. Irrelevant ones may be omitted or set to :json:`null` at any level.

.. code-block:: json-object

	"parameter": {
	  "value": 10.0,
	  "unit": "mm",
	  "uncertainty": {
	    "value": 0.1,
	    "unit": "mm"
	  }
	  "drift": [
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
--------------

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
-----------

:json:`"uncertainty":`
	gives a :json:`"value":` for the standard measurement uncertainty and its physical :json:`"unit":`. The intention is to use this to document (or model) a real, physical CT machine.

.. _sec_drifts:

Drifts
------

:json:`"drift":`
	provides an array that may contain an arbitrary number of drift components. Typically, only one drift component is necessary, but in some cases it can be useful to provide more than one drift component for a parameter, especially if some drift contributions shall be unknown to the reconstruction software, whereas others shall be considered during the reconstruction. A typical example would be a helix scan: the vertical movement of the stage along the rotation axis can be modelled as a drift that must be known during the reconstruction. However, inhomogeneities in the vertical motion can be modelled as a second drift component unknown to the reconstruction software.

	Drifts are applied for each frame individually once the stage has reached its intended position as described in the :ref:`acquisiton section <sec_acquisition>` of the scenario file. Because any drift value describes an absolute deviation from the initial condition at frame |nbsp| 0, they are not accumulated over time. If multiple drift components are defined, they are applied in an additive, sequential manner in the given order.

	Each drift component must provide a range of drift values (at least one). These drift values represent absolute deviations from the initial values at the start position (frame |nbsp| 0). They can be provided in the component's :json:`"value":` array or through a single-column CSV :json:`"file":`. If a drift component provides only a single :json:`"value":` different from :json:`null`, this drift deviation will stay constant throughout the scan. For example, a constant stage drift value for its tilt around one of the stage's plane vectors (see :ref:`geometry section <sec_geometry>`) leads to a simple axis wobble.

	For dynamic, non-constant drifts, more than one drift value can be provided in the :json:`"value":` array or CSV :json:`"file":`. Ideally, the number of rows in the CSV file would match the number of frames of the scan. If the number of provided drift values does not match the number of frames, the values are assumed to be spread in equidistant steps between start projection (first value) and last projection (last value), and a linear interpolation between neighbouring values is assumed to calculate each frame's deviation value for the parameter.

	The physical :json:`"unit":` of the deviation values should be specified; otherwise, the main parameter unit is assumed. If the drift refers to a parameter that expects a string (e.g. file name of a spectrum file), the :json:`"values":` array or CSV :json:`"file":` should contain a string for each frame; otherwise, the same equidistant behaviour is assumed as for numerical parameters with the exception that no interpolation takes place. Instead, a string remains valid until the next key frame is reached.

	The parameter :json:`"known_to_reconstruction":` (either :json:`true` or :json:`false`) can be used to specify whether the drift should be considered during the reconstruction of the CT scan (e.g. when calculating projection matrices).

	Drift keywords are prepared throughout this document for any parameters where they are assumed to be possible. In most cases of the example, they are set :json:`null`, rendering them inactive.


.. _sec_referred_data_files:

Formats of referred data files
------------------------------

A scenario description may refer to other data files.

For **one-dimensional** data such as response curves, characteristics files or spectra, the CSV (comma-separated values) or TSV format (tab-separated values) shall be used, with its columns in the order specified in the corresponding sections of this guide.

For **two-dimensional** data such as intensity profiles or bad pixel maps, image files shall be used. The minimum set of supported image file formats should be TIFF and headerless RAW. For the RAW format, please follow the details for three-dimensional data.

For **three-dimensional** data, such as a 3D spot intensity profile, a headerless RAW file shall be used. Its dimensions are specified at the respective place in the JSON scenario. The data type can be one of the following: :code:`uint8`, :code:`int8`, :code:`uint16`, :code:`int16`, :code:`float` (32 bit). Data shall be written row-first, column-second, slice-third. For an image with :math:`n_x` columns, :math:`n_y` rows and :math:`n_z` slices, this results in an array with the following one-dimensional index representation, with coordinates :math:`(x, y, z)` starting at :math:`(0, 0, 0)`:

.. math::
	:label: eq_raw_index

	\text{\textsf{Index}}(x, y, z) = (n_x \cdot n_y \cdot z) + (n_x \cdot y) + x.

3D raw data is expected to be written in little-endian byte order, and most-significant to least-significant bit (MSB\ :sub:`0`\ ).