# coding=utf-8

'''The Info class.
Every interaction with an info.xml file happens over a Info object.'''

from lxml import etree, objectify


class Info:
    '''The Info class.'''
    def __init__(self):
        with open("cmm/core/info.xsd") as schema_file:
            schema = etree.XMLSchema(file=schema_file)
        objectify.set_default_parser(objectify.makeparser(schema=schema))

        self.xml = objectify.Element("cmf", attrib={"version": "0"})

    def parse_string(self, xml):
        '''Parse a string.'''
        self.xml = objectify.fromstring(xml)

    def parse_file(self, xml):
        '''Parse a file or file-like object.'''
        self.xml = objectify.parse(xml)
