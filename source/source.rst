.. _sec_source:

Source
======

.. _sec_source_general:

General properties
------------------

The following properties can be specified in the source section of the scenario file.

The model name and the manufacturer, if an existing X-ray source is modelled:

.. code-block:: json-object
  :linenos:
  :lineno-start: 207

  "model":        "XS-1",
  "manufacturer": "X-ray Tube Company",

The tube acceleration voltage and the target current:

.. code-block:: json-object
  :linenos:
  :lineno-start: 209

  "voltage": {"value": 130, "unit": "kV"},
  "current": {"value": 120, "unit": "uA"}

.. _sec_target:

Target
------

.. code-block:: json-object
  :linenos:
  :lineno-start: 211

  "target": {
    "material_id": "W",
    "type": "reflection",
    "thickness": null,
    "angle": {
      "incidence": {"value": 45, "unit": "deg"},
      "emission":  {"value": 45, "unit": "deg"}
    }
  }

The target material is defined by providing a :json:`"material_id"` that refers to a material declaration in the :ref:`materials section <sec_materials>` of the file.

The :json:`"type"` can be either a transmission target or a reflection target:

.. code-block:: json-object
  :linenos:
  :lineno-start: 213

  "type": "transmission",
  "type": "reflection"

For a transmission target, its thickness must be specified:

.. code-block:: json-object
  :linenos:
  :lineno-start: 214

  "thickness": {"value": 3.0, "unit": "um"}

For a reflection target, this parameter should be set to :json:`null`.

The angles of electron incidence and main X-ray emission can be defined and refer to the angles between the target surface and electron beam or main photon emission direction, respectively.

.. _sec_spot_intensity_profile:

Spot intensity profile
----------------------

.. code-block:: json-object
  :linenos:
  :lineno-start: 220

  "spot": {
    "size": {
      "u": {"value": 100.0, "unit": "um"},
      "v": {"value": 100.0, "unit": "um"},
      "w": {"value":   0.0, "unit": "um"}
    },
    "sigma": {
      "u": {"value":  50.0, "unit": "um"},
      "v": {"value":  50.0, "unit": "um"},
      "w": {"value":   0.0, "unit": "um"}
    },
    "intensity_map": {
      "file": {"value": "spot_profile.raw", "drifts": null},
      "type": "float32",
      "dim_x": 301,
      "dim_y": 301,
      "dim_z": null,
      "endian": "little",
      "headersize": 0
    }
  }

The spot intensity profile is specified in the source's :json:`"spot"` section. At first, the :json:`"size"` of the virtual spot rectangle or volume is defined along the three axes of the source coordinate system. If only a two-dimensional spot profile is modelled, the size along the source's normal axis should be set to :json:`0`.

If the spot size is set to :json:`null`, the simulation software is free to choose a size that matches the required (Gaussian) shape.

.. code-block:: json-object
  :linenos:
  :lineno-start: 221

  "size": null

The shape of the spot can be defined in the following three ways.

.. _sec_spot_simple_gaussian:

Simple Gaussian profiles
~~~~~~~~~~~~~~~~~~~~~~~~

A simple Gaussian profile can be modelled by specifying the spatial sigmas :math:`\sigma` for each dimension:

:math:`I(\vec{r})=I_0\cdot\exp(-|\vec{r}|^2/2\sigma^2)`

.. code-block:: json-object
  :linenos:
  :lineno-start: 226

  "sigma": {
    "u": {"value":  50.0, "unit": "um"},
    "v": {"value":  50.0, "unit": "um"},
    "w": {"value":   0.0, "unit": "um"}
  },

.. _sec_spot_2d_images:

2D images
~~~~~~~~~

For a more detailed approach, the intensity profile can also be provided from an external image file. In this case, the :math:`\vec{u}` vector of the source coordinate system points from left to right in the image, and the :math:`\vec{v}` vector points from top to bottom, in analogy to the :ref:`detector geometry <sec_geometry_detector>`. The image shall be resized to match the given :json:`"size"` of the spot rectangle, without necessarily retaining the original aspect ratio of the image. The picture is recommended to be a 32 |nbsp| bit float gray-scale image and the pixel values in the interval [0, |nbsp| 1], with 0 meaning no intensity, and 1 meaning full intensity. However, a simulation software must also support gray-scale integer file formats and be able to re-normalize the provided gray values accordingly.

If a valid spot intensity image is provided, this method takes precedence over the previously described specification of Gaussian sigmas.

Further details about referring to :ref:`two-dimensional data files <sec_referred_data_files_2d>` (RAW or TIFF) are given in the section about *General structures*.

.. _sec_spot_3d_volumes:

3D volumes
~~~~~~~~~~

To describe a three-dimensional spot profile, a RAW file can be provided. It is recommended to be a 32 |nbsp| bit float volume with values between :code:`0` and :code:`1`, and should otherwise be re-normalized by the simulation software. The lowest value means no intensity, the highest value means maximum intensity. If specified, this method takes precedence over the first two described methods.

The :math:`x` direction of the given volume points along the :math:`\vec{u}` vector of the source coordinate system, :math:`y` points in direction :math:`\vec{v}`, and :math:`z` in direction :math:`\vec{w}`. The volume shall be resized to match the :json:`"size"` of the spot volume, without necessarily retaining the original aspect ratio of the volume file.

Further details about referring to :ref:`three-dimensional data files <sec_referred_data_files_3d>` (RAW volumes) are given in the section about *General structures*.

.. _sec_source_spectrum:

Spectrum
--------

If the spectrum is to be calculated by the simulation software, the following three parameters decide whether only a monochromatic energy scenario is described or a complete spectrum. If a valid spectrum file is provided, it takes precendence over the monochromatic mode. If no spectrum file is provided, a simulation software is free to generate its own spectrum from the given tube parameters.

.. code-block:: json-object
  :linenos:
  :lineno-start: 241

  "spectrum": {
    "monochromatic": false,
    "file": {"value": "tube_spectrum_130kV.tsv", "drifts": null}
  }

The spectrum from the provided file is assumed to be already filtered by the tube's window material, but not yet by any of the filters in front of the tube (as specified under :ref:`Tube window and filters <sec_tube_filters>`). The CSV or TSV spectrum file should contain the columns listed in :numref:`tab_csvSpectrum`, separated by a comma or tab character.

.. _tab_csvSpectrum:

.. table:: Table structure for X-ray spectrum files.

  ====== =================================================
  Column Property
  ====== =================================================
  1      Photon energy in keV
  2      Number of photons in 1 / (s ⋅ sr ⋅ mA)
  3      Uncertainty in the number of photons *(optional)*
  ====== =================================================

The energy values correspond to the centre of the histogram bins. The interpolation between the bin values shall not be specified here and is left to the simulation software. If a valid spectrum file is specified and the :json:`"file"` parameter is not set to :json:`null`, this has precedence over the spectrum calculated by the simulation software or the monochromatic mode.

.. _sec_tube_filters:

Tube window and filters
-----------------------

The :json:`"window"` material(s) and the additional :json:`"filters"` in front of the tube are specified in two separate JSON arrays. For both, an arbitrary number of materials and thicknesses can be specified. If a :ref:`source spectrum <sec_source_spectrum>` is provided in a file, the spectrum is assumed to be already filtered by all :json:`"window"` materials but not yet by any :json:`"filters"`.

The :json:`"material_id"` refers to the :ref:`material definition <sec_materials>` in the :json:`"materials"` section of the file. Also, a window and filter :json:`"thickness"` must be provided.

.. code-block:: json-object
  :linenos:
  :lineno-start: 245

  "window": [
    {
      "material_id": "Al",
      "thickness": {"value": 4.0, "unit": "mm"}
    }
  ],
  "filters": [
    {
      "material_id": "Brass",
      "thickness": {"value": 0.5, "unit": "mm"}
    },
    {
      "material_id": "Cu",
      "thickness": {"value": 0.25, "unit": "mm"}
    }
  ]