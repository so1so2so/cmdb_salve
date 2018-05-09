#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# from .plugins.disk import DiskPlugin
# from .plugins.mem import MemPlugin
# from .plugins.nic import NicPlugin
from conf import settings
import src.plugins.mem


def pack():
    response = {}

    for k, v in settings.PLUGINS.items():
        # v = 'src.plugins.disk.DiskPlugin'
        # 反射
        print  v
        # v=src.plugins.disk.DiskPlugin
        import importlib
        m_path, class_name = v.rsplit('.',1)
        # m=importlib.import_module('src.plugins.disk')
        m = importlib.import_module(m_path)
        # m2=__import__('src.plugins.disk')
        # print m2
        cls = getattr(m, class_name)
        # cls=getattr(m,'DiskPlugin')
        # cls2=getattr(m2,'DiskPlugin')
        # print cls
        response[k] = cls().execute()
    # print response
    return response


pack()
