from app.errors import ConfigNotFoundError
import yaml
import os.path


def read_yaml(filename):
    if not os.path.isfile(filename):
        raise ConfigNotFoundError('The file %s is not found' % filename)

    doc = {}

    with open(filename, 'r') as f:
        doc = yaml.load(f)

    return doc
