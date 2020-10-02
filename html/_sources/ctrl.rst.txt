CTRL
====

Register Listing for CTRL
-------------------------

+------------------------------------------+-------------------------------------+
| Register                                 | Address                             |
+==========================================+=====================================+
| :ref:`CTRL_RESET <CTRL_RESET>`           | :ref:`0x82000000 <CTRL_RESET>`      |
+------------------------------------------+-------------------------------------+
| :ref:`CTRL_SCRATCH <CTRL_SCRATCH>`       | :ref:`0x82000004 <CTRL_SCRATCH>`    |
+------------------------------------------+-------------------------------------+
| :ref:`CTRL_BUS_ERRORS <CTRL_BUS_ERRORS>` | :ref:`0x82000008 <CTRL_BUS_ERRORS>` |
+------------------------------------------+-------------------------------------+

CTRL_RESET
^^^^^^^^^^

`Address: 0x82000000 + 0x0 = 0x82000000`

    Write a ``1`` to this register to reset the SoC.

    .. wavedrom::
        :caption: CTRL_RESET

        {
            "reg": [
                {"name": "reset", "bits": 1},
                {"bits": 31},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


CTRL_SCRATCH
^^^^^^^^^^^^

`Address: 0x82000000 + 0x4 = 0x82000004`

    Use this register as a scratch space to verify that software read/write accesses
    to the Wishbone/CSR bus are working correctly. The initial reset value of
    0x1234578 can be used to verify endianness.

    .. wavedrom::
        :caption: CTRL_SCRATCH

        {
            "reg": [
                {"name": "scratch[31:0]", "attr": 'reset: 305419896', "bits": 32}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


CTRL_BUS_ERRORS
^^^^^^^^^^^^^^^

`Address: 0x82000000 + 0x8 = 0x82000008`

    Total number of Wishbone bus errors (timeouts) since start.

    .. wavedrom::
        :caption: CTRL_BUS_ERRORS

        {
            "reg": [
                {"name": "bus_errors[31:0]", "bits": 32}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


