# Bink Test
This is my solution for the Bink Test Project

## Getting Started

These are the instruction to clone, install, run and test the programme.

### Prerequisites

The software relies on the following packages, all of which are available via pip install

```
tabulate
python-dateutil
```

### Cloning

The repository can be cloned from

```
git clone https://github.com/bobrien01/bink.git
```

## Running

The programme can be run with:
```
python bink.py
```

Then the user can select from several options.
```
0 - Do all of the following
1 - Sort by Current Rent and select the lowest 5
2 - Filter on lease = 25 years
3 - Create dict of tenant name and mast counts
4 - Filter leases between 1 June 1999 and 31 Aug 2007
quit to quit
```

## Running the tests
The test can be run with:
```
pytest -v test_bink.py
```
