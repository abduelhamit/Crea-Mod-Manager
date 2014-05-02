#!/usr/bin/python
# -*- coding: utf-8 -*-

from lxml import etree, objectify

from helper import process_command


def load_info(path):
    with open("info.xsd") as open_file:
        schema = etree.XMLSchema(file=open_file)
    parser = objectify.makeparser(schema=schema)
    xml = process_command(u"7za e -so {} info.xml".format(path))
    if not xml:
        xml = process_command(u"tools/7za e -so {} info.xml".format(path))
    cmf = objectify.fromstring(xml, parser)
    return cmf


def parse_info(path):
    mod = load_info(path)
    display_text = []
    display_text += mod.name.text
    display_text += " (" + mod.version.get("format").format(
        *mod.version.getchildren()) + ")"
    display_text += " by " + mod.author.text
    display_text += "\n\n" + mod.shortDesc.text
    display_text += "\n\n" + mod.homepage.text
    display_text += "\n\n----------------------------------------"
    display_text += "---------------------------------------"
    display_text += "\n\n" + mod.desc.text
    display_text += "\n\n----------------------------------------"
    display_text += "---------------------------------------"
    display_text += "\n\nChangelog:"
    for entry in mod.changelog.entry:
        display_text += "\n\n{} ({}):\n{}".format(
            entry.get("version"), entry.get("date"), entry.text)
    display_text += "\n\n----------------------------------------"
    display_text += "---------------------------------------"
    display_text += "\n\nAdds:"
    try:
        for add in mod.files.add:
            display_text += "\n" + add.text
    except TypeError:
        display_text += "\nnothing"
    display_text += "\n\nModifies:"
    try:
        for modify in mod.files.modify:
            display_text += "\n" + modify.text
    except TypeError:
        display_text += "\nnothing"
    display_text += "\n\nReplaces:"
    try:
        for replace in mod.files.replace:
            display_text += "\n" + replace.text
    except TypeError:
        display_text += "\nnothing"
    return "".join(display_text)
