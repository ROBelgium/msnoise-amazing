import click

@click.group()
def amazing():
    """Example Amazing Plugin for MSNoise"""
    pass

@click.command()
def sayhi():
    """A Very Polite Command"""
    print("Hi")

@click.command()
def compute():
    """Compute an Amazing Value"""
    from .compute import main
    main()

@click.command()
def install():
    """ Create the Config table"""
    from .install import main
    main()


amazing.add_command(sayhi)
amazing.add_command(compute)
amazing.add_command(install)


def register_job_types():
    jobtypes = []
    jobtypes.append( {"name":"AMAZ1", "after":"new_files"} )
    return jobtypes


from flask.ext.admin.contrib.sqla import ModelView
from .amazing_table_def import AmazingConfig


class AmazingConfigView(ModelView):
    # Disable model creation
    view_title = "MSNoise Amazing Configuration"
    name = "Configuration"

    can_create = False
    can_delete = False
    page_size = 50
    # Override displayed fields
    column_list = ('name', 'value')

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(AmazingConfigView, self).__init__(AmazingConfig, session,
                                                endpoint="amazingconfig",
                                                name="Amazing Config",
                                                category="Configuration", **kwargs)