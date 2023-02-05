.. _sec_acquisition:

Acquisition
===========

Sample stage rotation
---------------------

The stage is assumed to perform a rotation around its :math:`\vec{w}_\textsf{O}` axis during the scan, resulting in a circular sample trajectory. Other trajectories can be modelled using :ref:`drifts <sec_drifts>`, especially drifts of the stage geometry parameters. For example, a helix scan can be modelled by starting with a standard circular trajectory of several rotations (as described in the following), and an additional drift of the stage center's :math:`z` position. If the scan trajectory is completely described by drifts, the stage rotation described here should be deactivated by setting both :json:`"start_angle"` and :json:`"stop_angle"` to :json:`0`.

For a circular CT scan, the start and stop angle of the sample stage are defined in this section. An angle of :json:`0` refers to the orientation of the stage as defined in the :ref:`geometry section <sec_geometry>` (for frame |nbsp| 0). All other angles express a rotation around the :math:`\vec{w}_\textsf{O}` axis of the stage. The direction of rotation must be mathematically positive in the case of counter-clockwise acquisition direction (:json:`"CCW"`), and mathematically negative in the case of clockwise acquisition direction (:json:`"CW"`). The stage reaches the start and stop angle by rotating in the given :json:`"direction"` around its normal axis (:numref:`fig_rotation`). This means that the :json:`"direction"` parameter affects both the positions of start and stop angle, as well as the direction of rotation in which the CT scan is performed. It also means that **the start angle must always be less than (or equal to) the stop angle.** However, negative angular positions and positions greater than 360° are allowed, as well as an angular coverage of more than a full circle, e.g. to perform multiple rotations during one scan.

.. code-block:: json-object
  :linenos:
  :lineno-start: 320

  "start_angle": {"value":   0, "unit": "deg"},
  "stop_angle":  {"value": 320, "unit": "deg"}

.. _fig_rotation:
.. figure:: pictures/rotation.*
  :width: 80%

  The given start angle and stop angle refer to opposite angular positions in **(a)** |nbsp| counter-clockwise or **(b)** |nbsp| clockwise direction (as seen from "above" the stage). They describe the angular range covered by the CT scan.

The direction of the sample stage rotation can be counter-clockwise (:json:`"CCW"`, mathematically positive) or clockwise (:json:`"CW"`, mathematically negative) around the :math:`\vec{w}_\textsf{O}` axis:

.. code-block:: json-object
  :linenos:
  :lineno-start: 322

  "direction": "CW",
  "direction": "CCW"

The parameter :json:`"scan_mode"` defines if the rotation stops while a projection is taken, or if it runs continuously.

.. code-block:: json-object
  :linenos:
  :lineno-start: 323

  "scan_mode": "stop+go",
  "scan_mode": "continuous"

The property for scan speed should only be used for continuous-motion scans. If undefined, it may be calculated from the detector's integration and dead time.

.. code-block:: json-object
  :linenos:
  :lineno-start: 324

  "scan_speed": {"value": 360, "unit": "deg/h"}

For stop&go scans, it should be set to :json:`null`:

.. code-block:: json-object
  :linenos:
  :lineno-start: 324

  "scan_speed": null

Frames and projections
----------------------

.. _sec_num_of_projections:

Number of projections
~~~~~~~~~~~~~~~~~~~~~

The :json:`"number_of_projections"` is also given in the acquisition section.

.. code-block:: json-object
  :linenos:
  :lineno-start: 325

  "number_of_projections": 2001

Beginning from the start angle, the necessary number of angular steps is performed (in the case of a stop&go scan). It is assumed that a frame is taken before each step (starting with the first frame at the start angle). The parameter :json:`"include_final_angle"` can be set to :json:`true` if the last projection should be taken after the stop angle has been reached, or to :json:`false` if it is meant to be taken at the last step before the stop angle is reached.

.. code-block:: json-object
  :linenos:
  :lineno-start: 326

  "include_final_angle": true

.. _sec_frame_avg:

Frame averaging
~~~~~~~~~~~~~~~

The number of frames to be averaged for one projection image can be specified:

.. code-block:: json-object
  :linenos:
  :lineno-start: 327

  "frame_average": 3

.. _sec_flat_dark_field:

Dark field and flat field acquisition and correction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If dark field and flat field images are acquired along with the projections, their numbers and frame averages can be specified. An :json:`"ideal"` image means that the simulation of noise is to be omitted by the simulation software, possibly in contrast to the :ref:`noise <sec_noise>` specification in the detector section. The parameter :json:`"correction"` tells whether the projection images already come in a corrected form as a result of the scan (:json:`true`) or if they are taken as uncorrected files (:json:`false`).

.. code-block:: json-object
  :linenos:
  :lineno-start: 328

  "dark_field": {
    "number": 1,
    "frame_average": 1,
    "ideal": true,
    "correction": false
  },
  "flat_field": {
    "number": 3,
    "frame_average": 20,
    "ideal": false,
    "correction": false
  }

.. _sec_pixel_binning:

Pixel binning
~~~~~~~~~~~~~

The number of pixels to bin in directions :math:`\vec{u}` and :math:`\vec{v}` of the detector:

.. code-block:: json-object
  :linenos:
  :lineno-start: 340

  "pixel_binning": {"u": 1, "v": 1}

The binning operation is not described here and left to the software.

Scattering
----------

This parameter specifies if X-ray scattering should be simulated or not.

.. code-block:: json-object
  :linenos:
  :lineno-start: 341

  "scattering": false