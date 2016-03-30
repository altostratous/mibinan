from ..models import Service


class ServicesHelper:
    service_tree = []

    def __init__(self, service_tree):
        self.service_tree = service_tree

    def html(self, tree):
        temp = ServiceHelper(tree[0])
        if tree[1].__len__() == 0:
            temp = '<li class = "service_input">%s<div class="service_toggle_%d service_input">' % (temp, tree[0].id)
        else:
            temp = '<ul class = "service_input">%s<div class="service_toggle_%d service_input">' % (temp, tree[0].id)
        for node in tree[1]:
            temp += self.html(node)
        temp + "</div>"
        if tree[1].__len__() == 0:
            temp += '</li>'
        else:
            temp += '</ul>'
        return temp

    def __str__(self):
        return self.html(self.service_tree)


class ServiceHelper:
    service = Service()

    def __init__(self, service):
        self.service = service

    def __str__(self):
        temp = '<div>'
        choice_type = "radio"
        if self.service.is_multiple:
            choice_type = "checkbox"
        temp += '<input type = "%s" id = "service_checkboxes_%d" name = "service_checkboxes_%d" /><label for=\
        "service_checkboxes_%d" onclick="toggle(%d)" >%s</label>' % (choice_type, self.service.id, self.service.id,
                                                                     self.service.id, self.service.id,
                                                                     self.service.title)
        temp += '<div class="service_toggle_%d"><p>%s</p>' % (self.service.id, self.service.description)
        temp += '<input type = "hidden" name = "service_ids" value=%d />' % self.service.id
        temp += '<input type = "text" name = "service_descriptions" placeholder="توضیحات" />'
        count_type = "hidden"
        if self.service.is_countable:
            count_type = "number"
        temp += '<input type = "%s" name = "service_counts" value="1" /></div>' % count_type
        temp += '</div>'
        return temp
