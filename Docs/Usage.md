# Usage Guide

Import utilities:

```python
from src.scripts.preprocess import preprocess_entry
```

Process a record:

```python
record = {"content": " messy   text   "}
result = preprocess_entry(record)
```

Use metadata tools for validation and loading.
