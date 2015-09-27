__author__ = '1'
from model.project import Project
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata =[
    Project(name=random_string("name",10),description=random_string("footer",20))
    for i in range(1)
]

@pytest.mark.parametrize("current_project",testdata)
def test_add_project(app, current_project):
    app.session.login("administrator","root")
    old_projects = app.project.get_project_list()
    app.project.create(current_project)
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)

