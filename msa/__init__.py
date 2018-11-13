from msa import file_manager, repository

if file_manager.init():
    repository.init()

if repository.find_one('default') is None:
    repository.create('default', '')
