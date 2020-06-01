from cerberus import Validator

validator = Validator()

msaProgressiveSchema = {
    "seq_type":{"required": True, "type": "string", "allowed": ["DNA", "PROTEIN"]},
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
    "sequences": {"required":True, "type":"list", "minlength":2, "maxlength":6, "nullable":False, "oneof":[
        {
            "schema":{
                "type":"string", 
                "minlength":1, 
                "maxlength":1000, 
                "nullable":False, 
                "regex": "^[agtcAGTC]+$"
                },
                "dependencies": {"seq_type": ["DNA"]}
        },
        {
            "schema":{
                "type":"string", 
                "minlength":1, 
                "maxlength":1000, 
                "nullable":False, 
                "regex": "^[a-zA-Z]+$"
                },
                "dependencies": {"seq_type": ["PROTEIN"]}
        }
        ]},
    "order": {"required":True, "type":"list", "minlength":1, "maxlength":5, "empty":False, "schema": {"type": "list", 'items':[{'type': 'integer', 'coerce': int},{'type': 'integer', 'coerce': int}]}},
    "match": {"required":True, "nullable":False, 'type': 'integer', 'coerce': int},
    "mismatch": {"required":True, "nullable":False, 'type': 'integer', 'coerce': int},
    "gap": {"required":True, "nullable":False, 'type': 'integer', 'coerce': int}
}

msaProgressiveOptimalSchema = {
    "seq_type":{"required": True, "type": "string", "allowed": ["DNA", "PROTEIN"]},
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
    "sequences": {"required":True, "type":"list", "minlength":2, "maxlength":6, "nullable":False, "oneof":[
        {
            "schema":{
                "type":"string", 
                "minlength":1, 
                "maxlength":1000, 
                "nullable":False, 
                "regex": "^[agtcAGTC]+$"
                },
                "dependencies": {"seq_type": ["DNA"]}
        },
        {
            "schema":{
                "type":"string", 
                "minlength":1, 
                "maxlength":1000, 
                "nullable":False, 
                "regex": "^[a-zA-Z]+$"
                },
                "dependencies": {"seq_type": ["PROTEIN"]}
        }
        ]},
    "match": {"required":True, "nullable":False, 'type': 'integer', 'coerce': int},
    "mismatch": {"required":True, "nullable":False, 'type': 'integer', 'coerce': int},
    "gap": {"required":True, "nullable":False, 'type': 'integer', 'coerce': int}
}
#this doesn't checked

def validate_msa_progessive(data):
    """
    validates extended pair align request
    """
    try:
        length = len(data['sequences'])
        msaProgressiveSchema['order']['minlength'] = int(length) -1
        msaProgressiveSchema['order']['maxlength'] = int(length) -1
    except:
        msaProgressiveSchema['order']['minlength'] = 1
        msaProgressiveSchema['order']['maxlength'] = 5

    status = validator.validate(data, msaProgressiveSchema)
    return (status, validator.errors)

def validate_msa_progessive_optimal(data):
    """
    validates extended pair align request
    """
    status = validator.validate(data, msaProgressiveOptimalSchema)
    return (status, validator.errors)