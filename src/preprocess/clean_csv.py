#Usage: python clean_csv.py <infile> <outfile>

import os
import sys
sys.path.insert(0, '../util')
import logger as lg
import csvutil as csv

COLS_TO_REMOVE = ['track_7digitalid', 'title', 'song_id', 'release', 'idx_similar_artists', 'idx_artist_terms', 'genre', 'artist_playmeid', 'artist_name', 'artist_mbid', 'artist_longitude', 'artist_location', 'artist_latitude', 'artist_7digitalid', 'analyzer_version', 'time_signature_confidence', 'mode_confidence', 'key_confidence', 'idx_tatums_start', 'idx_tatums_confidence', 'idx_segments_timbre', 'idx_segments_start', 'idx_segments_pitches', 'idx_segments_loudness_start', 'idx_segments_loudness_max_time', 'idx_segments_loudness_max', 'idx_segments_confidence', 'idx_sections_start', 'idx_sections_confidence', 'idx_beats_start', 'idx_beats_confidence', 'idx_bars_start', 'idx_bars_confidence', 'energy', 'danceability', 'audio_md5', 'analysis_sample_rate']

DATA_DIR = '../../data'

def remove_empty_cols(infile, outfile):
	dataset = csv.read(os.path.join(DATA_DIR, infile))
	csv.remove_cols(COLS_TO_REMOVE, dataset)
	csv.write(dataset, os.path.join(DATA_DIR, outfile))


if __name__ == '__main__':
	if len(sys.argv) != 3:
		lg.log(lg.E, 'Usage: python clean_csv.py <infile> <outfile>')
		sys.exit(1)

	remove_empty_cols(sys.argv[1], sys.argv[2])