import csvutil as csv
import copy

class DatasetManager:
	def __init__(self, inpath='', outpath=''):
		self.inpath = inpath
		self.outpath = outpath
		self.headerRemoved = False

	@classmethod
	def from_dataset(self, dataset):
		dm = DatasetManager()
		dm.dataset = dataset
		return dm

	@classmethod
	def from_dm(self, dm):
		return copy.deepcopy(dm)

	def load(self):
		self.dataset = csv.read(self.inpath)
		self.originaldataset = list(self.dataset)
		return self

	def save(self):
		csv.write(self.dataset, self.outpath)

	def restore(self):
		self.dataset = list(self.originaldataset)

	def remove_header(self):
		if not self.headerRemoved:
			self.header = self.dataset.pop(0)
			self.headerRemoved = True

	def restore_header(self):
		if self.headerRemoved:
			self.dataset.insert(0, self.header)

	def remove_row_by_index(self, row):
		del self.dataset[row]

	def remove_rows_by_index(self, rows):
		for row in reversed(xrange(len(self.dataset))):
			if row in rows:
				self.remove_row_by_index(row)

	def remove_col_by_name(self, col):
		self.remove_cols_by_name([col])

	def remove_cols_by_name(self, cols):
		inds = []
		for col in cols:
			inds.append(self.dataset[0].index(col))
		self.remove_cols_by_index(inds)

	def remove_col_by_index(self, col):
		self.remove_cols_by_index([col])

	def remove_cols_by_index(self, cols):
		for col in reversed(sorted(cols)):
			for row in xrange(len(self.dataset)):
				del self.dataset[row][col]

	def append_col(self, col):
		self.add_col(len(self.dataset[0]), col)

	def add_col(self, ind, col):
		for i in xrange(len(self.dataset)):
			self.dataset[i].insert(ind, col[i])

	def get_col(self, ind):
		return [x[ind] for x in self.dataset]