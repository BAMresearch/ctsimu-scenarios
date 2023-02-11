.. _parameters:

Parameter List
==============

:numref:`tab_parameters` gives an overview of all parameters in this file format specification. It lists the expected type and if the parameter supports drifts.

.. _tab_parameters:

.. table:: Parameter overview and support for drifts.

  ============================================================= ============= ============================
  Parameter                                                     Type          Drifts
  ============================================================= ============= ============================
  **File**
  :code:`file name`                                             string        no
  :code:`file description`                                      string        no
  :code:`file contact`                                          string        no
  :code:`file date_created`                                     string        no
  :code:`file date_changed`                                     string        no
  :code:`file version major`                                    integer       no
  :code:`file version minor`                                    integer       no
  :code:`file file_type`                                        string        no
  :code:`file file_format_version major`                        integer       no
  :code:`file file_format_version minor`                        integer       no
  **Environment**
  :code:`environment material_id`                               string        no
  :code:`environment temperature`                               float         yes
  **Geometry**
  :code:`geometry detector center x/y/z`                        float         yes
  :code:`geometry detector vector_u x/y/z`                      float         yes
  :code:`geometry detector vector_w x/y/z`                      float         yes
  :code:`geometry detector deviations`                          array         see :numref:`tab_deviations`
  :code:`geometry source type`                                  string        no
  :code:`geometry source beam_divergence u/v`                   float         yes
  :code:`geometry source center x/y/z`                          float         yes
  :code:`geometry source vector_u x/y/z`                        float         yes
  :code:`geometry source vector_w x/y/z`                        float         yes
  :code:`geometry source deviations`                            array         see :numref:`tab_deviations`
  :code:`geometry stage center x/y/z`                           float         yes
  :code:`geometry stage vector_u x/y/z`                         float         yes
  :code:`geometry stage vector_w x/y/z`                         float         yes
  :code:`geometry stage deviations`                             array         see :numref:`tab_deviations`
  **Detector**
  :code:`detector model`                                        string        no
  :code:`detector manufacturer`                                 string        no
  :code:`detector type`                                         string        no
  :code:`detector columns`                                      integer       yes
  :code:`detector rows`                                         integer       yes
  :code:`detector pixel_pitch u/v`                              float         yes
  :code:`detector bit_depth`                                    integer       no
  :code:`detector integration_time`                             float         yes
  :code:`detector dead_time`                                    float         yes
  :code:`detector image_lag`                                    float         yes
  :code:`detector gray_value imax`                              float         yes
  :code:`detector gray_value imin`                              float         yes
  :code:`detector gray_value factor`                            float         yes
  :code:`detector gray_value offset`                            float         yes
  :code:`detector gray_value intensity_characteristics_file`    string        yes
  :code:`detector gray_value efficiency_characteristics_file`   string        yes
  :code:`detector noise snr_at_imax`                            float         yes
  :code:`detector noise noise_characteristics_file`             string        yes
  :code:`detector gain`                                         anything      no
  :code:`detector unsharpness basic_spatial_resolution`         float         yes
  :code:`detector unsharpness mtf`                              string        yes
  :code:`detector bad_pixel_map file`                           string        yes
  :code:`detector bad_pixel_map type`                           string        no
  :code:`detector bad_pixel_map endian`                         string        no
  :code:`detector bad_pixel_map headersize`                     integer       no
  :code:`detector scintillator material_id`                     string        no
  :code:`detector scintillator thickness`                       float         yes
  :code:`detector window front`                                 array         --
  :code:`detector window front material_id`                     string        no
  :code:`detector window front thickness`                       float         yes
  :code:`detector window rear`                                  array         --
  :code:`detector window rear material_id`                      string        no
  :code:`detector window rear thickness`                        float         yes
  :code:`detector filters front`                                array         --
  :code:`detector filters front material_id`                    string        no
  :code:`detector filters front thickness`                      float         yes
  :code:`detector filters rear`                                 array         --
  :code:`detector filters rear material_id`                     string        no
  :code:`detector filters rear thickness`                       float         yes
  **Source**
  :code:`source model`                                          string        no
  :code:`source manufacturer`                                   string        no
  :code:`source voltage`                                        float         yes
  :code:`source current`                                        float         yes
  :code:`source target material_id`                             string        no
  :code:`source target type`                                    string        no
  :code:`source target thickness`                               float         yes
  :code:`source target angle incidence`                         float         yes
  :code:`source target angle emission`                          float         yes
  :code:`source spot size u/v/w`                                float         yes
  :code:`source spot sigma u/v/w`                               float         yes
  :code:`source spot intensity_map file`                        string        yes
  :code:`source spot intensity_map type`                        string        no
  :code:`source spot intensity_map dim_x/y/z`                   integer       no
  :code:`source spot intensity_map endian`                      string        no
  :code:`source spot intensity_map headersize`                  integer       no
  :code:`source spectrum monochromatic`                         boolean       no
  :code:`source spectrum file`                                  string        yes
  :code:`source spectrum window`                                array         --
  :code:`source spectrum window material_id`                    string        no
  :code:`source spectrum window thickness`                      float         yes
  :code:`source spectrum filters`                               array         --
  :code:`source spectrum filters material_id`                   string        no
  :code:`source spectrum filters thickness`                     float         yes
  **Samples**
  :code:`samples`                                               array         --
  :code:`samples name`                                          string        no
  :code:`samples file`                                          string        yes
  :code:`samples unit`                                          string        no
  :code:`samples scaling_factor r/s/t`                          float         yes
  :code:`samples material_id`                                   string        no
  :code:`samples position center u/v/w/x/y/z`                   float         yes
  :code:`samples position vector_r u/v/w/x/y/z`                 float         yes
  :code:`samples position vector_t u/v/w/x/y/z`                 float         yes
  :code:`samples position deviations`                           array         see :numref:`tab_deviations`
  **Acquisition**
  :code:`acquisition start_angle`                               float         no
  :code:`acquisition stop_angle`                                float         no
  :code:`acquisition direction`                                 string        no
  :code:`acquisition scan_mode`                                 string        no
  :code:`acquisition scan_speed`                                float         yes
  :code:`acquisition number_of_projections`                     integer       no
  :code:`acquisition include_final_angle`                       boolean       no
  :code:`acquisition frame_average`                             integer       no
  :code:`acquisition dark_field number`                         integer       no
  :code:`acquisition dark_field frame_average`                  integer       no
  :code:`acquisition dark_field ideal`                          boolean       no
  :code:`acquisition dark_field correction`                     boolean       no
  :code:`acquisition flat_field number`                         integer       no
  :code:`acquisition flat_field frame_average`                  integer       no
  :code:`acquisition flat_field ideal`                          boolean       no
  :code:`acquisition flat_field correction`                     boolean       no
  :code:`acquisition pixel_binning u/v`                         integer       no
  :code:`acquisition pixel_binning u/v`                         integer       no
  :code:`acquisition scattering`                                boolean       no
  **Materials**
  :code:`materials`                                             array         --
  :code:`materials id`                                          string        no
  :code:`materials name`                                        string        no
  :code:`materials density`                                     float         yes
  :code:`materials composition formula`                         string        yes
  :code:`materials composition mass_fraction`                   float         yes
  ============================================================= ============= ============================

Objects in the scene may come with :ref:`geometrical deviations <sec_geometry_deviations>`. These are defined as an array of deviation objects. The structure of deviation objects is listed in :numref:`tab_deviations`.


.. _tab_deviations:

.. table:: Deviation objects. The :json:`"axis"` my be defined as a string or object.

  ================================ ============= ==========
  Parameter                        Type          Drifts
  ================================ ============= ==========
  :code:`type`                     string        no
  :code:`axis`                     string        no
  :code:`axis`                     object        --
  :code:`axis x/y/z`               float         yes
  :code:`axis u/v/w`               float         yes
  :code:`axis r/s/t`               float         yes
  :code:`pivot x/y/z`              float         yes
  :code:`pivot u/v/w`              float         yes
  :code:`pivot r/s/t`              float         yes
  :code:`amount`                   float         yes
  :code:`known_to_reconstruction`  boolean       no
  ================================ ============= ==========