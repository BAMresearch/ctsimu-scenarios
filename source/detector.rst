.. _sec_detector:

Detector
========

.. _sec_detector_general:

General properties
------------------

The following properties can be specified in the detector section of the scenario file.

The model name and the manufacturer, if an existing detector is modelled:

.. code-block:: json-object
	:linenos:
	:lineno-start: 114

	"model":        "",
	"manufacturer": ""

Using the :json:`"type":` keyword, it can be defined whether an **ideal** or a **real** detector is described or shall be simulated. An **ideal** detector is assumed to convert all incident radiation energy linearly into grey values. For an **ideal** detector, no scintillator should be defined in the scenario file. A **real** detector is assumed to take the absorption characteristics and quantum yield of the scintillator material into account.

.. code-block:: json-object
	:linenos:
	:lineno-start: 116

	"type": "real" "ideal"

The number of detector pixels in directions :math:`\vec{u}_\textsf{D}` and :math:`\vec{v}_\textsf{D}`:

.. code-block:: json-object
	:linenos:
	:lineno-start: 117

	"columns": {"value": 2000, "unit": "px"},
	"rows":    {"value": 1500, "unit": "px"}

The pixel pitch (distance between neighbouring pixels) in directions :math:`\vec{u}_\textsf{D}` and :math:`\vec{v}_\textsf{D}`. The physical dimensions of the active detector area are calculated from the pixel pitch and the number of pixels per row and column.

.. code-block:: json-object
	:linenos:
	:lineno-start: 119

	"pixel_pitch": {
	  "u": {"value": 0.127, "unit": "mm", "uncertainty": {"value": 0, "unit": "mm"}, "drift": null},
	  "v": {"value": 0.127, "unit": "mm", "uncertainty": {"value": 0, "unit": "mm"}, "drift": null}
	}

The bit depth of the detector:

.. code-block:: json-object
	:linenos:
	:lineno-start: 123

	"bit_depth": {"value": 16}


The integration time is the exposure time to take one frame. The dead time is the time between exposure times, which includes the readout time of the detector.

.. code-block:: json-object
	:linenos:
	:lineno-start: 124

	"integration_time": {"value": 0.5, "unit": "s", "uncertainty": {"value": 0, "unit": "s"}, "drift": null},
	"dead_time":        {"value": 50, "unit": "ms", "uncertainty": {"value": 0, "unit": "s"}, "drift": null}

The :json:`"image_lag":` between subsequent frames can be specified, following loosely the definition of *GlobalLag1f* in ASTM E2597. :cite:p:`astm2597`

.. math::
	:label: eq_image_lag

	\textsf{image~lag} = \frac{\text{\textsf{Grey value at first frame radiation fully off}}}{\text{\textsf{Grey value at radiation fully on}}}

.. code-block:: json-object
	:linenos:
	:lineno-start: 126

	"image_lag": {"value": 0.05, "unit": null, "uncertainty": {"value": 0, "unit": null}, "drift": null}

As opposed to *GlobalLag1f*, :json:`"image_lag":` refers to the scenario described in this file, particularly the specified radiation intensity and integration time. Here, it is therefore not treated as a parameter intrinsic to the detector, but describes its lag characteristics only for the specified scenario.

.. _sec_gv_characteristics:

Grey value characteristics
--------------------------

There are three ways provided to model the grey value characteristics of the detector.

.. code-block:: json-object
	:linenos:
	:lineno-start: 127

	"grey_value":
	{
	  "imax":   {"value": 45000, "drift": null},
	  "imin":   {"value":  1000, "drift": null},

	  "factor": {"value": 3e15, "unit": "1/J", "uncertainty": {"value": 0, "unit": "1/J"}, "drift": null},
	  "offset": {"value": 1800, "unit": null,  "uncertainty": {"value": 0, "unit": null}, "drift": null},

	  "intensity_characteristics_file": {"value": "detector_intensity.csv", "drift": null},

	  "efficiency":   {"value": 0.7, "unit": null, "uncertainty": {"value": 0, "unit": null}, "drift": null},
	  "efficiency_characteristics_file": {"value": "detector_efficiency.csv", "drift": null}
	}

Min/Max method
~~~~~~~~~~~~~~

The first approach is to specify the average grey value at the maximum intensity of the free beam in the parameter :json:`"imax":`, and the average grey value at no incident radiation in the parameter :json:`"imin":`. Between these two values, a linear interpolation based on the incident intensity should take place to calculate the grey value of a pixel. In this case, the grey values are invariant under changes in the integration time or pixel size, and will be rescaled along with changes in the minimum or maximum intensity. It is similar to the re-normalization of the projection image to a specific grey value at maximum free-beam intensity.

Linear response function
~~~~~~~~~~~~~~~~~~~~~~~~

The second method allows to specify a linear response function. This function assigns a grey value to the collected energy E (in J) for each pixel.

.. math::
	:label: eq_greyValue

	\text{\textsf{Grey Value}} = \left(\textsf{factor} \cdot E \right) + \textsf{offset}

The file format allows to provide a :json:`"factor":` and an :json:`"offset":` for this linear function. This method allows the grey values to change with a change in pixel size, tube power, integration time or a change in intensity due to a different focus-detector distance. It has precedence over the first method if :json:`"factor":` and :json:`"offset":` are set and not :json:`"null":`. From eq. |nbsp| :math:numref:`eq_greyValue` it becomes clear that the :json:`"factor":` should have the inverse unit of the deposited energy: 1/J.

External characteristics file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For a more general approach, it is also possible to provide an arbitrary grey value characteristics from a CSV file specified by the parameter :json:`"intensity_characteristics_file":`. The file should contain the columns listed in :numref:`tab_csvDetectorIntensityCharacteristics`, separated by commas or white space.

The interpolation method between these discrete values shall not be specified here and is left to the simulation software. However, all values are assumed to refer to the centre of their bin.

If a valid intensity characteristics CSV file is specified and the parameter is not set to :json:`"null":`, this method has precedence over the first two methods.

.. _tab_csvDetectorIntensityCharacteristics:

.. table:: CSV for detector's intensity characteristics

	==== =====================================
	Col. Property
	==== =====================================
	1    Energy *E* in J, collected by a pixel
	2    Grey value
	3    Grey value uncertainty *(optional)*
	==== =====================================

Quantum efficiency
~~~~~~~~~~~~~~~~~~

The photon **conversion efficiency** (quantum efficiency) of the detector can also either be provided as a constant value for all photon energies -- using the parameter :json:`"efficiency":` -- or as another characteristics curve through a CSV file, using the parameter :json:`"efficiency_characteristics_file":`. In the latter case, this file should contain the columns listed in :numref:`tab_csvDetectorEfficiencyCharacteristics`, separated by commas or white space. If a valid efficiency characteristics file is provided, it has precedence over the global :json:`"efficiency":` property.

.. _tab_csvDetectorEfficiencyCharacteristics:

.. table:: CSV for detector's efficiency characteristics

	==== ========================================================================
	Col. Property
	==== ========================================================================
	1    Photon energy in keV
	2    Quantum efficiency, as the ratio of incident photons to absorbed photons
	3    Quantum efficiency uncertainty *(optional)*
	==== ========================================================================

.. _sec_image_quality:

Image Quality
-------------

.. _sec_noise:

Noise
~~~~~

The noise in the projection image can be described by specifying the signal-to-noise ratio (SNR) at the maximum intensity (free beam) for one frame, with no frame averaging applied.

.. code-block:: json-object
	:linenos:
	:lineno-start: 140

	"noise":
	{
	  "snr_at_imax": {"value": 205, "unit": null, "uncertainty": {"value": 0, "unit": null}, "drift": null},
	  "noise_characteristics_file": {"value": "noise.csv", "drift": null}
	}

Note that the SNR's underlying grey value distribution must refer to an area of pixels that ideally has the same mean intensity, and is not subject to systematic grey value variations from other physical effects such as the :math:`1/r^2` law or a change in the angle of radiation incidence on the detector.

It is also possible to provide an intensity-dependent noise characteristics using a CSV file. A valid characteristics file has precedence over the SNR at maximum intensity. The characteristics file should contain the columns listed in :numref:`tab_csvDetectorNoiseCharacteristics`, separated by commas or white space.

.. _tab_csvDetectorNoiseCharacteristics:

.. table:: CSV for noise characteristics

	==== =================================
	Col. Property
	==== =================================
	1    Mean pixel grey value (intensity)
	2    Signal-to-noise ratio (SNR)
	3    SNR uncertainty *(optional)*
	==== =================================

.. _sec_gain:

Gain
~~~~

A gain factor can be specified using the :json:`"gain":` parameter:

.. code-block:: json-object
	:linenos:
	:lineno-start: 145

	"gain":
	{
	  "value": 3,
	  "drift": null,
	  "scale_signal_and_noise": true
	}

If the parameter :json:`"scale_signal_and_noise":` is set to :json:`true`, a simulation software shall use this parameter to scale the grey values (usually linearly), and noise (usually quadratically) with the gain value. This assumes that the grey value characteristics and noise characteristics that have been provided before refer to a gain factor of 1. If the grey value and noise characteristics are already provided for the given gain factor, the parameter must be set to :json:`false`.

.. _sec_unsharpness:

Unsharpness
~~~~~~~~~~~

There are three ways provided to specify the detector unsharpness.

.. code-block:: json-object
	:linenos:
	:lineno-start: 151

	"unsharpness":
	{
	  "basic_spatial_resolution": {"value": 0.1, "unit": "mm", "uncertainty": {"value": 0, "unit": "mm"},        "drift": null},
	  "mtf10_frequency": {"value": 10, "unit": "lp/mm", "uncertainty": {"value": 1, "unit": "lp/mm"},            "drift": null},
	  "mtf": {"value": "detector_mtf.csv", "drift": null}
	}


1. The basic spatial resolution, as defined in ASTM E2597 :cite:p:`astm2597`, provided using the parameter :json:`"basic_spatial_resolution":`.
2. The MTF10 frequency of the system's modulation transfer function (MTF). This value states the frequency at which the contrast in the detector response drops to 10% :cite:p:`rossmann_point_1969`. It can be provided using the parameter :json:`"mtf10_frequency":`. If specified and not :json:`null`, this parameter has precedence over the basic spatial resolution.
3. The complete modulation transfer function (MTF, :cite:p:`rossmann_point_1969`), provided through a CSV file. Its name is given using the parameter :json:`"mtf":`, and it should contain the columns listed in tab.~\ref{tab:csvMTF}, separated by commas or white space. If a valid MTF is provided, this has precedence over the first two parameters mentioned here.

.. _tab_csvMTF:

.. table:: CSV for noise characteristics

	==== =============================================
	Col. Property
	==== =============================================
	1    Frequency in lp/mm
	2    Modulation contrast, from the interval [0, 1]
	3    Modulation contrast uncertainty *(optional)*
	==== =============================================


Bad pixel map
~~~~~~~~~~~~~

The bad pixel map provided here should be a 2D grey-scale image file with a number of columns and rows that matches the detector. A pixel value of :code:`0` means that the pixel is working properly. A pixel value other than :code:`0` means that the pixel does not function correctly. If a TIFF file is provided, the :json:`"type":` property is obsolete and can be omitted.

.. code-block:: json-object
	:linenos:
	:lineno-start: 157

	"bad_pixel_map":
	{
	  "value": "badpixels.raw",
	  "type": "uint8",
	  "drift": null
	}

.. _sec_scintillatorAndFilters:

Scintillator & Filters
----------------------

In this section, the scintillator and filter materials for the detector can be defined. The filter materials are split into :json:`"front":` filters and :json:`"rear":` filters (i.e. a back panel, mostly to consider backscattering). Any number of filters can be defined. For the materials of scintillator and filters, only a material ID is given here. The actual material definition and declaration of its chemical composition is found in the (materials~\ref{sec:materials}) section of the JSON file.

Note that front and rear of the detector are not explicitly identified by the detector's normal vector or any other property, but only given implicitly by the side of the detector facing the source, and the side facing away from the source.

.. code-block:: json-object
	:linenos:
	:lineno-start: 163

	"scintillator":
	{
	  "material_id": "CsI",
	  "thickness": {"value": 0.15, "unit": "mm", "uncertainty": {"value": 0, "unit": "mm"}, "drift": null}
	},
	"filters":
	{
	  "front":
	  [
	    {
	      "material_id": "Al",
	      "thickness": {"value": 0.2, "unit": "mm", "uncertainty": {"value": 0, "unit": "mm"}, "drift": null}
	    },
	    {
	      "material_id": "Kapton",
	      "thickness": {"value":0.13, "unit": "mm", "uncertainty": {"value": 0, "unit": "mm"}, "drift": null}
	    }
	  ],
	  "rear":
	  [
	    {
	      "material_id": "Al",
	      "thickness": {"value": 2.0, "unit": "mm", "uncertainty": {"value": 0, "unit": "mm"}, "drift": null}
	    }
	  ]
	}