#%%
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
	'robot'	: '/home/mrodriguez/renamevids/tvseries/Mr.Robot'	
}

def get_immediate_subdirectories(path):
    subdirs = []
    for item in os.walk(path):
        subdirs.append((item[0], item[2]))
    return subdirs

def get_immediate_files(_path):
    return [name for name in os.listdir(path)
            if os.path.isfile(os.path.join(_path, name))]

def process_directory(directory):
    print('Found directory: ', directory)
    series = find_series(directory)
    if series:
        process(directory, series)
    else:    
        print('No match found for', directory)
        
def find_series(directory):
    ldirectory = directory[0].lower()
    for series in seriesmap.items():
         if series[0] in ldirectory:
             return series
	
    return ''
        
def process(source_dir, series):
    print('Processing:', source_dir)
    for file in get_immediate_files(source_dir):
        print('File found:', file)

def main():
    for directory in get_immediate_subdirectories(path):
        process_directory(directory)
        print()
	
if __name__ == '__main__':
    main()

