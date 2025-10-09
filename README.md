# geomath-python-demo

Tiny 2D geometry helpers rewritten in Python with **one deliberate bug** to demo AI code-fixing.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pytest
```

`test_rotate_degrees_90_fails_intentionally` is expected to fail because of the deliberate bug
in ``Vector2D.rotate`` when `degrees=True`.
