from package_a import module2
from package_a.package_b import module3


def greet(name: str) -> None:
    # module2.shout(f"Hello, {name}!")
    module2.shout(module3.add_prefix("Hello,", name))
