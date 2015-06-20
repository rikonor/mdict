### mdict [![Build Status](https://travis-ci.org/rikonor/mdict.svg?branch=master)](https://travis-ci.org/rikonor/mdict)

mdict is a utility for robustly **retrieving** / **storing** values in nested python dicts.

#### Installation

```bash
pip install mdict
```

#### Example

```python
from mdict import *

A = {}

# mset
mset(A, "address:street", "Pekan")  # Set "Pekan"

# mget
mget(A, "address:street", default="N/A")  # Return "Pekan"

# Change delimiter
mget(A, "address,street", delimiter=",")  # Return "Pekan"
```

#### Motivation

```python
# Ever have this happen to you?
users = [
    {"name": "John", "settings": {"new": False, "subscribed": True}},
    {"name": "Mack", "settings": {"new": True}}
]

for user in users:
    print user["settings"]["subscribed"]
    
# Traceback (most recent call last):
#   File "mdict.py", line xx, in <module>
#     print user["settings"]["subscribed"]
# KeyError: 'subscribed'

# One solution is to check for the key's existance
for user in users:
    if 'settings' in user and 'subscribed' in user['settings']:
        print user['subscribed']

# BUT wouldn't it be much nicer to be able to write
from mdict import *

for user in users:
    print mget(user, 'settings:subscribed', False)

# You can also use MDict to get the old dict syntax
from mdict import MDict
a = {'a': {'b': 1}}
a = MDict(a)
a.get('a:b')

```

##### * This tool was inspired by  [SaltStack](http://saltstack.com/)