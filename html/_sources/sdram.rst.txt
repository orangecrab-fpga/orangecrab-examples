SDRAM
=====

Register Listing for SDRAM
--------------------------

+--------------------------------------------------------------------+--------------------------------------------------+
| Register                                                           | Address                                          |
+====================================================================+==================================================+
| :ref:`SDRAM_DFII_CONTROL <SDRAM_DFII_CONTROL>`                     | :ref:`0x82004000 <SDRAM_DFII_CONTROL>`           |
+--------------------------------------------------------------------+--------------------------------------------------+
| :ref:`SDRAM_DFII_PI0_COMMAND <SDRAM_DFII_PI0_COMMAND>`             | :ref:`0x82004004 <SDRAM_DFII_PI0_COMMAND>`       |
+--------------------------------------------------------------------+--------------------------------------------------+
| :ref:`SDRAM_DFII_PI0_COMMAND_ISSUE <SDRAM_DFII_PI0_COMMAND_ISSUE>` | :ref:`0x82004008 <SDRAM_DFII_PI0_COMMAND_ISSUE>` |
+--------------------------------------------------------------------+--------------------------------------------------+
| :ref:`SDRAM_DFII_PI0_ADDRESS <SDRAM_DFII_PI0_ADDRESS>`             | :ref:`0x8200400c <SDRAM_DFII_PI0_ADDRESS>`       |
+--------------------------------------------------------------------+--------------------------------------------------+
| :ref:`SDRAM_DFII_PI0_BADDRESS <SDRAM_DFII_PI0_BADDRESS>`           | :ref:`0x82004010 <SDRAM_DFII_PI0_BADDRESS>`      |
+--------------------------------------------------------------------+--------------------------------------------------+
| :ref:`SDRAM_DFII_PI0_WRDATA1 <SDRAM_DFII_PI0_WRDATA1>`             | :ref:`0x82004014 <SDRAM_DFII_PI0_WRDATA1>`       |
+--------------------------------------------------------------------+--------------------------------------------------+
| :ref:`SDRAM_DFII_PI0_WRDATA0 <SDRAM_DFII_PI0_WRDATA0>`             | :ref:`0x82004018 <SDRAM_DFII_PI0_WRDATA0>`       |
+--------------------------------------------------------------------+--------------------------------------------------+
| :ref:`SDRAM_DFII_PI0_RDDATA1 <SDRAM_DFII_PI0_RDDATA1>`             | :ref:`0x8200401c <SDRAM_DFII_PI0_RDDATA1>`       |
+--------------------------------------------------------------------+--------------------------------------------------+
| :ref:`SDRAM_DFII_PI0_RDDATA0 <SDRAM_DFII_PI0_RDDATA0>`             | :ref:`0x82004020 <SDRAM_DFII_PI0_RDDATA0>`       |
+--------------------------------------------------------------------+--------------------------------------------------+
| :ref:`SDRAM_DFII_PI1_COMMAND <SDRAM_DFII_PI1_COMMAND>`             | :ref:`0x82004024 <SDRAM_DFII_PI1_COMMAND>`       |
+--------------------------------------------------------------------+--------------------------------------------------+
| :ref:`SDRAM_DFII_PI1_COMMAND_ISSUE <SDRAM_DFII_PI1_COMMAND_ISSUE>` | :ref:`0x82004028 <SDRAM_DFII_PI1_COMMAND_ISSUE>` |
+--------------------------------------------------------------------+--------------------------------------------------+
| :ref:`SDRAM_DFII_PI1_ADDRESS <SDRAM_DFII_PI1_ADDRESS>`             | :ref:`0x8200402c <SDRAM_DFII_PI1_ADDRESS>`       |
+--------------------------------------------------------------------+--------------------------------------------------+
| :ref:`SDRAM_DFII_PI1_BADDRESS <SDRAM_DFII_PI1_BADDRESS>`           | :ref:`0x82004030 <SDRAM_DFII_PI1_BADDRESS>`      |
+--------------------------------------------------------------------+--------------------------------------------------+
| :ref:`SDRAM_DFII_PI1_WRDATA1 <SDRAM_DFII_PI1_WRDATA1>`             | :ref:`0x82004034 <SDRAM_DFII_PI1_WRDATA1>`       |
+--------------------------------------------------------------------+--------------------------------------------------+
| :ref:`SDRAM_DFII_PI1_WRDATA0 <SDRAM_DFII_PI1_WRDATA0>`             | :ref:`0x82004038 <SDRAM_DFII_PI1_WRDATA0>`       |
+--------------------------------------------------------------------+--------------------------------------------------+
| :ref:`SDRAM_DFII_PI1_RDDATA1 <SDRAM_DFII_PI1_RDDATA1>`             | :ref:`0x8200403c <SDRAM_DFII_PI1_RDDATA1>`       |
+--------------------------------------------------------------------+--------------------------------------------------+
| :ref:`SDRAM_DFII_PI1_RDDATA0 <SDRAM_DFII_PI1_RDDATA0>`             | :ref:`0x82004040 <SDRAM_DFII_PI1_RDDATA0>`       |
+--------------------------------------------------------------------+--------------------------------------------------+

SDRAM_DFII_CONTROL
^^^^^^^^^^^^^^^^^^

`Address: 0x82004000 + 0x0 = 0x82004000`


    .. wavedrom::
        :caption: SDRAM_DFII_CONTROL

        {
            "reg": [
                {"name": "sel",  "attr": '1', "bits": 1},
                {"name": "cke",  "bits": 1},
                {"name": "odt",  "bits": 1},
                {"name": "reset_n",  "bits": 1},
                {"bits": 28}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


+-------+---------+-------------------------------------------+
| Field | Name    | Description                               |
+=======+=========+===========================================+
| [0]   | SEL     |                                           |
|       |         |                                           |
|       |         | +---------+-----------------------------+ |
|       |         | | Value   | Description                 | |
|       |         | +=========+=============================+ |
|       |         | | ``0b0`` | Software (CPU) control.     | |
|       |         | +---------+-----------------------------+ |
|       |         | | ``0b1`  | Hardware control (default). | |
|       |         | +---------+-----------------------------+ |
+-------+---------+-------------------------------------------+
+-------+---------+-------------------------------------------+
+-------+---------+-------------------------------------------+
+-------+---------+-------------------------------------------+

SDRAM_DFII_PI0_COMMAND
^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x82004000 + 0x4 = 0x82004004`


    .. wavedrom::
        :caption: SDRAM_DFII_PI0_COMMAND

        {
            "reg": [
                {"name": "dfii_pi0_command[5:0]", "bits": 6},
                {"bits": 26},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


SDRAM_DFII_PI0_COMMAND_ISSUE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x82004000 + 0x8 = 0x82004008`


    .. wavedrom::
        :caption: SDRAM_DFII_PI0_COMMAND_ISSUE

        {
            "reg": [
                {"name": "dfii_pi0_command_issue", "bits": 1},
                {"bits": 31},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


SDRAM_DFII_PI0_ADDRESS
^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x82004000 + 0xc = 0x8200400c`


    .. wavedrom::
        :caption: SDRAM_DFII_PI0_ADDRESS

        {
            "reg": [
                {"name": "dfii_pi0_address[12:0]", "bits": 13},
                {"bits": 19},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


SDRAM_DFII_PI0_BADDRESS
^^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x82004000 + 0x10 = 0x82004010`


    .. wavedrom::
        :caption: SDRAM_DFII_PI0_BADDRESS

        {
            "reg": [
                {"name": "dfii_pi0_baddress[2:0]", "bits": 3},
                {"bits": 29},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


SDRAM_DFII_PI0_WRDATA1
^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x82004000 + 0x14 = 0x82004014`

    Bits 32-63 of `SDRAM_DFII_PI0_WRDATA`.

    .. wavedrom::
        :caption: SDRAM_DFII_PI0_WRDATA1

        {
            "reg": [
                {"name": "dfii_pi0_wrdata[63:32]", "bits": 32}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


SDRAM_DFII_PI0_WRDATA0
^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x82004000 + 0x18 = 0x82004018`

    Bits 0-31 of `SDRAM_DFII_PI0_WRDATA`.

    .. wavedrom::
        :caption: SDRAM_DFII_PI0_WRDATA0

        {
            "reg": [
                {"name": "dfii_pi0_wrdata[31:0]", "bits": 32}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


SDRAM_DFII_PI0_RDDATA1
^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x82004000 + 0x1c = 0x8200401c`

    Bits 32-63 of `SDRAM_DFII_PI0_RDDATA`.

    .. wavedrom::
        :caption: SDRAM_DFII_PI0_RDDATA1

        {
            "reg": [
                {"name": "dfii_pi0_rddata[63:32]", "bits": 32}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


SDRAM_DFII_PI0_RDDATA0
^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x82004000 + 0x20 = 0x82004020`

    Bits 0-31 of `SDRAM_DFII_PI0_RDDATA`.

    .. wavedrom::
        :caption: SDRAM_DFII_PI0_RDDATA0

        {
            "reg": [
                {"name": "dfii_pi0_rddata[31:0]", "bits": 32}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


SDRAM_DFII_PI1_COMMAND
^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x82004000 + 0x24 = 0x82004024`


    .. wavedrom::
        :caption: SDRAM_DFII_PI1_COMMAND

        {
            "reg": [
                {"name": "dfii_pi1_command[5:0]", "bits": 6},
                {"bits": 26},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


SDRAM_DFII_PI1_COMMAND_ISSUE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x82004000 + 0x28 = 0x82004028`


    .. wavedrom::
        :caption: SDRAM_DFII_PI1_COMMAND_ISSUE

        {
            "reg": [
                {"name": "dfii_pi1_command_issue", "bits": 1},
                {"bits": 31},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


SDRAM_DFII_PI1_ADDRESS
^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x82004000 + 0x2c = 0x8200402c`


    .. wavedrom::
        :caption: SDRAM_DFII_PI1_ADDRESS

        {
            "reg": [
                {"name": "dfii_pi1_address[12:0]", "bits": 13},
                {"bits": 19},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


SDRAM_DFII_PI1_BADDRESS
^^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x82004000 + 0x30 = 0x82004030`


    .. wavedrom::
        :caption: SDRAM_DFII_PI1_BADDRESS

        {
            "reg": [
                {"name": "dfii_pi1_baddress[2:0]", "bits": 3},
                {"bits": 29},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


SDRAM_DFII_PI1_WRDATA1
^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x82004000 + 0x34 = 0x82004034`

    Bits 32-63 of `SDRAM_DFII_PI1_WRDATA`.

    .. wavedrom::
        :caption: SDRAM_DFII_PI1_WRDATA1

        {
            "reg": [
                {"name": "dfii_pi1_wrdata[63:32]", "bits": 32}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


SDRAM_DFII_PI1_WRDATA0
^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x82004000 + 0x38 = 0x82004038`

    Bits 0-31 of `SDRAM_DFII_PI1_WRDATA`.

    .. wavedrom::
        :caption: SDRAM_DFII_PI1_WRDATA0

        {
            "reg": [
                {"name": "dfii_pi1_wrdata[31:0]", "bits": 32}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


SDRAM_DFII_PI1_RDDATA1
^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x82004000 + 0x3c = 0x8200403c`

    Bits 32-63 of `SDRAM_DFII_PI1_RDDATA`.

    .. wavedrom::
        :caption: SDRAM_DFII_PI1_RDDATA1

        {
            "reg": [
                {"name": "dfii_pi1_rddata[63:32]", "bits": 32}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


SDRAM_DFII_PI1_RDDATA0
^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x82004000 + 0x40 = 0x82004040`

    Bits 0-31 of `SDRAM_DFII_PI1_RDDATA`.

    .. wavedrom::
        :caption: SDRAM_DFII_PI1_RDDATA0

        {
            "reg": [
                {"name": "dfii_pi1_rddata[31:0]", "bits": 32}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


