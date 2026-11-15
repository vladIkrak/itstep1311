result = []


def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a / b


data = [(10, 2), (2, 5), ("123", 4), (18, 0), ([], 15), (8, 4), (150, 101)]

for a, b in data:
    try:
        res = divider(a, b)
    except ValueError as e:
        print(f"ValueError: a={a!r} is less than b={b!r} ({e!r})")
    except IndexError as e:
        print(f"IndexError: b={b!r} is greater than 100 ({e!r})")
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: dividing {a!r} by {b!r} ({e})")
    except TypeError as e:
        print(f"TypeError: {e}")
    except Exception as e:
        print(f"Other error {type(e).__name__}: {e}")
    else:
        result.append(res)

print(result)