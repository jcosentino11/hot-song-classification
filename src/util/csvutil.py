import csv
import os

HEADER = ["analysis_sample_rate", "audio_md5", "danceability", "duration", "end_of_fade_in", "energy", "idx_bars_confidence", "idx_bars_start", "idx_beats_confidence", "idx_beats_start", "idx_sections_confidence", "idx_sections_start", "idx_segments_confidence", "idx_segments_loudness_max", "idx_segments_loudness_max_time", "idx_segments_loudness_start", "idx_segments_pitches", "idx_segments_start", "idx_segments_timbre", "idx_tatums_confidence", "idx_tatums_start", "key", "key_confidence", "loudness", "mode", "mode_confidence", "start_of_fade_out", "tempo", "time_signature", "time_signature_confidence", "track_id", "analyzer_version", "artist_7digitalid", "artist_familiarity", "artist_hotttnesss", "artist_id", "artist_latitude", "artist_location", "artist_longitude", "artist_mbid", "artist_name", "artist_playmeid", "genre", "idx_artist_terms", "idx_similar_artists", "release", "release_7digitalid", "song_hotttnesss", "song_id", "title", "track_7digitalid"]

def append_header(dataset):
	dataset.insert(0, HEADER)

def write(dataset, path):
	with open(path, 'w') as f:
		writer = csv.writer(f, delimiter=',', quotechar='\'', quoting=csv.QUOTE_NONNUMERIC)
		for row in dataset:
			writer.writerow(row)

def read(path):
	dataset = []
	with open(path, 'r') as f:
		reader = csv.reader(f, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
		for row in reader:
			for i in xrange(len(row)):
				if isInt(row[i]):
					row[i] = int(row[i])
				elif isFloat(row[i]):
					row[i] = float(row[i])
			dataset.append(row)
	return dataset

def isInt(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

def isFloat(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

def remove_cols(cols, dataset):
	for col in reversed(xrange(len(dataset[0]))):
		if dataset[0][col] in cols:
			for row in xrange(len(dataset)):
				del dataset[row][col]
	return dataset