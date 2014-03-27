# coding=utf8

from django.test import TestCase
import jsonschema
import simplejson as json


class JsonSchemaTestCase(TestCase):
    def assertSchema(self, schema, content):
        try:
            jsonschema.validate(json.loads(content), schema)
        except jsonschema.ValidationError as e:
            self.fail(e.message)
        except json.JSONDecodeError as e:
            self.fail(e.message)
        except TypeError as e:
            self.fail(e.message)


class NotesTest(JsonSchemaTestCase):
    def test_schema(self):
        schema = {
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
        response = self.client.get('/api/notes')
        self.assertEqual(response.status_code, 200)
        self.assertSchema(schema, response.content)
        self.assertEqual(response['Content-Type'], 'application/json')
        #print response.content
        data = json.loads(response.content)
        jsonschema.validate(data, schema)


class Notes2Test(JsonSchemaTestCase):
    def test_schema(self):
        schema = {
            'type': 'object',
            'required': ['hoge'],
            'properties': {
                'hoge': {'type': 'string'},
                'mado': {'type': 'array'},
                'three': {'type': 'integer'},
            },
        }
        response = self.client.get('/api/notes2')
        self.assertEqual(response.status_code, 200)
        self.assertSchema(schema, response.content)
        self.assertEqual(response['Content-Type'], 'application/json')
        #print response.content
        data = json.loads(response.content)
        jsonschema.validate(data, schema)
