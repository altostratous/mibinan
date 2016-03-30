from ..models import Service


class ServicesHelper:
    service_tree = []

    def __init__(self, service_tree):
        self.service_tree = service_tree

    def html(self, tree):
        temp = "<ul>"
        for node in tree:
            if isinstance(node, dict):
                temp += '<ul>%s%s</ul>' % (list(node.keys())[0], self.html(list(node.values())[0]))
            else:
                temp += '<li>%s</li>' % ServiceHelper(node)
        temp += "</ul>"
        return temp

    def __str__(self):
        return self.html(self.service_tree)


class ServiceHelper:

    service = Service()

    def __init__(self, service):
        self.service = service

    def __str__(self):
        temp = '<div class = "service_input">'
        temp += '<span>%s</span>' % self.service.title
        temp += '<p>%s</p>' % self.service.description
        temp += '<input type = "checkbox" name = "service_checkboxes" />'
        temp += '<input type = "text" name = "service_descriptions" placeholder="توضیحات" />'
        temp += '<input type = "number" name = "service_counts" />'
        temp += '</div>'
        return temp
