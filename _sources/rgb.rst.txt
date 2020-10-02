RGB
===

Register Listing for RGB
------------------------

+--------------------------------+--------------------------------+
| Register                       | Address                        |
+================================+================================+
| :ref:`RGB_R <RGB_R>`           | :ref:`0x82005000 <RGB_R>`      |
+--------------------------------+--------------------------------+
| :ref:`RGB_G <RGB_G>`           | :ref:`0x82005004 <RGB_G>`      |
+--------------------------------+--------------------------------+
| :ref:`RGB_B <RGB_B>`           | :ref:`0x82005008 <RGB_B>`      |
+--------------------------------+--------------------------------+
| :ref:`RGB_DIV_M <RGB_DIV_M>`   | :ref:`0x8200500c <RGB_DIV_M>`  |
+--------------------------------+--------------------------------+
| :ref:`RGB_CONFIG <RGB_CONFIG>` | :ref:`0x82005010 <RGB_CONFIG>` |
+--------------------------------+--------------------------------+

RGB_R
^^^^^

`Address: 0x82005000 + 0x0 = 0x82005000`


    .. wavedrom::
        :caption: RGB_R

        {
            "reg": [
                {"name": "r[7:0]", "attr": 'reset: 255', "bits": 8},
                {"bits": 24},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


RGB_G
^^^^^

`Address: 0x82005000 + 0x4 = 0x82005004`


    .. wavedrom::
        :caption: RGB_G

        {
            "reg": [
                {"name": "g[7:0]", "bits": 8},
                {"bits": 24},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


RGB_B
^^^^^

`Address: 0x82005000 + 0x8 = 0x82005008`


    .. wavedrom::
        :caption: RGB_B

        {
            "reg": [
                {"name": "b[7:0]", "bits": 8},
                {"bits": 24},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


RGB_DIV_M
^^^^^^^^^

`Address: 0x82005000 + 0xc = 0x8200500c`


    .. wavedrom::
        :caption: RGB_DIV_M

        {
            "reg": [
                {"name": "div_m[31:0]", "bits": 32}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


RGB_CONFIG
^^^^^^^^^^

`Address: 0x82005000 + 0x10 = 0x82005010`


    .. wavedrom::
        :caption: RGB_CONFIG

        {
            "reg": [
                {"name": "breath",  "bits": 1},
                {"name": "rainbow",  "bits": 1},
                {"bits": 30}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


+-------+---------+--------------------------------------+
| Field | Name    | Description                          |
+=======+=========+======================================+
| [0]   | BREATH  | Modulate output with a breath effect |
+-------+---------+--------------------------------------+
| [1]   | RAINBOW | Modulate output with rainbow         |
+-------+---------+--------------------------------------+

