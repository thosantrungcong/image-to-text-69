from sys import stdout

from logging import INFO, Formatter, StreamHandler, Logger, getLogger

werkzeug_log = getLogger(name="werkzeug")
werkzeug_log.disabled = True

def create_log(name: str) -> Logger:
    log = getLogger(name=name)

    log.setLevel(level=INFO)
    log.propagate = False

    if log.handlers:
        return log


    handler = StreamHandler(stream=stdout)

    formatter = Formatter(
        fmt="-> %(asctime)s %(message)s",
        datefmt="%H:%M:%S"
    )

    handler.setFormatter(fmt=formatter)
    log.addHandler(hdlr=handler)

    return log