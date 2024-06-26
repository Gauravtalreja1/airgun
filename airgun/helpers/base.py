class BaseEntityHelper:
    def __init__(self, entity):
        self._entity = entity

    @property
    def entity(self):
        """Returns the entity associated with this helper."""
        return self._entity

    def read_filled_view(
        self, navigation_name, navigation_kwargs=None, values=None, read_widget_names=None
    ):
        """Navigate to a form using 'navigation_name' and with parameters from 'navigation_kwargs',
        fill the form with values and then read values for widgets from 'read_widget_names' list if
        supplied otherwise read all widgets values.

        Usage::

            # In host entity: open create view, click host.reset_puppet_environment button and read
            # host.puppet_environment
            session.host.helper.read_filled_view(
                'New',
                values={'host.reset_puppet_environment': True},
                read_widget_names=['host.puppet_environment'],
            )

        """
        navigation_kwargs = navigation_kwargs or {}
        values = values or {}
        view = self.entity.navigate_to(self.entity, name=navigation_name, **navigation_kwargs)
        view.fill(values)
        return view.read(widget_names=read_widget_names)
