# Amaranth-based OrangeCrab Examples

Using these examples requires Amaranth and it's dependencies to be installed.
Follow the directions for your environment on [the Amaranth documentation page](https://amaranth-lang.org/docs/amaranth/latest/install.html).

You will also need a fairly recent version of `amaranth-boards`.
This can be installed directly from GitHub using:

```bash
$ pip install --upgrade git+https://github.com/amaranth-lang/amaranth-boards#egg=amaranth-boards
```

# Building and Running
To build and load a design, put the device into dfu mode by plugging it in while holding
down the button (btn0), and then run the python file:

```bash
$ python blink.py
```
