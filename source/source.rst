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
	:lineno-start: 193

	"model":        "",
	"manufacturer": ""

The tube acceleration voltage and the target current:

.. code-block:: json-object
	:linenos:
	:lineno-start: 195

	"voltage": {"value": 130, "unit": "kV", "uncertainty": {"value": 0, "unit": "kV"}, "drift": null},
	"current": {"value": 100, "unit": "uA", "uncertainty": {"value": 0, "unit": "uA"}, "drift": null}


.. _sec_target:

Target
------

The target material is defined by providing a :json:`"material_id":` that refers to a material declaration in the materials section of the file (sec.~\ref{sec:materials}).

.. code-block:: json-object
	:linenos:
	:lineno-start: 199

	"material_id": "W"

The :json:`"type":` can be either a transmission target or a reflection target:

.. code-block:: json-object
	:linenos:
	:lineno-start: 200

	"type": "transmission" "reflection"

For a transmission target, its thickness can be specified:

.. code-block:: json-object
	:linenos:
	:lineno-start: 201

	"thickness": {"value": 3.0, "unit": "um", "uncertainty": {"value": 0, "unit": "um"}, "drift": null}

For a reflection target, this parameter should be set to :json:`null`:

.. code-block:: json-object
	:linenos:
	:lineno-start: 201

	"thickness": null

The angles of electron incidence and main X-ray emission can be defined and refer to the angles between the target surface and electron beam or main photon emission direction, respectively.

.. code-block:: json-object
	:linenos:
	:lineno-start: 202

	"angle":
	{
	  "incidence": {"value": 45, "unit": "deg", "uncertainty": {"value": 0, "unit": "deg"}, "drift": null},
	  "emission":  {"value": 45, "unit": "deg", "uncertainty": {"value": 0, "unit": "deg"}, "drift": null}
	}


.. _sec_spotIntensityProfile:

Spot intensity profile
----------------------

The spot intensity profile is specified in the source's :json:`"spot":` section. At first, the size of the virtual spot rectangle or volume is defined along the three axes of the source coordinate system. If only a two-dimensional spot profile is modelled, the size along the source's normal axis should be set to :json:`0`.

.. code-block:: json-object
	:linenos:
	:lineno-start: 210

	"size": {
	  "u": {"value": 100.0, "unit": "um", "uncertainty": {"value": 0, "unit": "um"}, "drift": null},
	  "v": {"value": 100.0, "unit": "um", "uncertainty": {"value": 0, "unit": "um"}, "drift": null},
	  "w": {"value":   0.0, "unit": "um", "uncertainty": {"value": 0, "unit": "um"}, "drift": null}
	}

If the spot size is set to :json:`null`, the simulation software is free to choose a size that matches the required (Gaussian) shape.

.. code-block:: json-object
	:linenos:
	:lineno-start: 210

	"size": null

The shape of the spot can be defined in the following three ways.

Simple Gaussian profiles
~~~~~~~~~~~~~~~~~~~~~~~~

A simple Gaussian profile can be modelled :math:`I(\vec{r})=I_0\cdot\exp(-|\vec{r}|^2/2\sigma^2)`, by specifying the spatial sigmas :math:`\sigma` for each dimension:

.. code-block:: json-object
	:linenos:
	:lineno-start: 210
	
	"sigma": {
	  "u": {"value":  50.0, "unit": "um", "uncertainty": {"value": 0, "unit": "um"}, "drift": null},
	  "v": {"value":  50.0, "unit": "um", "uncertainty": {"value": 0, "unit": "um"}, "drift": null},
	  "w": {"value":   0.0, "unit": "um", "uncertainty": {"value": 0, "unit": "um"}, "drift": null}
	}

2D images
~~~~~~~~~

For a more detailed approach, the intensity profile can also be provided from an external image file. In this case, the :math:`\vec{u}` vector of the source coordinate system points from left to right in the image, and the :math:`\vec{v}` vector points from top to bottom, in analogy to the dector (sec.~\ref{sec:geometry_detector}). The image shall be resized to match the :json:`"size":` of the spot rectangle, without necessarily retaining the original aspect ratio of the image. The picture is recommended to be a 32 |nbsp| bit float grey-scale image, and the pixel values in the interval [0, |nbsp| 1], with 0 meaning no intensity, and 1 meaning full intensity. However, a simulation software must also support grey-scale integer file formats, and be able to re-normalize the provided grey values accordingly. If a valid spot intensity image is provided, this method takes precedence over the previously described specification of Gaussian sigmas.

If a RAW file is provided, the number of pixels in directions :math:`x` (i.e. :math:`\vec{u}` in the source coordinate system) and :math:`y` (i.e. :math:`\vec{v}`) must be specified, as well as its type (see section \ref{sec:formats} about formats of referred data files for details). For TIFF images, the parameters :json:`"type":`, :json:`"dim_x":` and :json:`"dim_y":` are obsolete and can be omitted.

.. code-block:: json-object
	:linenos:
	:lineno-start: 220

	"intensity_map": {
	  "file": "spot_intensities.raw",
	  "type": "float",
	  "dim_x": 100,
	  "dim_y": 100,
	  "drift": null
	}

3D volumes
~~~~~~~~~~

To describe a three-dimensional spot profile, a RAW file can be provided. It is recommended to be a 32 |nbsp| bit float volume with values between :code:`0` and :code:`1`, and should otherwise be re-normalized by the simulation software. The lowest value (0) means no intensity, the highest value (1) means maximum intensity. If specified, this method takes precedence over the first two described methods.

The :math:`x` direction of the given volume points along the :math:`\vec{u}` vector of the source coordinate system, :math:`y` points in direction :math:`\vec{v}`, and :math:`z` in direction :math:`\vec{w}`. The data type and volume dimensions need to be specified as well (see section \ref{sec:formats} about formats of referred data files for details). The volume shall be resized to match the :json:`"size":` of the spot volume, without necessarily retaining the original aspect ratio of the volume file.

.. code-block:: json-object
	:linenos:
	:lineno-start: 220

	"intensity_map": {
	  "file": "spot_intensities.raw",
	  "type": "float",
	  "dim_x": 100,
	  "dim_y": 100,
	  "dim_z": 100,
	  "drift": null
	}

.. _sec_spectrum:

Spectrum
--------

If the spectrum is to be calculated by the simulation software, the following three parameters decide whether only a monochromatic energy scenario is described, or a complete spectrum, with the ability to artificially turn on and off the components from Bremsstrahlung and characteristic emission from the target material. If :json:`"bremsstrahlung":` or :json:`"characteristic":` (or both) is set to :json:`true`, these take precedence over the monochromatic case.

.. code-block:: json-object
	:linenos:
	:lineno-start: 229

	"spectrum":
	{
	  "monochromatic": false,
	  "bremsstrahlung": true,
	  "characteristic": true,
	  "file": {"value": "tube_spectrum.csv", "drift": null}
	}

A spectrum can also be provided through a CSV file. This spectrum is assumed to be already filtered by the tube's window material, but not yet by any of the filters in front of the tube (as specified in section~\ref{sec:filters}). The CSV file should contain the columns listed in tab.~\ref{tab:csvSpectrum}, separated by commas or white-space.

.. _tab_csvSpectrum:

.. table:: CSV format for an X-ray spectrum

	==== =================================================
	Col. Property
	==== =================================================
	1    Photon energy in keV
	2    Number of photons in 1 / (s ⋅ sr ⋅ mA)
	3    Uncertainty in the number of photons *(optional)*
	==== =================================================

The energy values correspond to the centre of the histogram bins. The interpolation between the bin values shall not be specified here and is left to the simulation software. If a valid spectrum file is specified and the :json:`"file":` parameter is not set to :json:`null`, this has precedence over the spectrum calculated by the simulation software.

.. _sec_tube_filters:

Tube window and filters
-----------------------

The :json:`"window":` material(s) and the additional :json:`"filters":` in front of the tube are specified in two separate JSON arrays. For both, an arbitrary number of materials and thicknesses can be specified. If a source spectrum is provided in a file (see section~\ref{sec:spectrum}), the spectrum is assumed to be already filtered by all :json:`"window":` materials, but not yet by any :json:`"filters":`.

The :json:`"material_id":` refers to the material definition in the :json:`"materials":` section of the file (sec.~\ref{sec:materials}). Also, a window and filter :json:`"thickness":` must be provided.

.. code-block:: json-object
	:linenos:
	:lineno-start: 236

	"window":
	[
	  {
	    "material_id": "Al",
	    "thickness": {"value": 4.0, "unit": "mm", "uncertainty": {"value": 0, "unit": "mm"}, "drift": null}
	  }
	],
	"filters":
	[
	  {
	    "material_id": "Brass",
	    "thickness": {"value": 0.5, "unit": "mm", "uncertainty": {"value": 0, "unit": "mm"}, "drift": null}
	  },
	  {
	    "material_id": "Cu",
	    "thickness": {"value": 0.25, "unit": "mm", "uncertainty": {"value": 0, "unit": "mm"}, "drift": null}
	  }
	]