# coding=utf-8

'''The Info class.
Every interaction with an info.xml file happens over a Info object.'''

from lxml import etree, objectify


class Info:
    '''The Info class.'''
    def __init__(self):
        self.xml = None

        with open("cmm/core/info.xsd") as schema_file:
            schema = etree.XMLSchema(file=schema_file)
        self.parser = objectify.makeparser(schema=schema)

    def parse_string(self, xml):
        '''Parse a string.'''
        self.xml = objectify.fromstring(xml, self.parser)

    def parse_file(self, xml):
        '''Parse a file or file-like object.'''
        self.xml = objectify.parse(xml, self.parser)
