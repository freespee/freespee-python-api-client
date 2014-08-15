# Basic usage

```python
from freespee_api import Freespee

api = Freespee('tag', 'password')
response = api.get('customers')

print response.result
```

See example.py for a more elaborate example.
