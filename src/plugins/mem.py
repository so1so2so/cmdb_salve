#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from .base import BasePlugin


class MemPlugin(BasePlugin):
    def windows(self):
        output = self.shell_cmd('asdf')
        # 正则表达式
        return output

    def linux(self):
        output = self.shell_cmd('asdf')
        # 正则表达式
        return output
