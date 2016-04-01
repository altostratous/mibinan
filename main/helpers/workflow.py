from ..models import Workflow, WorkflowLog, StepMove, Step


class WorkflowHelper:
    order = None

    def __init__(self, order):
        self.order = order

    def html(self):
        temp = '<div class="workflow">'
        last_log = self.order.workflowlog_set.all().reverse()[0]
        current_step_id = last_log.step_move.into_step.id
        for step in self.order.get_workflow().step_set.all():
            if step.id == current_step_id:
                temp += '<a class="btn workflow_arrow btn-cancel"> < </a>'
            temp += '<a href="#" class="btn">%s</a>' % step.title
            if step.id == current_step_id:
                temp += '<a class="btn workflow_arrow btn-confirm"> > </a>'
        temp += '</div>'
        return temp

    def __str__(self):
        return self.html()
