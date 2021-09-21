"""
pip install validators
"""

import traceback
from voluptuous import Schema, MultipleInvalid, Required


schema = Schema({
    "q": str,
    Required("per_page"): int,
    "page": int,
})

data_1 = {
    "q": "hello world",
    "per_page": 20,
    "page": 10,
}

data_2 =  {
    "q": "hello world",
    "page": 10,
}

failure_data = {
    "q": "hello world",
    "per_page": "hi",
    "page": 10,
}

try:
    schema(data_2)
except MultipleInvalid as e:
    print(e.errors)
    # traceback.print_exc()
