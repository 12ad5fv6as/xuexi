from contextlib import contextmanager

@contextmanager
def experiment(name):
	print("begin:", name)
	try:
		yield
	finally:
		print("end:", name)

with experiment("sample"):
	print("collecting")
