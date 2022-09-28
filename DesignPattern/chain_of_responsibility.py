# -*- coding: UTF-8 -*-
# created by Long on 2022/8/15 17:33
# @Software : PyCharm

from abc import ABCMeta, abstractmethod


class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self, day):
        pass


class GeneralManager(Handler):
    def handle_leave(self, day):
        if day <= 10:
            print("总经理准假%d天" % day)
        else:
            print("你还是辞职吧")


class DepartmentManager(Handler):
    def __init__(self):
        self.next = GeneralManager()

    def handle_leave(self, day):
        if day <= 5:
            print("部门经理准假%s天" % day)
        else:
            print("部门经理职权不足")
            self.next.handle_leave(day)


class ProjectDirector(Handler):
    def __init__(self):
        self.next = DepartmentManager()

    def handle_leave(self, day):
        if day <= 1:
            print("项目主管准假%d天" % day)
        else:
            print("项目主管职权不足")
            self.next.handle_leave(day)


day = 18
h = ProjectDirector()
h.handle_leave(day)