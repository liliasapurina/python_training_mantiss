__author__ = '1'

from model.project import Project
from random import randrange

def test_delete_some_project(app):
    app.session.login("administrator","root")
    old_projects = app.project.get_project_list()
    if app.project.count() == 0:
        app.project.create(Project(name="My project",description="My project description"))
    old_projects = app.project.get_project_list()
    index = 1
    while (index == 1 | index == 2):
        index = randrange(len(old_projects))
    app.project.delete_project_by_index(index)
    assert len(old_projects) - 1 == app.project.count()

