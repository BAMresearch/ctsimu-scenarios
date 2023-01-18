.. _sec_geometry:

Geometry
========

.. _sec_geometry_placement_in_world:

Placement of objects in the world coordinate system
---------------------------------------------------

.. _fig_coordinates:
.. figure:: pictures/geometry.*
  :width: 80%

  World coordinate system {x, |nbsp| y, |nbsp| z} and local coordinate systems {u, |nbsp| v, |nbsp| w}.

This specification does not define a fixed coordinate system for the CT set-up. The only assumption is that a right-handed world coordinate system {x, |nbsp| y, |nbsp| z} is used, and the local coordinate systems {u, |nbsp| v, |nbsp| w} of source, detector and sample stage are to be placed in this world coordinate system. :numref:`fig_coordinates` illustrates the general placement that is used in the following examples.

The :json:`"geometry"` section has three subsections to define the location and orientation of the principal CT scanner components: :json:`"detector"`, :json:`"source"` and :json:`"stage"`. They all share a common set of JSON properties for positioning. A very similar description is used later on to place samples into the scene (see :ref:`sample positioning <sec_sample_positioning>`). The placement description generally consists of the following parts:

:json:`"center":`
  specifies the object's center (x, |nbsp| y, |nbsp| z) in the world coordinate system, i.e., the geometric center of its bounding box. The bounding box is defined as the smallest cuboid (or rectangle, for 2D objects) that completely encloses the object, under the condition that the cuboid's edges are each strictly parallel to one of the coordinate axes of the object's own Cartesian coordinate system. The :json:`"center"` is the origin of the local coordinate system {u, |nbsp| v, |nbsp| w} and also the pivot point for rotational deviations if no alternative pivot point is specified.

:json:`"vector_u":` and :json:`"vector_w":`
  specify the object's orientation by defining the basis vectors :math:`\vec{u}` and :math:`\vec{w}` of the local coordinate system in terms of the world coordinate system {x, |nbsp| y, |nbsp| z}. They are not required to be unit vectors but they must be **orthogonal.**

  :math:`\vec{w}` is usually meant to be a normal vector and :math:`\vec{u}` is one of the support vectors. :math:`\vec{u}` and :math:`\vec{v}` also serve a second meaning as row and column vector of the resulting projection (for the detector) or of a given spot intensity profile image (for the source). See the descriptions below for details.

Deviations
----------

Deviations are small shifts (translations) or rotations that specify how much an object's position or orientation differs from its ideal placement for the given frame. Deviations can be part of an object's geometry definition. For example, a wobbling rotation axis of the stage could be described as a tilt of its local coordinate system:

.. code-block:: json-object
  :linenos:
  :lineno-start: 42
  
  "deviations": [
    {
      "type": "translation",
      "axis": "x",
      "amount": {"value": 0.5, "unit": "mm"},
      "known_to_reconstruction": false
    },
    {
      "type": "rotation",
      "axis": "w",
      "amount": {"value": 2.3e-2, "unit": "rad"},
      "known_to_reconstruction": true
    }
  ]

:json:`"deviations":` an array that can be used to specify a sequence of small deviations from the ideal geometry, both rotational or translational. Examples would be tilts of the detector or the rotation axis, or small shifts that should or should not be considered during the reconstruction of the CT scan.

A simulation software should treat the array's deviation components as subsequent transformations of the frame's ideal local coordinate system.
  
A deviation component should provide the following properties:

* :json:`"type":` can be either :code:`"translation"` or :code:`"rotation"`.
* :json:`"amount":` the amount by which to deviate. For a translational deviation, this is the length by which the object should shift in the given direction. For a rotational deviation, it is the angle by which the object should rotate around the given axis (and optionally, the given pivot point). A :json:`"value"` and :json:`"unit"` must be specified for the amount.
* :json:`"axis":` specifies the direction of the deviation. For translations, it provides the direction of the shift. For rotations, it provides the rotation axis. The axis must not be a unit vector, but its length has no special significance.
  
  The axis can be given as and axis designation or as an arbitrary vector:
  
  * :code:`"x"`, :code:`"y"` or :code:`"z"` are the axes of the **world coordinate system.**
  
    .. code-block:: json-object
      :linenos:
      :lineno-start: 45
      
      "axis": "x"
  
  * :code:`"u"`, :code:`"v"` or :code:`"w"` are the axes of the **local coordinate system** or of the **stage coordinate system** (in case of samples).
  
    .. code-block:: json-object
      :linenos:
      :lineno-start: 51
      
      "axis": "w"
    
  * :code:`"r"`, :code:`"s"` or :code:`"t"` are the local axes of the **sample coordinate system** (see :ref:`samples <sec_samples>` for details).
  * An **arbitrary axis** can be specified using the vector components from any of the three aforementioned sets (world, local or sample). For example, a vector defined in the world coordinate system would look like:
  
  .. code-block:: json-object
    :linenos:
    :lineno-start: 57
    
    "axis": {
      "x": {"value":  2.0},
      "y": {"value": -3.0},
      "z": {"value":  5.3}
    }
  
  whereas a vector that is fixed to the local coordinate system would look like in the following listing. If this were defined for the stage, the vector would follow the stage's rotation throughout the CT scan.

* :json:`"pivot":` For rotations, the pivot point where the rotation axis is attached can be specified. If not specified, the object's center point is assumed to be the rotation's pivot point. Similar to the :json:`"axis"`, the pivot can be expressed in terms of the world coordinate system {x, y, z}, the local (or stage) coordinate system {u, v, w}, or the sample coordinate sytem {r, s, t}.

  .. code-block:: json-object
    :linenos:
    :lineno-start: 62
    
    "pivot": {
      "x": {"value":  2.0, "unit": "mm"},
      "y": {"value": -3.0, "unit": "mm"},
      "z": {"value":  5.3, "unit": "mm"}
    }

* :json:`"known_to_reconstruction":` Whether these deviations are known to the reconstruction software or not depends on the purpose of the scenario and can be specified by setting this property to either :json:`true` or :json:`false`:

  .. code-block:: json-object
    :linenos:
    :lineno-start: 53

    "known_to_reconstruction": true

Note that deviations are applied on a per-frame basis. They do not propagate to the next frame, they do not accumulate. For a given frame, all deviations are assumed to be applied **after the rotating sample stage has arrived** at its intended angular position. This means that if the deviation's :json:`"amount"` is drifting throughout the CT scan, the deviation is calculated anew for each frame, based on its current drift value, and assumed to be applied to the object's ideal position and orientation for the frame (without considering any previous deviations that have been applied in the frames before).

For example, a **static stage tilt** can be modelled by a rotation around on of the axes of the world coordinate system, or a vector that is given in terms of {x, y, z}:

.. code-block:: json-object

  "deviations": [
    {
      "comment": "static axis tilt around beam direction",
      "type": "rotation",
      "axis": "x",
      "amount": {"value": 4, "unit": "deg"},
      "known_to_reconstruction": false
    }
  ]

If a **dynamic stage tilt (wobble)** is modelled, it can be given as a rotation around one of its local axes, or any vector given in terms of the local coordinate system {u, v, w}. This way, the deviation's axis will rotate along with the CT stage. Since each deviation is applied on a per-frame basis from the frame's ideal geometry, the axis will precess around a cone.

.. code-block:: json-object
  :linenos:
  :lineno-start: 118
  
  "deviations": [
    {
      "comment": "axis wobble",
      "type": "rotation",
      "axis": {
        "u": {"value": 1},
        "v": {"value": 1},
        "w": {"value": 0}
      }
      "amount": {"value": 4, "unit": "deg"},
      "known_to_reconstruction": false
    }
  ]

.. _sec_geometry_detector:

Detector
--------

For this specification, in general, vectors :math:`\vec{u}` and :math:`\vec{v}` designate an item's in-plane vectors, whereas :math:`\vec{w}` usually designates a normal vector. Following this convention, :math:`\vec{u}_\textsf{D}` is the detector's **row vector,** pointing from left to right in the resulting projection image (as seen on a computer screen with a pixel coordinate system that has its origin in the upper left corner). :math:`\vec{v}_\textsf{D}` is the detector's **column vector,** pointing from top to bottom in the resulting projection image. The orientation of these two vectors directly determines the orientation of the projection image.

Note that for any object only the normal vector :math:`\vec{w}` and the support vector :math:`\vec{u}` are given in the JSON file. The detector normal :math:`\vec{w}_\textsf{D}` does not have any special meaning and should be arranged such that the detector's row and column vector point in the desired directions.

The size and further properties of the detector are defined later on in the :ref:`detector section <sec_detector>` of the JSON file.

.. code-block:: json-object
  :linenos:
  :lineno-start: 24

  "detector": {
    "center": {
      "x": {"value": 400, "unit": "mm"},
      "y": {"value":   0, "unit": "mm"},
      "z": {"value":   0, "unit": "mm"}
    },

    "vector_u": {
      "x": {"value":  0},
      "y": {"value": -1},
      "z": {"value":  0}
    },
    "vector_w": {
      "x": {"value":  1},
      "y": {"value":  0},
      "z": {"value":  0}
    },
    
    "deviations": [
      {
        "type": "translation",
        "axis": "x",
        "amount": {"value": 0.5, "unit": "mm"},
        "known_to_reconstruction": false
      },
      {
        "type": "rotation",
        "axis": "w",
        "amount": {"value": 2.3e-2, "unit": "rad"},
        "known_to_reconstruction": true
      },
      {
        "type": "rotation",
        "axis": {
          "x": {"value":  2.0},
          "y": {"value": -3.0},
          "z": {"value":  5.3}
        },
        "pivot": {
          "x": {"value":  2.0, "unit": "mm"},
          "y": {"value": -3.0, "unit": "mm"},
          "z": {"value":  5.3, "unit": "mm"}
        },
        "amount": {"value": 1.3, "unit": "deg"},
        "known_to_reconstruction": true
      }
    ]
  }


.. _sec_geometry_source:

Source
------

The source can be modelled either as a cone-beam geometry or a parallel beam geometry. This behaviour is set by the :json:`"type":` property, which can be either :json:`"cone"` or :json:`"parallel"`.

.. code-block:: json-object
  :linenos:
  :lineno-start: 74

  "type": "cone",
  "type": "parallel"

In the case of a parallel beam, its divergence can be specified along both planar axes of the source:

.. code-block:: json-object
  :linenos:
  :lineno-start: 75

  "beam_divergence": {
    "u": {"value": 0, "unit": "deg"},
    "v": {"value": 0, "unit": "deg"}
  }

For a cone beam geometry, this property should be set to :json:`null`:

.. code-block:: json-object
  :linenos:
  :lineno-start: 75

  "beam_divergence": null

Spatially extended source intensity profiles are modelled as a rectangle. For cone-beam geometries, this will be a very small rectangle on the size scale of the spot size.

For parallel beam geometries, the optical axis of the system is assumed to be the :math:`\vec{w}_\textsf{F}` axis of the source, and all rays should be parallel to this axis (apart from beam divergence). This means that the source rectangle in the model should ideally be of a size such that the entire detector is covered by radiation.

If a spot intensity profile is given as an image (see :ref:`source <sec_spot_2d_images>` for details), :math:`\vec{u}_\textsf{F}` is the image's row vector, pointing from left to right in this image, and :math:`\vec{v}_\textsf{F}` is the image's column vector, pointing from top to bottom.

To allow the correct orientation of the intensity profile image, the vector :math:`\vec{w}_\textsf{F}` does not necessarily point in the main direction of radiation, but could also point in the opposite direction (due to the restraint of a right-handed coordinate system).

Within the WIPANO CTSimU project, we agreed to the convention of placing the source at (0, |nbsp| 0, |nbsp| 0). It is not a requirement.

.. code-block:: json-object
  :linenos:
  :lineno-start: 73

  "source": {
    "type": "cone",
    "beam_divergence": {
      "u": {"value": 0, "unit": "deg"},
      "v": {"value": 0, "unit": "deg"}
    },

    "center": {
      "x": {"value": 0, "unit": "mm"},
      "y": {"value": 0, "unit": "mm"},
      "z": {"value": 0, "unit": "mm"}
    },

    "vector_u": {
      "x": {"value":  0},
      "y": {"value": -1},
      "z": {"value":  0}
    },
    "vector_w": {
      "x": {"value":  1},
      "y": {"value":  0},
      "z": {"value":  0}
    },
    
    "deviations": []
  }


.. _sec_geometry_stage:

Stage
-----

The normal vector :math:`\vec{w}_\textsf{O}` of the sample stage specifies the axis of rotation for the CT scan. By default, the sample stage coordinate system and all samples attached to it are meant to rotate around this axis, whereas the source and detector stay still (as for typical industrial CT scanners).

Samples that are placed in the stage coordinate system all take part in the rotation of the sample stage. Samples that are placed in the world coordinate system are fixed during the CT scan (i.e. fixed relative to source and detector, see :ref:`samples <sec_samples>` for details).

.. code-block:: json-object
  :linenos:
  :lineno-start: 100

  "stage": {
    "center": {
      "x": {"value": 275, "unit": "mm"},
      "y": {"value":   0, "unit": "mm"},
      "z": {"value":   0, "unit": "mm"}
    },

    "vector_u": {
      "x": {"value":  1},
      "y": {"value":  0},
      "z": {"value":  0}
    },
    "vector_w": {
      "x": {"value":  0},
      "y": {"value":  0},
      "z": {"value":  1}
    },
    
    "deviations": [
      {
        "comment": "axis wobble",
        "type": "rotation",
        "axis": "u",
        "amount": {"value": 4, "unit": "deg"},
        "known_to_reconstruction": false
      }
    ]
  }
