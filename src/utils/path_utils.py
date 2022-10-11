from pathlib import Path


def filename(path: Path):
    name = path.name
    try:
        dot = name.rindex('.')
        return name[:dot]
    except ValueError:
        return name


def extension(path: Path):
    name = path.name
    try:
        dot = name.rindex('.')
        return name[dot + 1:]
    except ValueError:
        return None
