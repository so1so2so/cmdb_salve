#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from .base import BasePlugin


class DiskPlugin(BasePlugin):
    def windows(self):
        output = self.shell_cmd('ipconfig')
        return output

    def linux(self):
        output = self.shell_cmd('ifconfig')
        return output
