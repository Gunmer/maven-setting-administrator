from os.path import expanduser

user_home_path = expanduser("~") + '/'
m2_path = user_home_path + '.m2/'

msa_version = '1.0.2'

msa_path = m2_path + 'msa/'
database_path = msa_path + 'msa.db'

log_debug_enable = False
