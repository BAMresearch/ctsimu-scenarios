.. _sec_geometry:

Geometry
========

.. _sec_geometry_placement_in_world:

Placement of objects in the world coordinate system
---------------------------------------------------

.. _fig_coordinates:
.. figure:: pictures/geometry.*
	:width: 90%

	World coordinate system {x, |nbsp| y, |nbsp| z} and local coordinate systems {u, |nbsp| v, |nbsp| w}.

This specification does not define a fixed coordinate system for the CT set-up. The only assumption is that a right-handed world coordinate system {x, |nbsp| y, |nbsp| z} is used, and the local coordinate systems {u, |nbsp| v, |nbsp| w} of source, detector and sample stage are to be placed in this world coordinate system. :numref:`fig_coordinates` illustrates the set-up that is used in the following examples.

The :json:`"geometry":` section has three subsections to define the location and orientation of the principal CT scanner components: :json:`"detector":`, :json:`"source":` and :json:`"stage":`. They all share a common set of JSON properties for positioning, and a very similar description is used later on to place samples into the scene (see :ref:`sample positioning <sec_sample_positioning>`). The placement description generally consists of the following parts:

:json:`"centre":`
	specifies the object's centre (x, |nbsp| y, |nbsp| z) in the world coordinate system, i.e. the geometric centre of its bounding box. The bounding box is defined as the smallest cuboid (or rectangle, for 2D objects) that completely encloses the object, under the condition that the cuboid's edges are each strictly parallel to one of the coordinate axes of the object's own Cartesian coordinate system. The :json:`"centre":` is the origin of the local coordinate system {u, |nbsp| v, |nbsp| w} and also the pivot point for rotations.

:json:`"vector_u":` and :json:`"vector_w":`
	specify the object's orientation by defining the basis vectors :math:`\vec{u}` and :math:`\vec{w}` of the local coordinate system in terms of the world coordinate system {x, |nbsp| y, |nbsp| z}. They are not required to be unit vectors, but they must be **orthogonal.**

	:math:`\vec{w}` is usually meant to be a normal vector, and :math:`\vec{u}` is one of the support vectors. :math:`\vec{u}` and :math:`\vec{v}` also serve a second meaning as row and column vector of the resulting projection (for the detector) or of a given spot intensity profile image (for the source). See the descriptions below for details.

:json:`"rotation":`
	specifies small rotational deviations from the ideal geometry, such as tilts of the detector or the rotation axis. A simulation software should treat them as subsequent transformations of the initial local coordinate system. Whether these deviations are known to the reconstruction software or not depends on the purpose of the scenario and can be specified by setting the property :json:`"known_to_reconstruction":` to either :json:`true` or :json:`false`:

	.. code-block:: json-object
		:linenos:
		:lineno-start: 47

		"known_to_reconstruction": true

	:json:`"u":`, :json:`"v":` and :json:`"w":`
	specify small rotation angles around the axes of the **local** coordinate system. The convention here sticks to :math:`wv^{\prime}u^{\prime\prime}` for subsequent rotations, which means that the rotation around the :math:`\vec{w}` vector is performed first, then a rotation around the new :math:`\vec{v}^\prime` vector, and finally the rotation around the resulting :math:`\vec{u}^{\prime\prime}` vector. In the case of samples, their order of rotation takes place in the same manner: :math:`ts^{\prime}r^{\prime\prime}` (see :ref:`sample positioning <sec_sample_positioning>`).

	Note that the angular deviations specified here always describe a **static** deviation of the initial coordinate system (at frame |nbsp| 0). They are not applied individually at each frame, which means that a stage tilt described here is meant to stay constant throughout the scan and does not describe a wobble. For dynamic deviations, the :ref:`drift property <sec_drifts>` of parameters can be used, as drifts are applied for each frame individually after the stage has reached its intended frame position.


.. _sec_geometry_detector:

Detector
--------

For this specification, in general, vectors :math:`\vec{u}` and :math:`\vec{v}` designate an item's in-plane vectors, whereas :math:`\vec{w}` usually designates a normal vector. Following this convention, :math:`\vec{u}_\textsf{D}` is the detector's **row vector,** pointing from left to right in the resulting projection image (as seen on a computer screen with a pixel coordinate system that has its origin in the upper left corner). :math:`\vec{v}_\textsf{D}` is the detector's **column vector,** pointing from top to bottom in the resulting projection image. The orientation of these two vectors directly determines the orientation of the projection image.

Note that for any object only the normal vector :math:`\vec{w}` and the support vector :math:`\vec{u}` are given in the JSON file. The detector normal :math:`\vec{w}_\textsf{D}` does not have any special meaning and should be arranged such that the detector's row and column vector point in the desired directions.

The size and further properties of the detector are defined later on in the :ref:`detector section <sec_detector>` of the JSON file.

.. code-block:: json-object
	:linenos:
	:lineno-start: 24

	"detector":
	{
	  "centre": {
	    "x": {"value": 400, "unit": "mm", "uncertainty": {"value": 0, "unit": "mm"}, "drift": null},
	    "y": {"value":   0, "unit": "mm", "uncertainty": {"value": 0, "unit": "mm"}, "drift": null},
	    "z": {"value":   0, "unit": "mm", "uncertainty": {"value": 0, "unit": "mm"}, "drift": null}
	  },

	  "vector_u": {
	    "x": {"value":  0, "drift": null},
	    "y": {"value": -1, "drift": null},
	    "z": {"value":  0, "drift": null}
	  },
	  "vector_w": {
	    "x": {"value":  1, "drift": null},
	    "y": {"value":  0, "drift": null},
	    "z": {"value":  0, "drift": null}
	  },

	  "rotation": {
	    "u": {"value": 0,      "unit": "rad", "uncertainty": {"value": 0, "unit": "rad"}, "drift": null},
	    "v": {"value": 0,      "unit": "rad", "uncertainty": {"value": 0, "unit": "rad"}, "drift": null},
	    "w": {"value": 2.3e-2, "unit": "rad", "uncertainty": {"value": 0, "unit": "rad"}, "drift": null},
	    "known_to_reconstruction": true
	  }
	}


.. _sec_geometry_source:

Source
------

The source can be modelled either as a cone-beam geometry or a parallel beam geometry. This behaviour is set by the :json:`"type":` property, which can be either :json:`"cone"` or :json:`"parallel"`.

.. code-block:: json-object
	:linenos:
	:lineno-start: 53

	"type": "cone" "parallel"

In the case of a parallel beam, its divergence can be specified along both planar axes of the source:

.. code-block:: json-object
	:linenos:
	:lineno-start: 54

	"beam_divergence": {
		"u": {"value": 0, "unit": "rad", "uncertainty": {"value": 0, "unit": "rad"}, "drift": null},
		"v": {"value": 0, "unit": "rad", "uncertainty": {"value": 0, "unit": "rad"}, "drift": null}
	}

For a cone beam geometry, this property should be set to :json:`null`:

.. code-block:: json-object
	:linenos:
	:lineno-start: 54

	"beam_divergence": null

Spatially extended source intensity profiles are modelled as a rectangle. For cone-beam geometries, this will be a very small rectangle on the size scale of the spot size.

For parallel beam geometries, the optical axis of the system is assumed to be the :math:`\vec{w}_\textsf{F}` axis of the source, and all rays should be parallel to this axis (apart from beam divergence). This means that the source rectangle in the model should ideally be of a size such that the entire detector is covered by radiation.

If a spot intensity profile is given as an image (see :ref:`source <sec_spot_2d_images>` for details), :math:`\vec{u}_\textsf{F}` is the image's row vector, pointing from left to right in this image, and :math:`\vec{v}_\textsf{F}` is the image's column vector, pointing from top to bottom.

To allow the correct orientation of the intensity profile image, the vector :math:`\vec{w}_\textsf{F}` does not necessarily point in the main direction of radiation, but could also point in the opposite direction (due to the restraint of a right-handed coordinate system).

Within the WIPANO CTSimU project, we agreed to the convention of placing the source at (0, |nbsp| 0, |nbsp| 0). It is not a requirement.

.. code-block:: json-object
	:linenos:
	:lineno-start: 51

	"source":
	{
	  "type": "cone",
	  "beam_divergence": {
	    "u": {"value": 0, "unit": "rad", "uncertainty": {"value": 0, "unit": "rad"}, "drift": null},
	    "v": {"value": 0, "unit": "rad", "uncertainty": {"value": 0, "unit": "rad"}, "drift": null}
	  },

	  "centre": {
	    "x": {"value": 0, "unit": "mm", "uncertainty": {"value": 0, "unit": "mm"}, "drift": null},
	    "y": {"value": 0, "unit": "mm", "uncertainty": {"value": 0, "unit": "mm"}, "drift": null},
	    "z": {"value": 0, "unit": "mm", "uncertainty": {"value": 0, "unit": "mm"}, "drift": null}
	  },

	  "vector_u": {
	    "x": {"value":  0, "drift": null},
	    "y": {"value": -1, "drift": null},
	    "z": {"value":  0, "drift": null}
	  },
	  "vector_w": {
	    "x": {"value":  1, "drift": null},
	    "y": {"value":  0, "drift": null},
	    "z": {"value":  0, "drift": null}
	  },

	  "rotation": {
	    "u": {"value": 0, "unit": "rad", "uncertainty": {"value": 0, "unit": "rad"}, "drift": null},
	    "v": {"value": 0, "unit": "rad", "uncertainty": {"value": 0, "unit": "rad"}, "drift": null},
	    "w": {"value": 0, "unit": "rad", "uncertainty": {"value": 0, "unit": "rad"}, "drift": null},
	    "known_to_reconstruction": true
	  }
	}


.. _sec_geometry_stage:

Stage
-----

The normal vector :math:`\vec{w}_\textsf{O}` of the sample stage specifies the axis of rotation for the CT scan. By default, the sample stage coordinate system and all samples attached to it are meant to rotate around this axis, whereas the source and detector stay still (as for typical industrial CT scanners).

Samples that are placed in the stage coordinate system all take part in the rotation of the sample stage. Samples that are placed in the world coordinate system are fixed during the CT scan (i.e. fixed relative to source and detector, see :ref:`samples <sec_samples>` for details).

.. code-block:: json-object
	:linenos:
	:lineno-start: 84

	"stage":
	{
	  "centre": {
	    "x": {"value": 275, "unit": "mm", "uncertainty": {"value": 0, "unit": "mm"}, "drift": null},
	    "y": {"value":   0, "unit": "mm", "uncertainty": {"value": 0, "unit": "mm"}, "drift": null},
	    "z": {"value":   0, "unit": "mm", "uncertainty": {"value": 0, "unit": "mm"}, "drift": null}
	  },

	  "vector_u": {
	    "x": {"value":  1, "drift": null},
	    "y": {"value":  0, "drift": null},
	    "z": {"value":  0, "drift": null}
	  },
	  "vector_w": {
	    "x": {"value":  0, "drift": null},
	    "y": {"value":  0, "drift": null},
	    "z": {"value":  1, "drift": null}
	  },

	  "rotation": {
	    "u": {"value":  0, "unit": "rad", "uncertainty": {"value": 0, "unit": "rad"}, "drift": null},
	    "v": {"value":  0, "unit": "rad", "uncertainty": {"value": 0, "unit": "rad"}, "drift": null},
	    "w": {"value":  0, "unit": "rad", "uncertainty": {"value": 0, "unit": "rad"}, "drift": null},
	    "known_to_reconstruction": true
	  }
	}
