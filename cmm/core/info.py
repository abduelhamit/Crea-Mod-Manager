# coding=utf-8

'''The Info class.
Every interaction with an info.xml file happens over a Info object.'''

from lxml import etree, objectify


class Info(object):
    '''The Info class.'''
    with open("cmm/core/info.xsd") as schema_file:
        schema = etree.XMLSchema(file=schema_file)
    objectify.set_default_parser(objectify.makeparser(schema=schema))

    def __init__(self):
        self.xml = objectify.Element("cmf", attrib={"version": "0"})

    def parse_string(self, xml):
        '''Parse a string.'''
        self.xml = objectify.fromstring(xml)

    def parse_file(self, xml):
        '''Parse a file or file-like object.'''
        self.xml = objectify.parse(xml).getroot()

    def to_string(self):
        '''Return the XML representation of this Info object as a string.
        Raises DocumentInvalid if the XML representation of this Info object is
        not valid.'''
        objectify.deannotate(self.xml, cleanup_namespaces=True)
        Info.schema.assertValid(self.xml)
        return etree.tostring(
            self.xml, encoding="UTF-8", xml_declaration=True,
            pretty_print=True)

    @property
    def homepage(self):
        '''Return the homepage URL.'''
        try:
            return self.xml.homepage.text
        except AttributeError:
            return None

    @homepage.setter
    def homepage(self, val):
        '''Set the homepage URL.'''
        self.xml.homepage = val

    @homepage.deleter
    def homepage(self):
        '''Delete the homepage URL.'''
        del self.xml.homepage

    @property
    def update_link(self):
        '''Return the update URL.'''
        try:
            return self.xml.updateLink.text
        except AttributeError:
            return None

    @update_link.setter
    def update_link(self, val):
        '''Set the update URL.'''
        self.xml.updateLink = val

    @update_link.deleter
    def update_link(self):
        '''Delete the update URL.'''
        del self.xml.updateLink

    @property
    def author(self):
        '''Return the author.'''
        try:
            return self.xml.author.text
        except AttributeError:
            return None

    @author.setter
    def author(self, val):
        '''Set the author.'''
        self.xml.author = val

    @author.deleter
    def author(self):
        '''Delete the author.'''
        del self.xml.author

    @property
    def version_string(self):
        '''Return the version as a string.'''
        try:
            version_format = self.xml.version.get("format")
        except AttributeError:
            return None
        version_values = (v.text for v in self.xml.version.v)
        return version_format.format(*version_values)
