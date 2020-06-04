from cerberus import Validator

VALIDATOR = Validator()


SCHEMA = {'seq_a': {'type': 'string'},
          'seq_b': {'type': 'string'},
          'match': {'type': 'integer', 'coerce': int},
          'mismatch': {'type': 'integer', 'coerce': int},
          'gap': {'type': 'integer', 'coerce': int}
          }

BASIC_SCHEMA = {
    "seq_a": {"required": True, "type": "string",
              "minlength": 1, "maxlength": 1000, "nullable": False, "regex": "^[a-zA-Z]+$"},
    "seq_b": {"required": True, "type": "string",
              "minlength": 1, "maxlength": 1000, "nullable": False, "regex": "^[a-zA-Z]+$"},
    "match": {"required": True, "nullable": False, 'type': 'integer', 'coerce': int},
    "mismatch": {"required": True, "nullable": False, 'type': 'integer', 'coerce': int},
    "gap": {"required": True, "nullable": False, 'type': 'integer', 'coerce': int}
}


def validate_pair_align_basic(data):
    """
    validates basic pair align request
    """
    # validator = Validator(SCHEMA)
    status = VALIDATOR.validate(data, BASIC_SCHEMA)
    return (status, VALIDATOR.errors)
