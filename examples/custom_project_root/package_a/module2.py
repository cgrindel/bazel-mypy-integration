from package_a import module1


def shout(msg: str) -> None:
    module1.echo(msg.upper())
