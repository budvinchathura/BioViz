from cerberus import Validator

validator = Validator()

msaProgressiveSchema = {
    "sequences": {"required":True, "type":"list", "minlength":2, "maxlength":6, "nullable":False, "schema":{"type":"string", "minlength":1, "maxlength":100, "nullable":False, "regex":"^[a-zA-Z]+$"}},
    "order": {"required":True, "type":"list", "minlength":1, "maxlength":5, "empty":False, "schema": {"type": "list", 'items':[{'type': 'integer', 'coerce': int},{'type': 'integer', 'coerce': int}]}},
    "match": {"required":True, "nullable":False, 'type': 'integer', 'coerce': int},
    "mismatch": {"required":True, "nullable":False, 'type': 'integer', 'coerce': int},
    "gap": {"required":True, "nullable":False, 'type': 'integer', 'coerce': int}
}

msaProgressiveOptimalSchema = {
    "sequences": {"required":True, "type":"list", "minlength":2, "maxlength":6, "nullable":False, "schema":{"type":"string", "minlength":1, "maxlength":100, "nullable":False, "regex":"^[a-zA-Z]+$"}},
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