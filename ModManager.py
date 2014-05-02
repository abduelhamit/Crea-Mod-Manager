#!/usr/bin/python
# -*- coding: utf-8 -*-

from mod_file import load_info

class ModManager:
    def __init__(self):
        # keep data of one mod loaded
        self.current_mod = None
        # names of installed mods
        self.installed_mods = []
        # dict of {mod_name: mod_data};
        # self.current_mod may be in here but not installed
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
