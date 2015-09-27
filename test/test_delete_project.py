__author__ = '1'

# -*- coding: utf-8 -*-
from model.group import Group


def test_add_project(app, db, json_groups, check_ui):
    current_group = json_groups
    old_groups = db.get_group_list()
    app.group.create(current_group)
    new_groups = db.get_group_list()
    old_groups.append(current_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key = Group.id_or_max) == sorted(app.group.get_group_list(), key = Group.id_or_max)
