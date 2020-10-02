LXSPI
=====

Register Listing for LXSPI
--------------------------

+--------------------------------------------+--------------------------------------+
| Register                                   | Address                              |
+============================================+======================================+
| :ref:`LXSPI_BITBANG <LXSPI_BITBANG>`       | :ref:`0x82007800 <LXSPI_BITBANG>`    |
+--------------------------------------------+--------------------------------------+
| :ref:`LXSPI_MISO <LXSPI_MISO>`             | :ref:`0x82007804 <LXSPI_MISO>`       |
+--------------------------------------------+--------------------------------------+
| :ref:`LXSPI_BITBANG_EN <LXSPI_BITBANG_EN>` | :ref:`0x82007808 <LXSPI_BITBANG_EN>` |
+--------------------------------------------+--------------------------------------+

LXSPI_BITBANG
^^^^^^^^^^^^^

`Address: 0x82007800 + 0x0 = 0x82007800`

    Bitbang controls for SPI output.  Only standard 1x SPI is supported, and as a
    result all four wires are ganged together.  This means that it is only possible
    to perform half-duplex operations, using this SPI core.

    .. wavedrom::
        :caption: LXSPI_BITBANG

        {
            "reg": [
                {"name": "mosi",  "bits": 1},
                {"name": "clk",  "bits": 1},
                {"name": "cs_n",  "bits": 1},
                {"name": "dir",  "bits": 1},
                {"bits": 28}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


+-------+------+----------------------------------------------------------------+
| Field | Name | Description                                                    |
+=======+======+================================================================+
| [0]   | MOSI | Output value for MOSI pin, valid whenever ``dir`` is ``0``.    |
+-------+------+----------------------------------------------------------------+
| [1]   | CLK  | Output value for SPI CLK pin.                                  |
+-------+------+----------------------------------------------------------------+
| [2]   | CS_N | Output value for SPI CSn pin.                                  |
+-------+------+----------------------------------------------------------------+
| [3]   | DIR  | Sets the direction for *ALL* SPI data pins except CLK and CSn. |
|       |      |                                                                |
|       |      | +-------+-------------------------+                            |
|       |      | | Value | Description             |                            |
|       |      | +=======+=========================+                            |
|       |      | | 0     | SPI pins are all output |                            |
|       |      | +-------+-------------------------+                            |
|       |      | | 1     | SPI pins are all input  |                            |
|       |      | +-------+-------------------------+                            |
+-------+------+----------------------------------------------------------------+

LXSPI_MISO
^^^^^^^^^^

`Address: 0x82007800 + 0x4 = 0x82007804`

    Incoming value of MISO signal.

    .. wavedrom::
        :caption: LXSPI_MISO

        {
            "reg": [
                {"name": "miso", "bits": 1},
                {"bits": 31},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


LXSPI_BITBANG_EN
^^^^^^^^^^^^^^^^

`Address: 0x82007800 + 0x8 = 0x82007808`

    Write a ``1`` here to disable memory-mapped mode and enable bitbang mode.

    .. wavedrom::
        :caption: LXSPI_BITBANG_EN

        {
            "reg": [
                {"name": "bitbang_en", "bits": 1},
                {"bits": 31},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


