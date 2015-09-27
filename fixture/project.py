__author__ = '1'
from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        # open manage page
        wd.find_element_by_xpath("//html/body/table[2]/tbody/tr/td[1]/a[7]").click()
        #find_element_by_xpath('//div/td[1]')
        # opem projects manage page
        wd.find_element_by_xpath("//html/body/div[2]/p/span[2]/a").click()

    def create(self, project):
        wd = self.app.wd
        # open "manage projects"
        self.open_projects_page()
        # press "create new project"
        wd.find_element_by_css_selector("body > table:nth-child(6) > tbody > tr:nth-child(1) > td > form > input.button-small").click()
        # fill project form
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)
        # submit group creation
        wd.find_element_by_css_selector("body > div:nth-child(6) > form > table > tbody > tr:nth-child(7) > td > input").click()

    def get_project_list(self):
        wd = self.app.wd
        self.open_projects_page()
        projects = []
        for element in wd.find_elements_by_xpath("/html/body/table[3]/tbody/tr"):
            # TODO
            text = element.text
            id = element.get_attribute("value")
            # TODO
            projects.append(Project(name=text,id=id))
        return projects

