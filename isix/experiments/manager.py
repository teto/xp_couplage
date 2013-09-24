


# should be able to detect failed tests,
# propose the user to resume it or other options whenfacing a failure 
# sthg like try again or give up
class XPManager:

	def __init__(self, config, tests):
		self._tests = tests
		# TODO load config
		self._config = config

	# def run_tests():
