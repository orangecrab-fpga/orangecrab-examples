GPIO
====

Register Listing for GPIO
-------------------------

+--------------------------------+--------------------------------+
| Register                       | Address                        |
+================================+================================+
| :ref:`GPIO_OE <GPIO_OE>`       | :ref:`0x82005800 <GPIO_OE>`    |
+--------------------------------+--------------------------------+
| :ref:`GPIO_IN <GPIO_IN>`       | :ref:`0x82005804 <GPIO_IN>`    |
+--------------------------------+--------------------------------+
| :ref:`GPIO_OUT <GPIO_OUT>`     | :ref:`0x82005808 <GPIO_OUT>`   |
+--------------------------------+--------------------------------+
| :ref:`GPIO_ALT0 <GPIO_ALT0>`   | :ref:`0x8200580c <GPIO_ALT0>`  |
+--------------------------------+--------------------------------+
| :ref:`GPIO_ALT1 <GPIO_ALT1>`   | :ref:`0x82005810 <GPIO_ALT1>`  |
+--------------------------------+--------------------------------+
| :ref:`GPIO_ALT5 <GPIO_ALT5>`   | :ref:`0x82005814 <GPIO_ALT5>`  |
+--------------------------------+--------------------------------+
| :ref:`GPIO_ALT6 <GPIO_ALT6>`   | :ref:`0x82005818 <GPIO_ALT6>`  |
+--------------------------------+--------------------------------+
| :ref:`GPIO_ALT9 <GPIO_ALT9>`   | :ref:`0x8200581c <GPIO_ALT9>`  |
+--------------------------------+--------------------------------+
| :ref:`GPIO_ALT10 <GPIO_ALT10>` | :ref:`0x82005820 <GPIO_ALT10>` |
+--------------------------------+--------------------------------+
| :ref:`GPIO_ALT11 <GPIO_ALT11>` | :ref:`0x82005824 <GPIO_ALT11>` |
+--------------------------------+--------------------------------+
| :ref:`GPIO_ALT12 <GPIO_ALT12>` | :ref:`0x82005828 <GPIO_ALT12>` |
+--------------------------------+--------------------------------+
| :ref:`GPIO_ALT13 <GPIO_ALT13>` | :ref:`0x8200582c <GPIO_ALT13>` |
+--------------------------------+--------------------------------+
| :ref:`GPIO_ALT18 <GPIO_ALT18>` | :ref:`0x82005830 <GPIO_ALT18>` |
+--------------------------------+--------------------------------+
| :ref:`GPIO_ALT19 <GPIO_ALT19>` | :ref:`0x82005834 <GPIO_ALT19>` |
+--------------------------------+--------------------------------+
| :ref:`GPIO_ALT20 <GPIO_ALT20>` | :ref:`0x82005838 <GPIO_ALT20>` |
+--------------------------------+--------------------------------+
| :ref:`GPIO_ALT21 <GPIO_ALT21>` | :ref:`0x8200583c <GPIO_ALT21>` |
+--------------------------------+--------------------------------+

GPIO_OE
^^^^^^^

`Address: 0x82005800 + 0x0 = 0x82005800`

    GPIO Tristate(s) Control. Write ``1`` enable output driver

    .. wavedrom::
        :caption: GPIO_OE

        {
            "reg": [
                {"name": "io0",  "bits": 1},
                {"name": "io1",  "bits": 1},
                {"bits": 3},
                {"name": "io5",  "bits": 1},
                {"name": "io6",  "bits": 1},
                {"bits": 2},
                {"name": "io9",  "bits": 1},
                {"name": "io10",  "bits": 1},
                {"name": "io11",  "bits": 1},
                {"name": "io12",  "bits": 1},
                {"name": "io13",  "bits": 1},
                {"bits": 4},
                {"name": "io18",  "bits": 1},
                {"name": "io19",  "bits": 1},
                {"name": "io20",  "bits": 1},
                {"name": "io21",  "bits": 1},
                {"bits": 10}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


+-------+------+------------------------+
| Field | Name | Description            |
+=======+======+========================+
| [0]   | IO0  | Control for I/O pin 0  |
+-------+------+------------------------+
| [1]   | IO1  | Control for I/O pin 1  |
+-------+------+------------------------+
| [5]   | IO5  | Control for I/O pin 5  |
+-------+------+------------------------+
| [6]   | IO6  | Control for I/O pin 6  |
+-------+------+------------------------+
| [9]   | IO9  | Control for I/O pin 9  |
+-------+------+------------------------+
| [10]  | IO10 | Control for I/O pin 10 |
+-------+------+------------------------+
| [11]  | IO11 | Control for I/O pin 11 |
+-------+------+------------------------+
| [12]  | IO12 | Control for I/O pin 12 |
+-------+------+------------------------+
| [13]  | IO13 | Control for I/O pin 13 |
+-------+------+------------------------+
| [18]  | IO18 | Control for I/O pin 18 |
+-------+------+------------------------+
| [19]  | IO19 | Control for I/O pin 19 |
+-------+------+------------------------+
| [20]  | IO20 | Control for I/O pin 20 |
+-------+------+------------------------+
| [21]  | IO21 | Control for I/O pin 21 |
+-------+------+------------------------+

GPIO_IN
^^^^^^^

`Address: 0x82005800 + 0x4 = 0x82005804`

    GPIO Input(s) Status. Input value of IO pad as read by the FPGA

    .. wavedrom::
        :caption: GPIO_IN

        {
            "reg": [
                {"name": "io0",  "bits": 1},
                {"name": "io1",  "bits": 1},
                {"bits": 3},
                {"name": "io5",  "bits": 1},
                {"name": "io6",  "bits": 1},
                {"bits": 2},
                {"name": "io9",  "bits": 1},
                {"name": "io10",  "bits": 1},
                {"name": "io11",  "bits": 1},
                {"name": "io12",  "bits": 1},
                {"name": "io13",  "bits": 1},
                {"bits": 4},
                {"name": "io18",  "bits": 1},
                {"name": "io19",  "bits": 1},
                {"name": "io20",  "bits": 1},
                {"name": "io21",  "bits": 1},
                {"bits": 10}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


+-------+------+------------------------+
| Field | Name | Description            |
+=======+======+========================+
| [0]   | IO0  | Control for I/O pin 0  |
+-------+------+------------------------+
| [1]   | IO1  | Control for I/O pin 1  |
+-------+------+------------------------+
| [5]   | IO5  | Control for I/O pin 5  |
+-------+------+------------------------+
| [6]   | IO6  | Control for I/O pin 6  |
+-------+------+------------------------+
| [9]   | IO9  | Control for I/O pin 9  |
+-------+------+------------------------+
| [10]  | IO10 | Control for I/O pin 10 |
+-------+------+------------------------+
| [11]  | IO11 | Control for I/O pin 11 |
+-------+------+------------------------+
| [12]  | IO12 | Control for I/O pin 12 |
+-------+------+------------------------+
| [13]  | IO13 | Control for I/O pin 13 |
+-------+------+------------------------+
| [18]  | IO18 | Control for I/O pin 18 |
+-------+------+------------------------+
| [19]  | IO19 | Control for I/O pin 19 |
+-------+------+------------------------+
| [20]  | IO20 | Control for I/O pin 20 |
+-------+------+------------------------+
| [21]  | IO21 | Control for I/O pin 21 |
+-------+------+------------------------+

GPIO_OUT
^^^^^^^^

`Address: 0x82005800 + 0x8 = 0x82005808`

    GPIO Ouptut(s) Control. Value loaded into the output driver

    .. wavedrom::
        :caption: GPIO_OUT

        {
            "reg": [
                {"name": "io0",  "bits": 1},
                {"name": "io1",  "bits": 1},
                {"bits": 3},
                {"name": "io5",  "bits": 1},
                {"name": "io6",  "bits": 1},
                {"bits": 2},
                {"name": "io9",  "bits": 1},
                {"name": "io10",  "bits": 1},
                {"name": "io11",  "bits": 1},
                {"name": "io12",  "bits": 1},
                {"name": "io13",  "bits": 1},
                {"bits": 4},
                {"name": "io18",  "bits": 1},
                {"name": "io19",  "bits": 1},
                {"name": "io20",  "bits": 1},
                {"name": "io21",  "bits": 1},
                {"bits": 10}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


+-------+------+------------------------+
| Field | Name | Description            |
+=======+======+========================+
| [0]   | IO0  | Control for I/O pin 0  |
+-------+------+------------------------+
| [1]   | IO1  | Control for I/O pin 1  |
+-------+------+------------------------+
| [5]   | IO5  | Control for I/O pin 5  |
+-------+------+------------------------+
| [6]   | IO6  | Control for I/O pin 6  |
+-------+------+------------------------+
| [9]   | IO9  | Control for I/O pin 9  |
+-------+------+------------------------+
| [10]  | IO10 | Control for I/O pin 10 |
+-------+------+------------------------+
| [11]  | IO11 | Control for I/O pin 11 |
+-------+------+------------------------+
| [12]  | IO12 | Control for I/O pin 12 |
+-------+------+------------------------+
| [13]  | IO13 | Control for I/O pin 13 |
+-------+------+------------------------+
| [18]  | IO18 | Control for I/O pin 18 |
+-------+------+------------------------+
| [19]  | IO19 | Control for I/O pin 19 |
+-------+------+------------------------+
| [20]  | IO20 | Control for I/O pin 20 |
+-------+------+------------------------+
| [21]  | IO21 | Control for I/O pin 21 |
+-------+------+------------------------+

GPIO_ALT0
^^^^^^^^^

`Address: 0x82005800 + 0xc = 0x8200580c`

    GPIO Alt Control. IO pin alternative functions

    .. wavedrom::
        :caption: GPIO_ALT0

        {
            "reg": [
                {"name": "ctrl",  "bits": 8},
                {"bits": 24}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


+-------+------+---------------------------------------+
| Field | Name | Description                           |
+=======+======+=======================================+
| [7:0] | CTRL | Select alternative function on IO pin |
|       |      |                                       |
|       |      | +-------+-------------+               |
|       |      | | Value | Description |               |
|       |      | +=======+=============+               |
|       |      | | 0     | csr_control |               |
|       |      | +-------+-------------+               |
+-------+------+---------------------------------------+

GPIO_ALT1
^^^^^^^^^

`Address: 0x82005800 + 0x10 = 0x82005810`

    GPIO Alt Control. IO pin alternative functions

    .. wavedrom::
        :caption: GPIO_ALT1

        {
            "reg": [
                {"name": "ctrl",  "bits": 8},
                {"bits": 24}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


+-------+------+---------------------------------------+
| Field | Name | Description                           |
+=======+======+=======================================+
| [7:0] | CTRL | Select alternative function on IO pin |
|       |      |                                       |
|       |      | +-------+-------------+               |
|       |      | | Value | Description |               |
|       |      | +=======+=============+               |
|       |      | | 0     | csr_control |               |
|       |      | +-------+-------------+               |
+-------+------+---------------------------------------+

GPIO_ALT5
^^^^^^^^^

`Address: 0x82005800 + 0x14 = 0x82005814`

    GPIO Alt Control. IO pin alternative functions

    .. wavedrom::
        :caption: GPIO_ALT5

        {
            "reg": [
                {"name": "ctrl",  "bits": 8},
                {"bits": 24}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


+-------+------+---------------------------------------+
| Field | Name | Description                           |
+=======+======+=======================================+
| [7:0] | CTRL | Select alternative function on IO pin |
|       |      |                                       |
|       |      | +-------+-------------+               |
|       |      | | Value | Description |               |
|       |      | +=======+=============+               |
|       |      | | 0     | csr_control |               |
|       |      | +-------+-------------+               |
+-------+------+---------------------------------------+

GPIO_ALT6
^^^^^^^^^

`Address: 0x82005800 + 0x18 = 0x82005818`

    GPIO Alt Control. IO pin alternative functions

    .. wavedrom::
        :caption: GPIO_ALT6

        {
            "reg": [
                {"name": "ctrl",  "bits": 8},
                {"bits": 24}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


+-------+------+---------------------------------------+
| Field | Name | Description                           |
+=======+======+=======================================+
| [7:0] | CTRL | Select alternative function on IO pin |
|       |      |                                       |
|       |      | +-------+-------------+               |
|       |      | | Value | Description |               |
|       |      | +=======+=============+               |
|       |      | | 0     | csr_control |               |
|       |      | +-------+-------------+               |
+-------+------+---------------------------------------+

GPIO_ALT9
^^^^^^^^^

`Address: 0x82005800 + 0x1c = 0x8200581c`

    GPIO Alt Control. IO pin alternative functions

    .. wavedrom::
        :caption: GPIO_ALT9

        {
            "reg": [
                {"name": "ctrl",  "bits": 8},
                {"bits": 24}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


+-------+------+---------------------------------------+
| Field | Name | Description                           |
+=======+======+=======================================+
| [7:0] | CTRL | Select alternative function on IO pin |
|       |      |                                       |
|       |      | +-------+-------------+               |
|       |      | | Value | Description |               |
|       |      | +=======+=============+               |
|       |      | | 0     | csr_control |               |
|       |      | +-------+-------------+               |
+-------+------+---------------------------------------+

GPIO_ALT10
^^^^^^^^^^

`Address: 0x82005800 + 0x20 = 0x82005820`

    GPIO Alt Control. IO pin alternative functions

    .. wavedrom::
        :caption: GPIO_ALT10

        {
            "reg": [
                {"name": "ctrl",  "bits": 8},
                {"bits": 24}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


+-------+------+---------------------------------------+
| Field | Name | Description                           |
+=======+======+=======================================+
| [7:0] | CTRL | Select alternative function on IO pin |
|       |      |                                       |
|       |      | +-------+-------------+               |
|       |      | | Value | Description |               |
|       |      | +=======+=============+               |
|       |      | | 0     | csr_control |               |
|       |      | +-------+-------------+               |
+-------+------+---------------------------------------+

GPIO_ALT11
^^^^^^^^^^

`Address: 0x82005800 + 0x24 = 0x82005824`

    GPIO Alt Control. IO pin alternative functions

    .. wavedrom::
        :caption: GPIO_ALT11

        {
            "reg": [
                {"name": "ctrl",  "bits": 8},
                {"bits": 24}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


+-------+------+---------------------------------------+
| Field | Name | Description                           |
+=======+======+=======================================+
| [7:0] | CTRL | Select alternative function on IO pin |
|       |      |                                       |
|       |      | +-------+-------------+               |
|       |      | | Value | Description |               |
|       |      | +=======+=============+               |
|       |      | | 0     | csr_control |               |
|       |      | +-------+-------------+               |
+-------+------+---------------------------------------+

GPIO_ALT12
^^^^^^^^^^

`Address: 0x82005800 + 0x28 = 0x82005828`

    GPIO Alt Control. IO pin alternative functions

    .. wavedrom::
        :caption: GPIO_ALT12

        {
            "reg": [
                {"name": "ctrl",  "bits": 8},
                {"bits": 24}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


+-------+------+---------------------------------------+
| Field | Name | Description                           |
+=======+======+=======================================+
| [7:0] | CTRL | Select alternative function on IO pin |
|       |      |                                       |
|       |      | +-------+-------------+               |
|       |      | | Value | Description |               |
|       |      | +=======+=============+               |
|       |      | | 0     | csr_control |               |
|       |      | +-------+-------------+               |
+-------+------+---------------------------------------+

GPIO_ALT13
^^^^^^^^^^

`Address: 0x82005800 + 0x2c = 0x8200582c`

    GPIO Alt Control. IO pin alternative functions

    .. wavedrom::
        :caption: GPIO_ALT13

        {
            "reg": [
                {"name": "ctrl",  "bits": 8},
                {"bits": 24}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


+-------+------+---------------------------------------+
| Field | Name | Description                           |
+=======+======+=======================================+
| [7:0] | CTRL | Select alternative function on IO pin |
|       |      |                                       |
|       |      | +-------+-------------+               |
|       |      | | Value | Description |               |
|       |      | +=======+=============+               |
|       |      | | 0     | csr_control |               |
|       |      | +-------+-------------+               |
+-------+------+---------------------------------------+

GPIO_ALT18
^^^^^^^^^^

`Address: 0x82005800 + 0x30 = 0x82005830`

    GPIO Alt Control. IO pin alternative functions

    .. wavedrom::
        :caption: GPIO_ALT18

        {
            "reg": [
                {"name": "ctrl",  "bits": 8},
                {"bits": 24}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


+-------+------+---------------------------------------+
| Field | Name | Description                           |
+=======+======+=======================================+
| [7:0] | CTRL | Select alternative function on IO pin |
|       |      |                                       |
|       |      | +-------+-------------+               |
|       |      | | Value | Description |               |
|       |      | +=======+=============+               |
|       |      | | 0     | csr_control |               |
|       |      | +-------+-------------+               |
+-------+------+---------------------------------------+

GPIO_ALT19
^^^^^^^^^^

`Address: 0x82005800 + 0x34 = 0x82005834`

    GPIO Alt Control. IO pin alternative functions

    .. wavedrom::
        :caption: GPIO_ALT19

        {
            "reg": [
                {"name": "ctrl",  "bits": 8},
                {"bits": 24}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


+-------+------+---------------------------------------+
| Field | Name | Description                           |
+=======+======+=======================================+
| [7:0] | CTRL | Select alternative function on IO pin |
|       |      |                                       |
|       |      | +-------+-------------+               |
|       |      | | Value | Description |               |
|       |      | +=======+=============+               |
|       |      | | 0     | csr_control |               |
|       |      | +-------+-------------+               |
+-------+------+---------------------------------------+

GPIO_ALT20
^^^^^^^^^^

`Address: 0x82005800 + 0x38 = 0x82005838`

    GPIO Alt Control. IO pin alternative functions

    .. wavedrom::
        :caption: GPIO_ALT20

        {
            "reg": [
                {"name": "ctrl",  "bits": 8},
                {"bits": 24}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


+-------+------+---------------------------------------+
| Field | Name | Description                           |
+=======+======+=======================================+
| [7:0] | CTRL | Select alternative function on IO pin |
|       |      |                                       |
|       |      | +-------+-------------+               |
|       |      | | Value | Description |               |
|       |      | +=======+=============+               |
|       |      | | 0     | csr_control |               |
|       |      | +-------+-------------+               |
+-------+------+---------------------------------------+

GPIO_ALT21
^^^^^^^^^^

`Address: 0x82005800 + 0x3c = 0x8200583c`

    GPIO Alt Control. IO pin alternative functions

    .. wavedrom::
        :caption: GPIO_ALT21

        {
            "reg": [
                {"name": "ctrl",  "bits": 8},
                {"bits": 24}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


+-------+------+---------------------------------------+
| Field | Name | Description                           |
+=======+======+=======================================+
| [7:0] | CTRL | Select alternative function on IO pin |
|       |      |                                       |
|       |      | +-------+-------------+               |
|       |      | | Value | Description |               |
|       |      | +=======+=============+               |
|       |      | | 0     | csr_control |               |
|       |      | +-------+-------------+               |
+-------+------+---------------------------------------+

