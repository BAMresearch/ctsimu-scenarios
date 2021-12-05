.. _geometry:

Geometry
========

Placement of objects in the world coordinate system
---------------------------------------------------

.. _fig_coordinates:
.. figure:: pictures/geometry.*
	:width: 90%

	World coordinate system {x, |nbsp| y, |nbsp| z} and local coordinate systems {u, |nbsp| v, |nbsp| w}.

This specification does not define a fixed coordinate system for the CT set-up. The only assumption is that a right-handed world coordinate system {x, |nbsp| y, |nbsp| z} is used, and the local coordinate systems {u, |nbsp| v, |nbsp| w} of source, detector and sample stage are to be placed in this world coordinate system. :numref:`fig_coordinates` illustrates the set-up that is used in the following examples.

The :json:`"geometry":` section has three subsections to define the location and orientation of the principal CT scanner components: :json:`"detector":`, :json:`"source":` and :json:`"stage":`. They all share a common set of JSON properties for positioning (described in sec.~\ref{sec:geometry_detector}, \ref{sec:geometry_source} and \ref{sec:geometry_stage}), and a very similar description is used later on to place samples into the scene (sec.~\ref{sec:samplePositioning}). The placement description generally consists of the following parts:

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
	specify small rotation angles around the axes of the **local** coordinate system. The convention here sticks to :math:`wv^{\prime}u^{\prime\prime}` for subsequent rotations, which means that the rotation around the :math:`\vec{w}` vector is performed first, then a rotation around the new :math:`\vec{v}^\prime` vector, and finally the rotation around the resulting :math:`\vec{u}^{\prime\prime}` vector. In the case of samples, their order of rotation takes place in the same manner: :math:`ts^{\prime}r^{\prime\prime}` (see sec.~\ref{sec:samplePositioning}).

	Note that the angular deviations specified here always describe a **static** deviation of the initial coordinate system (at frame |nbsp| 0). They are not applied individually at each frame, which means that a stage tilt described here is meant to stay constant throughout the scan and does not describe a wobble. For dynamic deviations, the drift property of parameters can be used (sec.~\ref{sec:values_units_uncertainties_drifts}), as drifts are applied for each frame individually after the stage has reached its intended frame position.