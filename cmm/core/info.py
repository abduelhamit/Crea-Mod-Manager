# coding=utf-8

'''The Info class.
Every interaction with an info.xml file happens over a Info object.'''

from lxml import etree, objectify


class Info(object):
    '''The Info class.'''
    def __init__(self):
        with open("cmm/core/info.xsd") as schema:
            objectify.set_default_parser(objectify.makeparser(
                schema=etree.XMLSchema(file=schema)))

        self.xml = objectify.Element("cmf", attrib={"version": "0"})

    def parse_string(self, xml):
        '''Parse a string.'''
        self.xml = objectify.fromstring(xml)

    def parse_file(self, xml):
        '''Parse a file or file-like object.'''
        self.xml = objectify.parse(xml).getroot()

    def to_string(self):
        '''Return the XML representation of this Info object as a string.'''
        objectify.deannotate(self.xml, cleanup_namespaces=True)
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

    homepage = property(get_homepage, set_homepage)

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
