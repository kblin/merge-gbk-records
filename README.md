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

By default, `merge-gbk-records` will add a 20 kbp spacer of all `N`s and output
the merged record on the terminal.

```
merge-gbk-records first.gbk second.gbk > merged.gbk
```

You can set different lengths using `-l` or `--length`. To use a 5 kbp spacer, use:
```
merge-gbk-records --length 5 first.gbk second.gbk > merged.gbk
```

You can select an all-frame stop codon spacer instead using `-s stop` or `--spacer stop`:
```
merge-gbk-records --spacer stop first.gbk second.gbk > merged.gbk
```

Instead of writing to stdout, you can also write to a file using `-o` or `--outfile`:
```
merge-gbk-records --outfile merged.gbk first.gbk second.gbk
```

To print help about the command, just run it with `-h` or `--help`:
```
merge-gbk-records --help
```

## License
All code is available under the Apache License version 2, see the
[`LICENSE`](LICENSE) file for details.
