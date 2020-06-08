from cerberus import Validator


class ExtendedValidator(Validator):
    ''' Add functionalities which doesn't in the generic library '''

    def _validate_pairing_length(self, other, field, value):
        """ Test length of MSA pairing order against length of sequences.

        The rule's arguments are validated against this schema:
        {'type': 'string'}
        """
        if other not in self.document:
            return False
        if len(value) != len(self.document[other]) - 1:
            self._error(field,
                        "Length of field %s doesn't match field %s's length." % (field, other))

    def _validate_pairing_validity(self, other, field, value):
        """ Test validity of the pairing against length of sequences.

        The rule's arguments are validated against this schema:
        {'type': 'string'}
        """
        if other not in self.document:
            return False
        n_sequences = len(self.document[other])
        current_set = set([])
        for i in range(1, n_sequences+1):
            current_set.add(i)
        flag = True

        for index, pair in enumerate(value):
            if not isinstance(pair, list):
                flag = False
                break
            if not len(pair) == 2:
                flag = False
                break
            if not((pair[0] in current_set) and (pair[1] in current_set) and (pair[0] != pair[1])):
                flag = False
                break
            current_set.remove(pair[0])
            current_set.remove(pair[1])
            current_set.add(n_sequences+index+1)

        if not flag:
            self._error(field, "Pairing order invalid")


VALIDATOR = ExtendedValidator()

MSA_PROGRESSIVE_SCHEMA = {
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
    "sequences": {"required": True, "type": "list",
                  "minlength": 2, "maxlength": 6, "nullable": False,
                  "oneof": [
                      {
                          "schema": {
                              "type": "string",
                              "minlength": 1,
                              "maxlength": 1000,
                              "nullable": False,
                              "regex": "^[agtcAGTC]+$"
                          },
                          "dependencies": {"seq_type": ["DNA"]}
                      },
                      {
                          "schema": {
                              "type": "string",
                              "minlength": 1,
                              "maxlength": 1000,
                              "nullable": False,
                              "regex": "^[abcdefghiklmnpqrstvwxyzABCDEFGHIKLMNPQRSTVWXYZ]+$"
                          },
                          "dependencies": {"seq_type": ["PROTEIN"]}
                      }
                  ]},
    "order": {"required": True,
              "type": "list",
              "empty": False,
              "schema": {"type": "list",
                         'items': [{'type': 'integer', 'coerce': int},
                                   {'type': 'integer', 'coerce': int}]},
              "pairing_length": "sequences",
              "pairing_validity": "sequences"},
    "match": {"required": True, "nullable": False, 'type': 'integer', 'coerce': int},
    "mismatch": {"required": True, "nullable": False, 'type': 'integer', 'coerce': int},
    "gap": {"required": True, "nullable": False, 'type': 'integer', 'coerce': int}
}

MSA_PROGRESSIVE_OPTIMAL_SCHEMA = {
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
    "sequences": {"required": True, "type": "list",
                  "minlength": 2, "maxlength": 6, "nullable": False, "oneof": [
                      {
                          "schema": {
                              "type": "string",
                              "minlength": 1,
                              "maxlength": 1000,
                              "nullable": False,
                              "regex": "^[agtcAGTC]+$"
                          },
                          "dependencies": {"seq_type": ["DNA"]}
                      },
                      {
                          "schema": {
                              "type": "string",
                              "minlength": 1,
                              "maxlength": 1000,
                              "nullable": False,
                              "regex": "^[abcdefghiklmnpqrstvwxyzABCDEFGHIKLMNPQRSTVWXYZ]+$"
                          },
                          "dependencies": {"seq_type": ["PROTEIN"]}
                      }
                  ]},
    "match": {"required": True, "nullable": False, 'type': 'integer', 'coerce': int},
    "mismatch": {"required": True, "nullable": False, 'type': 'integer', 'coerce': int},
    "gap": {"required": True, "nullable": False, 'type': 'integer', 'coerce': int}
}
# this doesn't checked


def validate_msa_progessive(data):
    """
    validates extended pair align request
    """
    status = VALIDATOR.validate(data, MSA_PROGRESSIVE_SCHEMA)
    return (status, VALIDATOR.errors)


def validate_msa_progessive_optimal(data):
    """
    validates extended pair align request
    """
    status = VALIDATOR.validate(data, MSA_PROGRESSIVE_OPTIMAL_SCHEMA)
    return (status, VALIDATOR.errors)
