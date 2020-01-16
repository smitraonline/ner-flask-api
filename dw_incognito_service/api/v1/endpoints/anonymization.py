import logging
import json

from flask import request
from flask_restplus import fields
from flask_restplus import Resource
from dw_incognito_service.api.restplus import api
from dw_incognito_service.parsers import nltk_ner_parser
from dw_incognito_service.parsers import phone_parser
from dw_incognito_service.parsers import email_parser

log = logging.getLogger(__name__)

ns = api.namespace('v1/anonymizer', description='Operations related to anonymization')


@ns.route('/')
class Hello(Resource):
    @api.response(200, 'Anonymizer is running.')
    #@api.marshal_list_with(input)
    def get(self):
        """
        Health check.
        """
        return "hello", 200
    @api.response(200, 'Anonymizer is running.')
    # @api.expect(input)
    def put(self):
        """
        Health check.
        """
        data = request.json
        return "hello", 200


input = ns.model('input', {
    'data': fields.String(required=True, description='raw data'),
})

@ns.route('/tokenize')
@api.response(200, 'Process Successful.')
class Tokenizer(Resource):
    @ns.expect(input)
    def post(self):
        """
        Tokenize any String and tag parts of speech.
        """
        json_data = request.json
        output = nltk_ner.tokenize(json_data["data"])
        return {"data": output}, 200

@ns.route('/anonymize')
class Anonymizer(Resource):
    @ns.expect(input)
    def post(self):
        """
        Anonymize PI data.
        """
        json_data = request.json
        output = nltk_ner_parser.anonymize(json_data["data"])
        output = phone_parser.anonymize(output)
        output = email_parser.anonymize(output)
        return {"data": output}

@ns.route('/anonymize/name')
class Anonymizer(Resource):
    @ns.expect(input)
    def post(self):
        """
        Anonymize PI data.
        """
        json_data = request.json
        output = nltk_ner_parser.anonymize(json_data["data"])
        return {"data": output}

@ns.route('/anonymize/phone')
class PhoneAnonymizer(Resource):
    @ns.expect(input)
    def post(self):
        """
        Anonymize PI data.
        """
        json_data = request.json
        output = phone_parser.anonymize(json_data["data"])
        return {"data": output}

@ns.route('/anonymize/email')
class EmailAnonymizer(Resource):
    @ns.expect(input)
    def post(self):
        """
        Anonymize PI data.
        """
        json_data = request.json
        output = email_parser.anonymize(json_data["data"])
        return {"data": output}