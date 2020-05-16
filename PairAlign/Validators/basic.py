from cerberus import Validator
SCHEMA = {'seq_a': {'type': 'string'},
          'seq_b': {'type': 'string'},
          'match': {'type': 'integer', 'coerce': int},
          'mismatch': {'type': 'integer', 'coerce': int},
          'gap': {'type': 'integer', 'coerce': int}
          }


def validate_pair_align(data):
    """
    validates basic pair align request
    """
    validator = Validator(SCHEMA)
    status = validator.validate(data)
    return (status, validator.errors)
