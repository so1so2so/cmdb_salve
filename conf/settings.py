#!/usr/bin/env python
# _*_ coding:utf-8 _*_
MODE = "Agent" # Salt,SSH

PLUGINS = {
    'disk': 'src.plugins.disk.DiskPlugin',
    'mem': 'src.plugins.mem.MemPlugin',
    'nic': 'src.plugins.nic.NicPlugin',
}
