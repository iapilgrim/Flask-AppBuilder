from wtforms.widgets import HTMLString, html_params
from flask.ext.wtf import fields, widgets, TextField


class DatePickerWidget(object):
    """
    Date Time picker from Eonasdan GitHub

    """
    data_template = ('<div class="input-group date appbuilder_date" id="datepicker">'
                    '<span class="input-group-addon"><i class="fa fa-calendar"></i>'
                    '</span>'
                    '<input class="form-control" data-format="yyyy-MM-dd" %(text)s/>'
                    '</div>'
                    )

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('name', field.name)
        if not field.data:
            field.data = ""
        template = self.data_template

        return HTMLString(template % {'text': html_params(type='text',
                                      value=field.data,
                                      **kwargs)
                                      })


class DateTimePickerWidget(object):
    """
    Date Time picker from Eonasdan GitHub

    """
    data_template = ('<div class="input-group date appbuilder_datetime" id="datetimepicker">'
                    '<span class="input-group-addon"><i class="fa fa-calendar"></i>'
                    '</span>'
                    '<input class="form-control" data-format="yyyy-MM-dd hh:mm:ss" %(text)s/>'
        '</div>'
        )

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('name', field.name)
        if not field.data:
            field.data = ""
        template = self.data_template

        return HTMLString(template % {'text': html_params(type='text',
                                        value=field.data,
                                        **kwargs)
                                })




class BS3TextFieldWidget(widgets.TextInput):
    def __call__(self, field, **kwargs):
        kwargs['class'] = u'form-control'
        if field.label:
            kwargs['placeholder'] = field.label.text
        if 'name_' in kwargs:
            field.name = kwargs['name_']
        return super(BS3TextFieldWidget, self).__call__(field, **kwargs)

class BS3TextAreaFieldWidget(widgets.TextArea):
    def __call__(self, field, **kwargs):
        kwargs['class'] = u'form-control'
        kwargs['rows'] = 3
        if field.label:
            kwargs['placeholder'] = field.label.text
        return super(BS3TextAreaFieldWidget, self).__call__(field, **kwargs)

class BS3PasswordFieldWidget(widgets.PasswordInput):
    def __call__(self, field, **kwargs):
        kwargs['class'] = u'form-control'
        if field.label:
            kwargs['placeholder'] = field.label.text
        return super(BS3PasswordFieldWidget, self).__call__(field, **kwargs)


class Select2Widget(widgets.Select):
    def __call__(self, field, **kwargs):
        kwargs['class'] = u'my_select2'
        kwargs['style'] = u'width:250px'
        kwargs['data-placeholder'] = u'Select Value'
        if 'name_' in kwargs:
            field.name = kwargs['name_']
        return super(Select2Widget, self).__call__(field, **kwargs)

class Select2ManyWidget(widgets.Select):
    def __call__(self, field, **kwargs):
        kwargs['class'] = u'my_select2'
        kwargs['style'] = u'width:250px'
        kwargs['data-placeholder'] = u'Select Value'
        kwargs['multiple'] = u'true'
        if 'name_' in kwargs:
            field.name = kwargs['name_']
        return super(Select2ManyWidget, self).__call__(field, **kwargs)
