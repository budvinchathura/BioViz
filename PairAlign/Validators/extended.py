from cerberus import Validator

validator = Validator()

extendedSchema1 = {
        "seq_type" : {"required":True, "type":"string", "allowed": ["PROTEIN"]},
        "sub_mat" : {"required":True, "type":"string", "allowed": ["DEFAULT"]},
        "seq_a" : {"required":True, "type":"string", "minlength":1, "maxlength":100, "nullable":False, "regex":"^[a-zA-Z]+$"},
        "seq_b" : {"required":True, "type":"string", "minlength":1, "maxlength":100, "nullable":False, "regex":"^[a-zA-Z]+$"},
        "match" : {"required":True, "nullable":False, 'type': 'integer', 'coerce': int},
        "mismatch" : {"required":True, "nullable":False, 'type': 'integer', 'coerce': int},
        "opening_gap" : {"required":True, "nullable":False, 'type': 'integer', 'coerce': int},
        "extending_gap" : {"required":True, "nullable":False, 'type': 'integer', 'coerce': int},
        "priority" : {"required":True, "type":"string", "minlength":1, "allowed": ["HIGHROAD", "LOWROAD"]}
}

extendedSchema2 = {
        "seq_type" : {"required":True, "type":"string", "allowed": ["DNA"]},
        "sub_mat" : {"required":True, "type":"string", "allowed": ["DEFAULT"]},
        "seq_a" : {"required":True, "type":"string", "minlength":1, "maxlength":100, "nullable":False, "regex":"^[agtcAGTC]+$"},
        "seq_b" : {"required":True, "type":"string", "minlength":1, "maxlength":100, "nullable":False, "regex":"^[agtcAGTC]+$"},
        "match" : {"required":True, "nullable":False, 'type': 'integer', 'coerce': int},
        "mismatch" : {"required":True, "nullable":False, 'type': 'integer', 'coerce': int},
        "opening_gap" : {"required":True, "nullable":False, 'type': 'integer', 'coerce': int},
        "extending_gap" : {"required":True, "nullable":False, 'type': 'integer', 'coerce': int},
        "priority" : {"required":True, "type":"string", "minlength":1, "allowed": ["HIGHROAD", "LOWROAD"]}
}

extendedSchema3 = {
        "seq_type" : {"required":True, "type":"string", "allowed": ["DNA"]},
        "sub_mat" : {"required":True, "type":"dict", "keysrules":{"regex":"^[AGTC]{2}$"}, "valuesrules":{'type': 'integer', 'coerce': int}},
        "seq_a" : {"required":True, "type":"string", "minlength":1, "maxlength":100, "nullable":False, "regex":"^[agtcAGTC]+$"},
        "seq_b" : {"required":True, "type":"string", "minlength":1, "maxlength":100, "nullable":False, "regex":"^[agtcAGTC]+$"},
        "match" : {"required":False, "nullable":True, 'type': 'integer', 'coerce': int},
        "mismatch" : {"required":False, "nullable":True, 'type': 'integer', 'coerce': int},
        "opening_gap" : {"required":True, "nullable":False, 'type': 'integer', 'coerce': int},
        "extending_gap" : {"required":True, "nullable":False, 'type': 'integer', 'coerce': int},
        "priority" : {"required":True, "type":"string", "minlength":1, "allowed": ["HIGHROAD", "LOWROAD"]}
}

extendedSchema4 = {
        "seq_type" : {"required":True, "type":"string", "allowed": ["PROTEIN"]},
        "sub_mat" : {"required":True, "type":"string", "allowed": ["BLOSUM30", "BLOSUM45", "BLOSUM50", "BLOSUM60", "BLOSUM90"]},
        "seq_a" : {"required":True, "type":"string", "minlength":1, "maxlength":100, "nullable":False, "regex":"^[a-zA-Z]+$"},
        "seq_b" : {"required":True, "type":"string", "minlength":1, "maxlength":100, "nullable":False, "regex":"^[a-zA-Z]+$"},
        "match" : {"required":False, "nullable":True, 'type': 'integer', 'coerce': int},
        "mismatch" : {"required":False, "nullable":True, 'type': 'integer', 'coerce': int},
        "opening_gap" : {"required":True, "nullable":False, 'type': 'integer', 'coerce': int},
        "extending_gap" : {"required":True, "nullable":False, 'type': 'integer', 'coerce': int},
        "priority" : {"required":True, "type":"string", "minlength":1, "allowed": ["HIGHROAD", "LOWROAD"]}
}

def validate_pair_align_extended(data):
    """
    validates extended pair align request
    """
    status1 = validator.validate(data, extendedSchema1)
    e1 = validator.errors
    status2 = validator.validate(data, extendedSchema2)
    e2 = validator.errors
    status3 = validator.validate(data, extendedSchema3)
    e3 = validator.errors
    status4 = validator.validate(data, extendedSchema4)
    e4 = validator.errors
    status = status1 or status2 or status3 or status4
    e = [e1, e2, e3, e4]
    # print([e1, e2, e3, e4])
    return (status, e)