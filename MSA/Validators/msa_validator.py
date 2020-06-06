from cerberus import Validator


class ExtendedValidator(Validator):
    ''' Add functionalities which doesn't in the generic library '''
    def _validate_order_length(self, other, field, value):
        """ Test length of order agains length of sequences.

        The rule's arguments are validated against this schema:
        {'type': 'string'}
        """
        if other not in self.document:
            return False
        if len(value) != len(self.document[other]) - 1:
            self._error(field,
                        "Length of field %s doesn't match field %s's length." %(field, other))
    
    def _validate_item_range(self, other, field, value):
        """ Test validity of the items against length of sequences.

        The rule's arguments are validated against this schema:
        {'type': 'string'}
        """
        if other not in self.document:
            return False
        for sub in value:
            for n in sub:
                if 1 > int(n) or int(n) > (2*len(self.document[other]) - 2):
                    self._error(field,
                        "Values should be in range %s - %s" %(1, 2*len(self.document[other]) - 2))
                    

    def _validate_unique(self, argument, field, value):
        """ Test uniqueness of order items.

        The rule's arguments are validated against this schema:
        {'type': 'boolean'}
        """
        temp = []
        for sub in value:
            for n in sub:
                if n not in temp:
                    temp.append(n)
                elif not argument:
                    pass
                else:
                    self._error(field,
                        "Values should be unique")

    def _validate_unique(self, argument, field, value):
        """ Test uniqueness of order items.

        The rule's arguments are validated against this schema:
        {'type': 'boolean'}
        """
        temp = []
        
        for sub in value:
            for n in sub:
                if n not in temp:
                    temp.append(n)
                elif not argument:
                    pass
                else:
                    self._error(field,
                        "Values should be unique")


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
                              "regex": "^[a-zA-Z]+$"
                          },
                          "dependencies": {"seq_type": ["PROTEIN"]}
                      }
                  ]},
    "order": {"required": True, "type": "list", "order_length": "sequences", "empty": False,
              "unique": True, "item_range": "sequences", "schema": {"type": "list",
                         'items': [{'type': 'integer', 'coerce': int},
                                   {'type': 'integer', 'coerce': int}]}},
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
                              "regex": "^[a-zA-Z]+$"
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
