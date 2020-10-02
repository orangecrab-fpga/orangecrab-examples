DDRPHY
======

Register Listing for DDRPHY
---------------------------

+----------------------------------------------------------------+------------------------------------------------+
| Register                                                       | Address                                        |
+================================================================+================================================+
| :ref:`DDRPHY_DLY_SEL <DDRPHY_DLY_SEL>`                         | :ref:`0x82003800 <DDRPHY_DLY_SEL>`             |
+----------------------------------------------------------------+------------------------------------------------+
| :ref:`DDRPHY_RDLY_DQ_RST <DDRPHY_RDLY_DQ_RST>`                 | :ref:`0x82003804 <DDRPHY_RDLY_DQ_RST>`         |
+----------------------------------------------------------------+------------------------------------------------+
| :ref:`DDRPHY_RDLY_DQ_INC <DDRPHY_RDLY_DQ_INC>`                 | :ref:`0x82003808 <DDRPHY_RDLY_DQ_INC>`         |
+----------------------------------------------------------------+------------------------------------------------+
| :ref:`DDRPHY_RDLY_DQ_BITSLIP_RST <DDRPHY_RDLY_DQ_BITSLIP_RST>` | :ref:`0x8200380c <DDRPHY_RDLY_DQ_BITSLIP_RST>` |
+----------------------------------------------------------------+------------------------------------------------+
| :ref:`DDRPHY_RDLY_DQ_BITSLIP <DDRPHY_RDLY_DQ_BITSLIP>`         | :ref:`0x82003810 <DDRPHY_RDLY_DQ_BITSLIP>`     |
+----------------------------------------------------------------+------------------------------------------------+
| :ref:`DDRPHY_BURSTDET_CLR <DDRPHY_BURSTDET_CLR>`               | :ref:`0x82003814 <DDRPHY_BURSTDET_CLR>`        |
+----------------------------------------------------------------+------------------------------------------------+
| :ref:`DDRPHY_BURSTDET_SEEN <DDRPHY_BURSTDET_SEEN>`             | :ref:`0x82003818 <DDRPHY_BURSTDET_SEEN>`       |
+----------------------------------------------------------------+------------------------------------------------+

DDRPHY_DLY_SEL
^^^^^^^^^^^^^^

`Address: 0x82003800 + 0x0 = 0x82003800`


    .. wavedrom::
        :caption: DDRPHY_DLY_SEL

        {
            "reg": [
                {"name": "dly_sel[1:0]", "bits": 2},
                {"bits": 30},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


DDRPHY_RDLY_DQ_RST
^^^^^^^^^^^^^^^^^^

`Address: 0x82003800 + 0x4 = 0x82003804`


    .. wavedrom::
        :caption: DDRPHY_RDLY_DQ_RST

        {
            "reg": [
                {"name": "rdly_dq_rst", "bits": 1},
                {"bits": 31},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


DDRPHY_RDLY_DQ_INC
^^^^^^^^^^^^^^^^^^

`Address: 0x82003800 + 0x8 = 0x82003808`


    .. wavedrom::
        :caption: DDRPHY_RDLY_DQ_INC

        {
            "reg": [
                {"name": "rdly_dq_inc", "bits": 1},
                {"bits": 31},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


DDRPHY_RDLY_DQ_BITSLIP_RST
^^^^^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x82003800 + 0xc = 0x8200380c`


    .. wavedrom::
        :caption: DDRPHY_RDLY_DQ_BITSLIP_RST

        {
            "reg": [
                {"name": "rdly_dq_bitslip_rst", "bits": 1},
                {"bits": 31},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


DDRPHY_RDLY_DQ_BITSLIP
^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x82003800 + 0x10 = 0x82003810`


    .. wavedrom::
        :caption: DDRPHY_RDLY_DQ_BITSLIP

        {
            "reg": [
                {"name": "rdly_dq_bitslip", "bits": 1},
                {"bits": 31},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


DDRPHY_BURSTDET_CLR
^^^^^^^^^^^^^^^^^^^

`Address: 0x82003800 + 0x14 = 0x82003814`


    .. wavedrom::
        :caption: DDRPHY_BURSTDET_CLR

        {
            "reg": [
                {"name": "burstdet_clr", "bits": 1},
                {"bits": 31},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


DDRPHY_BURSTDET_SEEN
^^^^^^^^^^^^^^^^^^^^

`Address: 0x82003800 + 0x18 = 0x82003818`


    .. wavedrom::
        :caption: DDRPHY_BURSTDET_SEEN

        {
            "reg": [
                {"name": "burstdet_seen[1:0]", "bits": 2},
                {"bits": 30},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


