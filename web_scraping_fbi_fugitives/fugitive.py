class Fugitive:
	def __init__(self, l_name, f_name, m_name, url, dob=None, pob=None, hair=None, eyes=None, height=None, weight=None, sex=None, race=None,
					nationality=None, scars=None, ncic=None, reward=None, remarks=None, caution=None):
		self.l_name=l_name
		self.f_name=f_name
		self.m_name=m_name
		self.url=url
		self.dob=dob
		self.pob=pob
		self.hair=hair
		self.eyes=eyes
		self.height=height
		self.weight=weight
		self.sex=sex
		self.race=race
		self.nationality=nationality
		self.scars=scars
		self.ncic=ncic
		self.reward=reward
		self.remarks=remarks
		self.caution=caution


	def __str__(self):
		return f'Name: {self.name} URL: {self.url}'

	__repr__=__str__
