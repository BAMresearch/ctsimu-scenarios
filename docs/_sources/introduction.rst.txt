.. _sec_introduction:

Introduction
============

The WIPANO CTSimU project aims to define a qualification framework for radiographic simulation software. Such software is intended to be used for determining measurement uncertainties for geometrical properties of scanned samples, which arise from the overall procedure of a computed tomography (CT) scan.

On the following pages, a JSON structure (JavaScript Object Notation) is introduced. Its purpose is to contain all relevant parameters of an industrial CT scan, with the intention to

1. document the parameters of any real CT set-up with their respective uncertainties, and
2. completely describe CT scenarios for simulations within the project.

The JSON format was chosen because it is both *human-readable* and *human-writeable*, as well as *machine-readable*, which enables reproducible simulations based on the scenario description files.

A listing of a :ref:`full example <FullExample>` can be found at the end of this document. Additional example scenarios, along with simulated projection images, can be found on the Github repository of the file format specification, in the :code:`examples` folder:

`https://github.com/BAMresearch/ctsimu-scenarios <https://github.com/BAMresearch/ctsimu-scenarios>`__

The line numbers in the code snippets in the following description refer to the line numbers of the full example. It describes a step cylinder made of a glass ceramic, placed 20 |nbsp| mm to the "left" of the rotation axis at a slight angle. The rotation stage is symmetrically surrounded by a fixed aluminium frame that does not follow the rotation of the stage (:numref:`exampleCTsetup`). The detector is tilted around its planar normal by 0.023 |nbsp| rad in clockwise direction (as seen from the source). The stage's rotation axis is tilted and performs a wobble motion at an angle of 4°.

.. _exampleCTsetup:
.. figure:: pictures/example.png
    :width: 100%

    **Left:** CT setup that is described by the example code snippets in the following sections. **Right:** Resulting projection on the detector.