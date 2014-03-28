# coding=utf8

notes_requests = {
}

notes_response = {
    'type': 'object',
    'required': ['hoge'],
    'properties': {
        'hoge': {'type': 'string'},
        'mado': {
            'type': 'array',
            'minItems': 1,
            'items': {'type': 'integer'},
            'uniqueItems': True,
        },
        'three': {'type': 'integer'},
    },
}

notes2_response = notes_response
