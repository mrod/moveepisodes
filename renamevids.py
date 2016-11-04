import os

""" 
Scans subdirectories containing tv episodes, identifies them and move them to their
defined destination folder, using a simple renaming.
Usage: 
python renamevids.py
"""

path = '/home/mrodriguez/renamevids/downloads'

seriesmap = {
	'walking' : '/home/mrodriguez/renamevids/tvseries/The.Walking.Dead',
	'robot'	  : '/home/mrodriguez/renamevids/tvseries/Mr.Robot'	
}

def get_immediate_subdirectories(_path):
    return [name for name in os.listdir(_path)
            if os.path.isdir(os.path.join(_path, name))]

def process_directory(directory):
	print('Processing "' + directory + '" ...')
	ldirectory = directory.lower()

	found = False
	
	for key, value in seriesmap.iteritems():
		if key in ldirectory:
			print 'Match: ' + value
			found = True
			break;

	if not found:
		print 'No match found for ' + directory			

for directory in get_immediate_subdirectories(path):
	process_directory(directory)
	print('\n')
	


    