#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, os.path
from core.mod_file import load_info


class ModManager:
    def __init__(self):
        # the directory where .cmf files are stored
        self.mod_dir = 'mods'
        # the file where we save our list of installed mods
        self.mod_list_file = 'installed_mods.txt'
        # keep data of one mod loaded
        self.current_mod = None
        # dict of {mod_name: mod_data}
        self.installed_mods = {}

    def get_mod_name(self, mod=None):
        if mod is None:
            mod = self.current_mod
        return mod.name.text

    def is_mod_installed(self, mod=None, installed_list=None):
        if mod is None:
            mod = self.current_mod
        if installed_list is None:
            installed_list = self.installed_mods
        return self.get_mod_name(mod) in installed_list

    def update_current_mod(self, mod_name):
        # retrieve the mod data using the mod name
        self.current_mod = self.installed_mods[mod_name]

    def new_current_mod(self, path):
        """We just loaded a mod from the filesystem,
        so we have to load its data."""
        self.current_mod = load_info(path)

    def install(self, mod=None):
        if mod is None:
            mod = self.current_mod
        # if we haven't already installed the mod
        if not self.is_mod_installed(mod=mod):
            # install the mod
            # TODO: install
            # and add it to the record
            self.installed_mods[self.get_mod_name(mod)] = \
                self.current_mod

    def uninstall(self, mod=None):
        if mod is None:
            mod = self.current_mod
        if self.is_mod_installed(mod=mod):
            # uninstall the mod
            # TODO: uninstall
            # and remove it from the record
            del self.installed_mods[self.get_mod_name(mod)]

    def save_mod_list(self):
        with open(self.mod_list_file, 'wb') as f:
            f.writelines('\n'.join([mod_name for mod_name in
                self.installed_mods.keys()]))

    def load_mod_list(self):
        # mods in mod_list_file, { mod_name: mod_info }
        mods_to_load = { name.strip(): None for name in
            open(self.mod_list_file, 'rb').readlines() }
        
        for filename in os.listdir(self.mod_dir):
            try:
                # get the name of the mod from the file
                mod_info = load_info(os.path.join(self.mod_dir, filename))
                self.installed_mods[self.get_mod_name(mod_info)] = mod_info
            except (XMLSyntaxError) as error:
                if error.message:
                    message = error.message
                else:
                    message = "Unknown error"
