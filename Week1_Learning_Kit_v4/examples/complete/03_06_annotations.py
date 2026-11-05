def echo(value: int) -> int:
    return value

print(echo(42))
print(echo("42"))  # Also prints 42, but returns a str.
print(type(echo("42")).__name__)  # str
