BUTTON
======

Register Listing for BUTTON
---------------------------

+------------------------------+-------------------------------+
| Register                     | Address                       |
+==============================+===============================+
| :ref:`BUTTON_IN <BUTTON_IN>` | :ref:`0x82008800 <BUTTON_IN>` |
+------------------------------+-------------------------------+

BUTTON_IN
^^^^^^^^^

`Address: 0x82008800 + 0x0 = 0x82008800`

    GPIO Input(s) Status.

    .. wavedrom::
        :caption: BUTTON_IN

        {
            "reg": [
                {"name": "in", "bits": 1},
                {"bits": 31},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


