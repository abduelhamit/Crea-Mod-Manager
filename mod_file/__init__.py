#!/usr/bin/python
# -*- coding: utf-8 -*-

from lxml import etree, objectify

from helper import process_command


def load_info(path):
    with open("info.xsd") as f:
        schema = etree.XMLSchema(file=f)
    parser = objectify.makeparser(schema=schema)
    xml = process_command(u"7za e -so {} info.xml".format(path))
    if not xml:
        xml = process_command(u"tools/7za e -so {} info.xml".format(path))
    cmf = objectify.fromstring(xml, parser)
    return cmf
