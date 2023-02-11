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
  :lineno-start: 135

  "model":        "DT-1",
  "manufacturer": "Detector Company"

With the :json:`"type"` property, it can be defined whether an **ideal** or a **real** detector is described or shall be simulated. An **ideal** detector is assumed to convert all incident radiation energy linearly into gray values. For an **ideal** detector, no scintillator should be defined in the scenario file. A **real** detector is assumed to take the absorption characteristics and quantum yield of the scintillator material into account.

.. code-block:: json-object
  :linenos:
  :lineno-start: 137

  "type": "real",
  "type": "ideal"

The **number of detector pixels** in directions :math:`\vec{u}_\textsf{D}` and :math:`\vec{v}_\textsf{D}`:

.. code-block:: json-object
  :linenos:
  :lineno-start: 138

  "columns": {"value": 200, "unit": "px"},
  "rows":    {"value": 150, "unit": "px"},

The **pixel pitch** (distance between neighbouring pixels) in directions :math:`\vec{u}_\textsf{D}` and :math:`\vec{v}_\textsf{D}`. The physical dimensions of the active detector area are calculated from the pixel pitch and the number of pixels per row and column.

.. code-block:: json-object
  :linenos:
  :lineno-start: 140

  "pixel_pitch": {
    "u": {"value": 1.3, "unit": "mm"},
    "v": {"value": 1.3, "unit": "mm"}
  }

The **bit depth** of the detector:

.. code-block:: json-object
  :linenos:
  :lineno-start: 144

  "bit_depth": {"value": 16}

The **integration time** is the exposure time to take one frame. The **dead time** is the time between exposure times, which includes the readout time of the detector.

.. code-block:: json-object
  :linenos:
  :lineno-start: 145

  "integration_time": {"value": 0.5, "unit": "s"},
  "dead_time":        {"value": 50,  "unit": "ms"},

The **image lag** between subsequent frames can be specified, following loosely the definition of *GlobalLag1f* in ASTM E2597. :cite:p:`astm2597`

.. math::
  :label: eq_image_lag

  \textsf{image~lag} = \frac{\text{\textsf{Gray value at first frame radiation fully off}}}{\text{\textsf{Gray value at radiation fully on}}}

.. code-block:: json-object
  :linenos:
  :lineno-start: 147

  "image_lag": {"value": 0.05, "unit": null}

As opposed to *GlobalLag1f*, the image lag refers to the scenario described in this file, particularly the specified radiation intensity and integration time. Here, it is therefore not treated as a parameter intrinsic to the detector, but describes its lag characteristics only for the specified scenario.

.. _sec_gv_characteristics:

Gray value characteristics
--------------------------

There are three ways provided to model the gray value characteristics of the detector.

.. code-block:: json-object
  :linenos:
  :lineno-start: 148

  "gray_value": {
    "imax":   {"value": 45000},
    "imin":   {"value":   180},

    "factor": {"value": 1.8e13, "unit": "1/J"},
    "offset": {"value":    180, "unit": null},

    "intensity_characteristics_file": {"value": "detector_gray_values.tsv"},
    "efficiency_characteristics_file": {"value": "detector_efficiency.tsv"}
  }

Min/Max method
~~~~~~~~~~~~~~

The first approach is to specify the average gray value at the maximum intensity of the free beam in the parameter :json:`"imax"` and the average gray value at no incident radiation in the parameter :json:`"imin"`. Between these two values, a linear interpolation based on the incident intensity should take place to calculate the gray value of a pixel. The given values refer to the first frame of the CT scan and are not adapted to different condition in other frames. For example, if the tube current rises during the scan, the maximum free beam gray value in the projection image should rise as well.

Linear response function
~~~~~~~~~~~~~~~~~~~~~~~~

The second method allows to specify a linear response function. This function assigns a gray value to the collected energy E (in J) for each pixel.

.. math::
  :label: eq_grayValue

  \text{\textsf{Gray Value}} = \left(\textsf{factor} \cdot E \right) + \textsf{offset}

The file format allows to provide a :json:`"factor"` and an :json:`"offset"` for this linear function. This method allows the gray values to change with a change in pixel size, tube power, integration time or a change in intensity due to a different focus-detector distance.

This method has precedence over the first method if :json:`"factor"` and :json:`"offset"` are set and not :json:`null`. From eq. |nbsp| :math:numref:`eq_grayValue` it becomes clear that the :json:`"factor"` should have the inverse unit of the deposited energy: 1/J.

External characteristics file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For a more general approach, it is also possible to provide an arbitrary gray value characteristics from a CSV or TSV file specified by the parameter :json:`"intensity_characteristics_file"`. The file should contain the columns listed in :numref:`tab_csvDetectorIntensityCharacteristics`, separated by a comma or tab character.

A linear interpolation is assumed to take place between the given values. Therefore, if higher precision is required, a higher density of values should be provided in this file.

If a valid intensity characteristics CSV file is specified and the parameter is not set to :json:`null`, this method has precedence over the first two methods.

.. _tab_csvDetectorIntensityCharacteristics:

.. table:: Table structure for intensity characteristics files

  ====== =====================================
  Column Property
  ====== =====================================
  1      Energy *E* in J, collected by a pixel
  2      Gray value
  3      Gray value uncertainty *(optional)*
  ====== =====================================

.. _sec_detector_quantum_efficiency:

Quantum efficiency
~~~~~~~~~~~~~~~~~~

The photon **conversion efficiency** (quantum efficiency) of the detector can be provided as a characteristics curve from a file, using the parameter :json:`"efficiency_characteristics_file"`. This file should contain the columns listed in :numref:`tab_csvDetectorEfficiencyCharacteristics`, separated by a comma or tab character.

A linear interpolation is assumed to take place between the given values. Therefore, if higher precision is required, a higher density of values should be provided in this file.

The quantum efficiency is assumed to already take the detector's :ref:`window <sec_scintillator_and_filters>` into account, but not additional, external :ref:`filters <sec_scintillator_and_filters>`.

.. _tab_csvDetectorEfficiencyCharacteristics:

.. table:: Table structure for efficiency characteristics files

  ====== ========================================================================
  Column Property
  ====== ========================================================================
  1      Photon energy in keV
  2      Quantum efficiency, as the ratio of incident photons to absorbed photons
  3      Quantum efficiency uncertainty *(optional)*
  ====== ========================================================================

.. _sec_image_quality:

Image quality
-------------

.. _sec_noise:

Noise
~~~~~

The noise in the projection image can be described by the signal-to-noise ratio (SNR) at the maximum free-beam intensity for the first frame of the CT scan, with no frame averaging applied. This value can be specified in the parameter :json:`"snr_at_imax"`.

.. code-block:: json-object
  :linenos:
  :lineno-start: 158

  "noise": {
    "snr_at_imax": {"value": 205.3},
    "noise_characteristics_file": {"value": "detector_noise.tsv"}
  }

It is also possible to provide an intensity-dependent noise characteristic using a CSV or TSV file. A valid characteristics file has precedence over the SNR at maximum intensity. The characteristics file should contain the columns listed in :numref:`tab_csvDetectorNoiseCharacteristics`, separated by a comma or tab character.

.. _tab_csvDetectorNoiseCharacteristics:

.. table:: Table structure for noise characteristics files

  ====== =================================
  Column Property
  ====== =================================
  1      Mean pixel gray value
  2      Signal-to-noise ratio (SNR)
  3      SNR uncertainty *(optional)*
  ====== =================================

.. _sec_gain:

Gain
~~~~

A gain factor can be specified using the :json:`"gain"` parameter. It does not have to be a number, but can also be the name of the gain mode used. This differs between CT or detector manufacturers.

.. code-block:: json-object
  :linenos:
  :lineno-start: 162

  "gain": {"value": 3},

This parameter is only for documentation purposes. A simulation software is not expected to take this value into account. Instead, the provided gray value and noise characteristics are assumed to match the gain mode that is recorded here.

.. _sec_unsharpness:

Unsharpness
~~~~~~~~~~~

.. code-block:: json-object
  :linenos:
  :lineno-start: 163

  "unsharpness": {
    "basic_spatial_resolution": {"value": 0.1, "unit": "mm"},
    "mtf": {"value": "detector_mtf.tsv"}
  }

There are two ways provided to specify the detector unsharpness:

1. The **basic spatial resolution,** as defined in ASTM E2597 :cite:p:`astm2597`, provided using the parameter :json:`"basic_spatial_resolution"`.
2. The **modulation transfer function** (MTF, :cite:p:`rossmann_point_1969`), provided through a CSV or TSV file. The file name can be given in the parameter :json:`"mtf"`. It should contain the columns listed in :numref:`tab_csvMTF`, separated by comma or tab characters. If a valid MTF is provided, this has precedence over the basic spatial resolution.

.. _tab_csvMTF:

.. table:: Table structure for MTF files

  ====== =============================================
  Column Property
  ====== =============================================
  1      Frequency in lp/mm
  2      Modulation contrast, from the interval [0, 1]
  3      Modulation contrast uncertainty *(optional)*
  ====== =============================================

.. _sec_bad_pixel_map:

Bad pixel map
~~~~~~~~~~~~~

The bad pixel map provided here should be a 2D gray-scale image file with a signed data type (:code:`int8`, :code:`int16`, :code:`float32` or :code:`float64`) with a number of columns and rows that matches the detector. A pixel gray value of :code:`-1` means that the pixel is working properly. A pixel gray value other than :code:`-1` means that the pixel does not function correctly and its value is instead replaced by the provided gray value from the bad pixel map.

.. code-block:: json-object
  :linenos:
  :lineno-start: 167

  "bad_pixel_map": {
    "file": {"value": "badpixels.raw", "drifts": null},
    "type": "int16",
    "endian": "little",
    "headersize": 0
  }

.. _sec_scintillator_and_filters:

Scintillator, window & filters
------------------------------

In this section, the scintillator and filter materials for the detector can be defined. The window and filter materials are split into :json:`"front"` and :json:`"rear"` components (e.g., to use as a back panel, mostly to consider backscattering). Any number of windows and filters can be defined. For the materials, only a material ID is given here. The actual material definition and declaration of its chemical composition is found in the :ref:`materials section <sec_materials>` of the JSON file.

The :json:`"window"` materials refer to the detector's built-in components, whereas :json:`"filters"` are assumed to be additional components that are not originally part of the detector housing. This distinction is made because the detector's :ref:`quantum efficiency <sec_detector_quantum_efficiency>` (which can be defined in the :json:`"efficiency_characteristics_file"`) already takes the window material into account, but none of the additional, external filters.

Note that front and rear of the detector are not explicitly identified by the detector's normal vector or any other property, but only given implicitly by the side of the detector facing the source.

.. code-block:: json-object
  :linenos:
  :lineno-start: 173

  "scintillator": {
    "material_id": "CsI",
    "thickness": {"value": 0.15, "unit": "mm"}
  },
  "window": {
    "front": [
      {
        "material_id": "Kapton",
        "thickness": {"value": 0.13, "unit": "mm"}
      }
    ],
    "rear": []
  },
  "filters": {
    "front": [
      {
        "material_id": "Al",
        "thickness": {"value": 0.2, "unit": "mm"}
      },
      {
        "material_id": "Cu",
        "thickness": {"value": 0.1, "unit": "mm"}
      }
    ],
    "rear": [
      {
        "material_id": "Al",
        "thickness": {"value": 2.0, "unit": "mm"}
      }
    ]
  }