from msa import file_manager, repository
from msa.setting import Setting

if file_manager.init():
    print(' - Creating directory ...')
    repository.init()
    print(' - Creating database ...')

if repository.find_one('default') is None:
    print(' - Adding default settings ...')
    repository.create(Setting('default', ''))
