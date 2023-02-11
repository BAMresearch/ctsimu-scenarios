.. _sec_proprietary:

Software-specific properties
============================

If a simulation software requires additional information or simulation parameters, those software-specific properties can be provided in the section called :json:`"simulation"`. For each software, its own sub-section should be created.

.. code-block:: json-object
  :linenos:
  :lineno-start: 460

  "simulation": {
    "aRTist": {
      "multisampling_detector": {"value": "3x3"},
      "multisampling_spot": {"value": "30"},
      "spectral_resolution": {"value": 1, "unit": "keV"},
      "scattering_mcray_photons": {"value": 5e7},
      "scattering_image_interval": {"value": 5},
      "long_range_unsharpness": {
        "extension": {"value": 2, "unit":  "mm"},
        "ratio":     {"value": 10, "unit": "%"}
      },
      "primary_energies": false,
      "primary_intensities": false
    }
  }