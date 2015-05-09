#Usage: python clean_csv.py <infile> <outfile>

import os
import sys
sys.path.insert(0, '../util')
from dm import DatasetManager
import csvutil as csv
import math

# TODO make artist_id and track_id nominal
COLS_TO_REMOVE = ['artist_id','track_id','track_7digitalid', 'title', 'song_id', 'release', 'idx_similar_artists', 'idx_artist_terms', 'genre', 'artist_playmeid', 'artist_name', 'artist_mbid', 'artist_longitude', 'artist_location', 'artist_latitude', 'artist_7digitalid', 'analyzer_version', 'time_signature_confidence', 'mode_confidence', 'key_confidence', 'idx_tatums_start', 'idx_tatums_confidence', 'idx_segments_timbre', 'idx_segments_start', 'idx_segments_pitches', 'idx_segments_loudness_start', 'idx_segments_loudness_max_time', 'idx_segments_loudness_max', 'idx_segments_confidence', 'idx_sections_start', 'idx_sections_confidence', 'idx_beats_start', 'idx_beats_confidence', 'idx_bars_start', 'idx_bars_confidence', 'energy', 'danceability', 'audio_md5', 'analysis_sample_rate']

DATA_DIR = '../../data'

def find_rows_with_nan(dataset):
	rows = []
	for row in reversed(xrange(len(dataset))):
		for col in reversed(xrange(len(dataset[0]))):
			if csv.isFloat(dataset[row][col]) and math.isnan(dataset[row][col]):
				rows.append(row)
				break
	return rows

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print('Usage: python clean_csv.py <infile> <outfile>')
		sys.exit(1)

	inpath = os.path.join(DATA_DIR, sys.argv[1])
	outpath = os.path.join(DATA_DIR, sys.argv[2])

	dm = DatasetManager(inpath=inpath, outpath=outpath)
	dm.load()
	dm.remove_cols_by_name(COLS_TO_REMOVE)
	dm.remove_rows_by_index(find_rows_with_nan(dm.dataset))
	dm.save()