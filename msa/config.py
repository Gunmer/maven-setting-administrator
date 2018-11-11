from pathlib import Path

user_home_path = str(Path.home()) + '/'
# user_home_path = '/tmp/'
m2_path = user_home_path + '.m2/'

msa_path = m2_path + 'msa/'
database_path = msa_path + 'msa.db'

log_debug_enable = False
