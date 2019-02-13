[![Build Status](https://travis-ci.org/afrendeiro/combat.svg?branch=master)](https://travis-ci.org/afrendeiro/combat)

Combat
==========
This is a fork of [Brent Pedersen's Python implementation of Combat](https://github.com/brentp/combat.py)

## Installation
```bash
pip install git+https://github.com/afrendeiro/combat.git
```

## Usage
```python
from combat import combat
```

## Testing
Currently tested on Travis for Python 2.7 and 3.6.

```python
pytest
```

## References

    Johnson WE, Rabinovic A, Li C (2007). Adjusting batch effects in microarray
    expression data using Empirical Bayes methods. Biostatistics 8:118-127.  

    Jeffrey T. Leek, W. Evan Johnson, Hilary S. Parker, Andrew E. Jaffe
    and John D. Storey (). sva: Surrogate Variable Analysis. R package
    version 3.4.0.

    https://github.com/brentp/combat.py
