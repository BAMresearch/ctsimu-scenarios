.. _sec_samples:

Samples
=======

.. _sec_samples_general:

General properties
------------------

Any number of samples can be defined in the :json:`"samples"` array and placed in the scene, either :ref:`attached to the rotating sample stage <sec_sample_in_stage_coordinates>`, or :ref:`fixed to the world coordinate system <sec_sample_in_world_coordinates>`. A sample object has the following properties.

The sample name:

.. code-block:: json-object
  :linenos:
  :lineno-start: 265

  "name": "Tetrahedron"

A reference to the model file (e.g. STL or CAD file) that describes the sample geometry:

.. code-block:: json-object
  :linenos:
  :lineno-start: 266

  "file": {"value": "tetra.stl", "drifts": null}

The unit of length that is used in the model file:

.. code-block:: json-object
  :linenos:
  :lineno-start: 267

  "unit": "mm"

A scaling factor for each axis of the sample coordinate system, if the model should be resized by a constant factor:

.. code-block:: json-object
  :linenos:
  :lineno-start: 268

  "scaling_factor": {
    "r": {"value": 0.75, "drifts": null},
    "s": {"value": 0.75, "drifts": null},
    "t": {"value": 0.75, "drifts": null}
  }

The material of the sample, given by a :json:`"material_id"` that references a material definition in the :ref:`materials section <sec_materials>` of the file:

.. code-block:: json-object
  :linenos:
  :lineno-start: 273

  "material_id": "Glass Ceramic"

.. _sec_sample_positioning:

Sample positioning
------------------

.. _sec_sample_in_stage_coordinates:

Sample attached to the stage coordinate system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The sample coordinate system {r, |nbsp| s, |nbsp| t} is equivalent to the surface model's proper {x, |nbsp| y, |nbsp| z} coordinate system (except for the location of the origin). It is specific to each sample and can be placed in the stage coordinate system by providing its center coordinates in terms of {u, |nbsp| v, |nbsp| w}\ :sub:`O` (see :numref:`fig_sampleCoordinates` for an illustration). If done so, the sample is attached to the stage and will follow any rotations and translations performed by the stage during the CT scan.

.. _fig_sampleCoordinates:
.. figure:: pictures/sample.*
  :width: 60%

  World coordinate system {x, |nbsp| y, |nbsp| z}, stage coordinate system {u, |nbsp| v, |nbsp| w}\ :sub:`O` and sample coordinate system {r, |nbsp| s, |nbsp| t}.

The description follows the convention that has been established for the :ref:`placement of objects in the world coordinate system <sec_geometry_placement_in_world>`, with the following sub-elements of the sample's :json:`"position"` property.

.. code-block:: json-object
  :linenos:
  :lineno-start: 274

  "position": {
    "center": {
      "u": {"value":  0, "unit": "mm"},
      "v": {"value": 20, "unit": "mm"},
      "w": {"value":  0, "unit": "mm"}
    },

    "vector_r": {
      "u": {"value":  1},
      "v": {"value":  0},
      "w": {"value":  0}
    },
    "vector_t": {
      "u": {"value":  0},
      "v": {"value": -0.2},
      "w": {"value":  1}
    },

    "deviations": []
  }

The **center** is given in terms of the stage coordinate system {u, |nbsp| v, |nbsp| w}\ :sub:`O`.

To define the sample's **orientation,** its :math:`\vec{r}` and :math:`\vec{t}` vector must also be expressed in terms of the stage coordinate system {u, |nbsp| v, |nbsp| w}\ :sub:`O`\ :

In analogy to the **deviations** of the principal elements of the scene (see :ref:`deviations <sec_geometry_deviations>` in the geometry section), the sample's deviations can also take place along axes of the **sample coordinate system** {r, s, t}.

.. _sec_sample_in_world_coordinates:

Fixed sample position in the world coordinate system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the sample is placed in the fixed world coordinate system, it will not follow any motions performed by the sample stage. Instead, it will stay fixed in {x, y, z} if no custom drifts are specified.

The description is very similar to placing a sample in the stage coordinate system, as described in the :ref:`previous section <sec_sample_in_stage_coordinates>`. The only difference is that the object's center and basis vectors :math:`\vec{r}` and :math:`\vec{t}` are now expressed in terms of the world coordinate system {x, |nbsp| y, |nbsp| z}, just like it is done for the source and detector. The following listing gives an example of an aluminium frame around the sample stage that is fixed to the world coordinate system.

.. code-block:: json-object
  :linenos:
  :lineno-start: 295

  {
    "name": "Attachment Frame",
    "file": {"value": "frame.stl", "drifts": null},
    "unit": "mm",
    "scaling_factor": {
      "r": {"value": 1.0, "drifts": null},
      "s": {"value": 1.0, "drifts": null},
      "t": {"value": 1.0, "drifts": null}
    },
    "material_id": "Al",
    "position": {
      "center": {
        "x": {"value": 275, "unit": "mm"},
        "y": {"value":   0, "unit": "mm"},
        "z": {"value":   0, "unit": "mm"}
      },

      "vector_r": {
        "x": {"value":  1},
        "y": {"value":  0},
        "z": {"value":  0}
      },
      "vector_t": {
        "x": {"value":  0},
        "y": {"value":  1},
        "z": {"value":  0}
      },

      "deviations": []
    }
  }
