import h5py
import numpy as np

def print_attrs(f):
	f.visititems(__hdf5_print_attrs)

def __print_attrs(name, obj):
	print(name)
	for key, val in obj.attrs.iteritems():
		print("    %s: %s" % (key, val))

def get_analysis_vals(f):
	d = f['analysis/songs']
	return list([item for item in d][0])

def get_metadata_vals(f):
	d = f['metadata/songs']
	return list([item for item in d][0])

# scrape all values from the file
def get_vals(f):
	return get_analysis_vals(f) + get_metadata_vals(f)

def read_file(filename):
	return h5py.File(filename, 'r')