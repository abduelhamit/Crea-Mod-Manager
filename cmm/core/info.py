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
        '''
        Return the XML representation of this Info object as a string.
        Raises DocumentInvalid if the XML representation of this Info object is not valid.
        '''
        objectify.deannotate(self.xml, cleanup_namespaces=True)
        Info.schema.assertValid(self.xml)
        return etree.tostring(
            self.xml, encoding="UTF-8", xml_declaration=True,
            pretty_print=True)

    def get_homepage(self):
        '''Return the homepage URL.'''
        try:
            return self.xml.homepage.text
        except AttributeError:
            return None

    def set_homepage(self, url):
        '''Set the homepage URL.'''
        self.xml.homepage = url

    def del_homepage(self):
        '''Delete the homepage URL.'''
        del self.xml.homepage

    homepage = property(get_homepage, set_homepage, del_homepage)

    def get_update_link(self):
        '''Return the update URL.'''
        try:
            return self.xml.updateLink.text
        except AttributeError:
            return None

    def set_update_link(self, url):
        '''Set the update URL.'''
        self.xml.updateLink = url

    def del_update_link(self):
        '''Delete the update URL.'''
        del self.xml.updateLink

    update_link = property(get_update_link, set_update_link, del_update_link)
