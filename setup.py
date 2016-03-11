from setuptools import setup, find_packages

setup(
    name='msnoise_amazing',
    version='0.1a',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['msnoise',
                      'obspy'],
    entry_points = {
        'msnoise.plugins.commands': [
            'amazing = msnoise_amazing.plugin_definition:amazing',
            ],
        'msnoise.plugins.jobtypes': [
            'register = msnoise_amazing.plugin_definition:register_job_types',
            ],
        'msnoise.plugins.table_def': [
            'AmazingConfig = msnoise_amazing.amazing_table_def:AmazingConfig',
            ],
        'msnoise.plugins.admin_view': [
            'AmazingConfigView = msnoise_amazing.plugin_definition:AmazingConfigView',
            ],
        },
    author = "Thomas Lecocq & MSNoise dev team",
    author_email = "Thomas.Lecocq@seismology.be",
    description = "An example plugin",
    license = "EUPL-1.1",
    url = "http://www.msnoise.org",
    keywords="amazing seismology"
)