# coding=utf8

from django.test import TestCase
import jsonschema
import simplejson as json

from . import jsonschemas


class JsonSchemaTestCase(TestCase):
    def assertSchema(self, schema, content):
        try:
            jsonschema.validate(json.loads(content), schema)
        except json.JSONDecodeError as e:
            # json 形式が不正の場合
            self.fail(e.message)
        except jsonschema.ValidationError as e:
            if e.validator == 'required':
                self.fail(e.message)
            else:
                self.fail(e.message)


class NotesTest(JsonSchemaTestCase):
    def test_schema(self):
        response = self.client.get('/api/notes')
        self.assertEqual(response.status_code, 200)
        self.assertSchema(jsonschemas.notes_response, response.content)
        self.assertEqual(response['Content-Type'], 'application/json')


class Notes2Test(JsonSchemaTestCase):
    def test_schema(self):
        response = self.client.get('/api/notes2')
        self.assertEqual(response.status_code, 200)
        self.assertSchema(jsonschemas.notes2_response, response.content)
        self.assertEqual(response['Content-Type'], 'application/json')
        # print response.content
        # data = json.loads(response.content)
        # jsonschema.validate(data, schema)
