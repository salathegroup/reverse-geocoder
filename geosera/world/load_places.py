import os
from django.contrib.gis.utils import LayerMapping
from geosera.models.place import Place 
from geosera.models.place import place_mapping


def load(fips, verbose=True):
	shp_path = 'data/tiger_place_2010/tl_2010_%s_place10.shp' % fips
	shp_file = os.path.abspath(os.path.join(os.path.dirname(__file__), shp_path))
	lm = LayerMapping(Place, shp_file, place_mapping, transform=True, encoding='latin-1')
	lm.save(strict=True, verbose=verbose)

def run():
	#fips_codes = ['01', '02', '04', '05', '06', '08', '09', '10', '11', '12', '13',  '15', '16', '17', '18', '19', '20', '21', '22', '23', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '60', '66','69', '72','78']
	#fips_codes = ['44', '45', '46', '47', '48', '49', '50', '51', '53', '54', '55', '56', '60', '66','69', '72','78']
	fips_codes = ['56', '60', '66','69', '72','78']

	for fips in fips_codes:
		load(fips)
