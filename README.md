# Merge multiple GenBank records using a defined spacer sequence

A small script to turn a multiple GenBank records (either in multiple files or a
single multi-record file) into a single record.

Sequences are merged by concatenating them in order, and putting a spacer
sequence between them. Spacer sequence length can be given in kbp. It is
possible to pick an all-N spacer, or using a spacer consisting of all-frame stop
codons.

## Installation

```
pip install merge-gbk-records
```

Alternatively, clone this repository from GitHub, then run (in a python virtual environment)
```
pip install .
```
If this fails on older versions of Python, try updating your `pip` tool first:
```
pip install --upgrade pip
```
and then rerun the `merge-gbk-records` install.

`merge-gbk-records` is only developed and tested on Python releases still under active
support by the Python project. At the moment, this means versions 2.7, 3.3, 3.4, 3.5 and 3.6.
Specifically, no attempt at testing under Python versions older than 2.7 or 3.3 is being made.

If your system is stuck on an older version of Python, consider using a tool like
[Homebrew](http://brew.sh) or [Linuxbrew](http://linuxbrew.sh) to obtain a more up-to-date
version.


## Usage


## License
All code is available under the Apache License version 2, see the
[`LICENSE`](LICENSE) file for details.
