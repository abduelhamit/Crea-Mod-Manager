#!/usr/bin/python
# -*- coding: utf-8 -*-

class ModManager:
	def __init__(self):
        # keep data of one mod loaded
		self.current_mod = None
		# names of installed mods
        self.installed_mods = []
        # dict of {mod_name: mod_data};
        # self.current_mod may be in here but not installed
        self.installed_mods = {}
    
    def get_mod_name(self, mod = self.current_mod):
		return mod.name.text
	
	def is_mod_installed(self, mod = current_mod, installed_list = self.installed_mods):
        if mod is not None:
            return self.get_mod_name(mod) in installed_list
        return False

    def update_current_mod(self, mod_index, modify_index = lambda index: index):
        # retrieve the mod data using the mod name
        # modify the input if need be
        self.current_mod = self.installed_mods[
            modify_index(mod_index)
        ]
        
    def install(self, mod = self.current_mod):
		# if we haven't already installed the mod
        if not self.is_mod_installed(mod=mod):
            # install the mod
            # TODO: install
            # and add it to the record
            self.installed_mods[self.get_mod_name(mod)] = \
                self.current_mod
    
    def uninstall(self, mod = self.current_mod):
		if self.is_mod_installed(mod=mod):
			# uninstall the mod
			# TODO: uninstall
			# and remove it from the record
			del self.installed_mods[self.get_mod_name(mod)]
