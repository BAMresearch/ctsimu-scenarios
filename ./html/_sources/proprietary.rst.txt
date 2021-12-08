.. _sec_proprietary:

Software-specific properties
============================

If a simulation software requires additional information or simulation parameters, those software-specific properties can be provided in the section called :json:`"simulation":`. For each software, its own sub-section should be created.

.. code-block:: json-object
	:linenos:
	:lineno-start: 410

	"simulation":
	{
	  "aRTist":
	  {
	    "multisampling_detector": {"value": null, "drift": null},
	    "multisampling_spot": {"value": "30", "drift": null},
	    "scattering_mcray_photons": {"value": "5e+007", "drift": null},
	    "long_range_unsharpness":
	    {
	      "extension": {"value": 2, "unit":  "mm", "drift": null},
	      "ratio":     {"value": 10, "unit": "%", "drift": null}
	    }
	  }
	}