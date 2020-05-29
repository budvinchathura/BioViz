from cerberus import Validator

validator = Validator()

extendedSchema = {
        "seq_type" : {"required":True, "type":"string", "allowed": ["DNA","PROTEIN"]},
        "sub_mat" : {"required":True, 
        "oneof": [
            {
                "type":"dict", "schema":{"TG":{"regex":"^-{0,1}[0-9]+$"},
                "TC":{"regex":"^-{0,1}[0-9]+$"},
                "TA":{"regex":"^-{0,1}[0-9]+$"},
                "GC":{"regex":"^-{0,1}[0-9]+$"},
                "GA":{"regex":"^-{0,1}[0-9]+$"},
                "CA":{"regex":"^-{0,1}[0-9]+$"},
                "TT":{"regex":"^-{0,1}[0-9]+$"},
                "GG":{"regex":"^-{0,1}[0-9]+$"},
                "CC":{"regex":"^-{0,1}[0-9]+$"},
                "AA":{"regex":"^-{0,1}[0-9]+$"}
                },
                "dependencies": {"seq_type":["DNA"]}
            },
            {
                # "allowed": ["BLOSUM30", "BLOSUM45", "BLOSUM50", "BLOSUM60", "BLOSUM90"],
                "allowed": ["BLOSUM45", "BLOSUM50", "BLOSUM62", "BLOSUM90"],
                "dependencies": {"seq_type":["PROTEIN"]}
            },
            {
                "dependencies": ["match", "mismatch"],
                "allowed": ["DEFAULT"]
            }
            ]
            },
        "seq_a" : {"required":True, "type":"string", "minlength":1, "maxlength":100, "nullable":False, "oneof":[
                {
                        "regex":"^[agtcAGTC]+$",
                        "dependencies": {"seq_type":["DNA"]}
                },
                {
                        "regex":"^[a-zA-Z]+$",
                        "dependencies": {"seq_type":["PROTEIN"]}
                }
        ]},
        "seq_b" : {"required":True, "type":"string", "minlength":1, "maxlength":100, "nullable":False, "oneof":[
                {
                        "regex":"^[agtcAGTC]+$",
                        "dependencies": {"seq_type":["DNA"]}
                },
                {
                        "regex":"^[a-zA-Z]+$",
                        "dependencies": {"seq_type":["PROTEIN"]}
                }
        ]},
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
    status = validator.validate(data, extendedSchema)
    return (status, validator.errors)