from pathlib import Path
import os
from shutil import copyfile

# for production
PATH = input("Full path where to create dirs(use forward salshes): ")
PATH = Path(PATH)
PROJ_NAME = input("Name of project: ")

# for testing
# PATH = r'Full path'
# PATH = Path(PATH)
#
# PROJ_NAME = 'loan_pred'


main_dirs = ['notebooks', PROJ_NAME, 'data', 'scripts']  # Name of the sub-directories


def create_dirs():
    # Create directories from main_dirs

    for dir in main_dirs:
        dir_name = PATH / PROJ_NAME / dir

        if dir == 'data':
            dir_name = dir_name / 'raw'

        else:
            pass

        try:
            # Create target Directory
            os.makedirs(dir_name)
            print("Directory ", dir_name, " Created ")
        except FileExistsError:
            print("Directory ", dir_name, " already exists")

create_dirs()


def copy_templates():
    # copies template files like README or config, etc. to dirs

    readme_src = Path('template_files/README.md')
    config_src = Path('template_files/config.py')
    custom_funcs_src = Path('template_files/custom_funcs.py')

    readme_dst = Path(PATH / PROJ_NAME / 'README.md')
    config_dst = Path(PATH / PROJ_NAME / PROJ_NAME / 'config.py')
    custom_funcs_dst = Path(PATH / PROJ_NAME / PROJ_NAME / 'custom_funcs.py')

    copyfile(readme_src, readme_dst)
    copyfile(config_src, config_dst)
    copyfile(custom_funcs_src, custom_funcs_dst)
    print('Template files created.')

copy_templates()
