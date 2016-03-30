from ..models import Service


class ServicesHelper:
    service_tree = []

    def __init__(self, service_tree):
        self.service_tree = service_tree

    def html(self, tree):
        temp = ServiceHelper(tree[0])
        if tree[1].__len__() == 0:
            return "<li>%s</li>" % temp
        else:
            temp = "<ul>%s" % temp
        for node in tree[1]:
            temp += self.html(node)
        return temp + "</ul>"

    def __str__(self):
        return self.html(self.service_tree)


class ServiceHelper:
    service = Service()

    def __init__(self, service):
        self.service = service

    def __str__(self):
        temp = '<div class = "service_input">'
        temp += '<h3>%s</h3>' % self.service.title
        temp += '<p>%s</p>' % self.service.description
        temp += '<input type = "hidden" name = "service_ids" value=%d />' % self.service.id
        temp += '<input type = "checkbox" id = "service_checkboxes_%d" name = "service_checkboxes_%d" /><label for=\
        "service_checkboxes_%d" ></label>' % (self.service.id, self.service.id, self.service.id)
        temp += '<input type = "text" name = "service_descriptions" placeholder="توضیحات" />'
        temp += '<input type = "number" name = "service_counts" />'
        temp += '</div>'
        return temp
