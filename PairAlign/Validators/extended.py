from cerberus import Validator

VALIDATOR = Validator()

EXTENDED_SCHEMA = {
    "seq_type": {"required": True, "type": "string", "allowed": ["DNA", "PROTEIN"]},
    "sub_mat": {"required": True,
                "oneof": [
                    {
                        "type": "dict", "schema": {
                            "TG": {"required": True, "regex": "^-{0,1}[0-9]+$"},
                            "TC": {"required": True, "regex": "^-{0,1}[0-9]+$"},
                            "TA": {"required": True, "regex": "^-{0,1}[0-9]+$"},
                            "GC": {"required": True, "regex": "^-{0,1}[0-9]+$"},
                            "GA": {"required": True, "regex": "^-{0,1}[0-9]+$"},
                            "CA": {"required": True, "regex": "^-{0,1}[0-9]+$"},
                            "TT": {"required": True, "regex": "^-{0,1}[0-9]+$"},
                            "GG": {"required": True, "regex": "^-{0,1}[0-9]+$"},
                            "CC": {"required": True, "regex": "^-{0,1}[0-9]+$"},
                            "AA": {"required": True, "regex": "^-{0,1}[0-9]+$"}
                        },
                        "dependencies": {"seq_type": ["DNA"]}
                    },
                    {
                        "allowed": ["BLOSUM30", "BLOSUM45", "BLOSUM50", "BLOSUM60", "BLOSUM90"],
                        "dependencies": {"seq_type": ["PROTEIN"]}
                    },
                    {
                        "dependencies": ["match", "mismatch"],
                        "allowed": ["DEFAULT"]
                    }
                ]
                },
    "seq_a": {"required": True, "type": "string",
              "minlength": 1, "maxlength": 1000, "nullable": False, "oneof": [
                  {
                      "regex": "^[agtcAGTC]+$",
                      "dependencies": {"seq_type": ["DNA"]}
                  },
                  {
                      "regex": "^[abcdefghiklmnpqrstvwxyzABCDEFGHIKLMNPQRSTVWXYZ]+$",
                      "dependencies": {"seq_type": ["PROTEIN"]}
                  }
              ]},
    "seq_b": {"required": True, "type": "string",
              "minlength": 1, "maxlength": 1000, "nullable": False, "oneof": [
                  {
                      "regex": "^[agtcAGTC]+$",
                      "dependencies": {"seq_type": ["DNA"]}
                  },
                  {
                      "regex": "^[abcdefghiklmnpqrstvwxyzABCDEFGHIKLMNPQRSTVWXYZ]+$",
                      "dependencies": {"seq_type": ["PROTEIN"]}
                  }
              ]},
    "match": {"required": False, "nullable": True, 'type': 'integer', 'coerce': int},
    "mismatch": {"required": False, "nullable": True, 'type': 'integer', 'coerce': int},
    "opening_gap": {"required": True, "nullable": False, 'type': 'integer', 'coerce': int},
    "extending_gap": {"required": True, "nullable": False, 'type': 'integer', 'coerce': int},
    "priority": {"required": True, "type": "string", "minlength": 1, "allowed": ["HIGHROAD", "LOWROAD"]}
}


def validate_pair_align_extended(data):
    """
    validates extended pair align request
    """
    status = VALIDATOR.validate(data, EXTENDED_SCHEMA)
    return (status, VALIDATOR.errors)
