.. _sec_samples:

Samples
=======

.. _sec_samples_general:

General properties
------------------

Any number of samples can be defined in the :json:`"samples":` array and placed in the scene, either :ref:`attached to the rotating sample stage <sec_sample_in_stage_coordinates>`, or :ref:`fixed to the world coordinate system <sec_sample_in_world_coordinates>`. A sample object has the following properties.

The sample name:

.. code-block:: json-object
	:linenos:
	:lineno-start: 259

	"name": "Step Cylinder"

A reference to the model file (e.g. STL or CAD file) that describes the sample geometry:

.. code-block:: json-object
	:linenos:
	:lineno-start: 260

	"file": {"value": "stepCyl.stl", "drift": null}

The unit of length that is used in the model file:

.. code-block:: json-object
	:linenos:
	:lineno-start: 261

	"unit": "mm"

A scaling factor for each axis of the sample coordinate system, if the model should be resized by a constant factor:

.. code-block:: json-object
	:linenos:
	:lineno-start: 262

	"scaling_factor": {
	  "r": {"value": 1.0, "drift": null},
	  "s": {"value": 1.0, "drift": null},
	  "t": {"value": 1.0, "drift": null}
	}

The material of the sample, given by a :json:`"material_id":` that references a material definition in the material section of the file:

.. code-block:: json-object
	:linenos:
	:lineno-start: 267

	"material_id": "Glass Ceramic"

.. _sec_sample_positioning:

Sample positioning
------------------

.. _sec_sample_in_stage_coordinates:

Sample attached to the stage coordinate system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The sample coordinate system {r, |nbsp| s, |nbsp| t} is equivalent to the surface model's proper {x, |nbsp| y, |nbsp| z} coordinate system (except for the location of the origin). It is specific to each sample and can be placed in the stage coordinate system by providing its centre coordinates in terms of {u, |nbsp| v, |nbsp| w}\ :sub:`O` (see :numref:`fig_sampleCoordinates` for an illustration). If done so, the sample is attached to the stage and will follow any rotations and translations performed by the stage during the CT scan.

The description follows the convention that has been established for the :ref:`placement of objects in the world coordinate system <sec_geometry_placement_in_world>`, with the following sub-elements of the sample's :json:`"position":` property.

.. code-block:: json-object
	:linenos:
	:lineno-start: 270

	"centre": {
	  "u": {"value":  0, "unit": "mm", "uncertainty": {"value": 0, "unit": "mm"}, "drift": null},
	  "v": {"value": 20, "unit": "mm", "uncertainty": {"value": 0, "unit": "mm"}, "drift": null},
	  "w": {"value":  0, "unit": "mm", "uncertainty": {"value": 0, "unit": "mm"}, "drift": null}
	}

.. _fig_sampleCoordinates:
.. figure:: pictures/sample.*
	:width: 60%

	World coordinate system {x, |nbsp| y, |nbsp| z}, stage coordinate system {u, |nbsp| v, |nbsp| w}\ :sub:`O` and sample coordinate system {r, |nbsp| s, |nbsp| t}.

To define the sample's orientation, its :math:`\vec{r}` and :math:`\vec{t}` vector must also be expressed in terms of the stage coordinate system {u, |nbsp| v, |nbsp| w}\ :sub:`O`\ :

.. code-block:: json-object
	:linenos:
	:lineno-start: 277

	"vector_r": {
	  "u": {"value":  1,   "drift": null},
	  "v": {"value":  0,   "drift": null},
	  "w": {"value":  0,   "drift": null}
	},
	"vector_t": {
	  "u": {"value":  0,   "drift": null},
	  "v": {"value": -0.2, "drift": null},
	  "w": {"value":  1,   "drift": null}
	}

In analogy to the rotational deviations of the source, stage and detector (see :ref:`geometry <sec_geometry>`), the sample's rotational deviations should also be expressed in terms of the **sample coordinate system.** Rotations are meant to be applied in the following manner: :math:`ts^{\prime}r^{\prime\prime}` which means that the rotation around the sample's :math:`\vec{t}` axis is performed first, followed by the rotation around the new :math:`\vec{s}^{\prime}` axis, and finally the rotation around the resulting :math:`\vec{r}^{\prime\prime}` axis.

.. code-block:: json-object
	:linenos:
	:lineno-start: 287

	"rotation": {
	  "r": {"value": 0, "unit": "rad", "uncertainty": {"value": 0, "unit": "rad"}, "drift": null},
	  "s": {"value": 0, "unit": "rad", "uncertainty": {"value": 0, "unit": "rad"}, "drift": null},
	  "t": {"value": 0, "unit": "rad", "uncertainty": {"value": 0, "unit": "rad"}, "drift": null}
	}

.. _sec_sample_in_world_coordinates:

Fixed sample position in the world coordinate system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the sample is placed in the fixed world coordinate system, it will not follow any motions performed by the sample stage, but it will stay fixed relative to source and detector.

The description is very similar to placing a sample in the stage coordinate system, as described in the :ref:`previous section <sec_sample_in_stage_coordinates>`. The only difference is that the object's centre and basis vectors :math:`\vec{r}` and :math:`\vec{t}` are now expressed in terms of the world coordinate system {x, |nbsp| y, |nbsp| z}, just like it is done for the source and detector. The rotational deviations are still described in the sample coordinate system {r, |nbsp| s, |nbsp| t}. The following listing gives an example of an aluminium frame around the sample stage that is fixed to the world coordinate system.

.. code-block:: json-object
	:linenos:
	:lineno-start: 295

	"name": "Attachment Frame",
	"file": {"value": "frame.stl", "drift": null},
	"unit": "mm",
	"scaling_factor": {
	  "r": {"value": 1.0, "drift": null},
	  "s": {"value": 1.0, "drift": null},
	  "t": {"value": 1.0, "drift": null}
	},
	"material_id": "Al",
	"position":
	{
	  "centre": {
	    "x": {"value": 275, "unit": "mm", "uncertainty": {"value": 0, "unit": "mm"}, "drift": null},
	    "y": {"value":   0, "unit": "mm", "uncertainty": {"value": 0, "unit": "mm"}, "drift": null},
	    "z": {"value":   0, "unit": "mm", "uncertainty": {"value": 0, "unit": "mm"}, "drift": null}
	  },

	  "vector_r": {
	    "x": {"value":  1, "drift": null},
	    "y": {"value":  0, "drift": null},
	    "z": {"value":  0, "drift": null}
	  },
	  "vector_t": {
	    "x": {"value":  0, "drift": null},
	    "y": {"value":  1, "drift": null},
	    "z": {"value":  0, "drift": null}
	  },

	  "rotation": {
	    "r": {"value": 0, "unit": "rad", "uncertainty": {"value": 0, "unit": "rad"}, "drift": null},
	    "s": {"value": 0, "unit": "rad", "uncertainty": {"value": 0, "unit": "rad"}, "drift": null},
	    "t": {"value": 0, "unit": "rad", "uncertainty": {"value": 0, "unit": "rad"}, "drift": null}
	  }
	}
