"""Tiny test runner for the drills. Not an exercise: do not edit.

Each drill file ends with `run(globals())`. It calls every function whose
name starts with `test_` and prints TODO / PASS / FAIL / ERROR for each.
"""


def raises(exc, fn, *args, **kwargs):
    """Asserts that fn(*args, **kwargs) raises exc. Other exceptions propagate."""
    try:
        fn(*args, **kwargs)
    except exc:
        return
    raise AssertionError(f"{fn.__name__}{args} did not raise {exc.__name__}")


def run(namespace):
    tests = [(n, f) for n, f in namespace.items() if n.startswith("test_") and callable(f)]
    passed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"PASS  {name}")
            passed += 1
        except NotImplementedError:
            print(f"TODO  {name}")
        except AssertionError as e:
            print(f"FAIL  {name}: {e}")
        except Exception as e:
            print(f"ERROR {name}: {type(e).__name__}: {e}")
    print(f"\n{passed}/{len(tests)} passed")
