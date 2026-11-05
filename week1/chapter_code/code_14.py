class MonitorConfig:
	def __init__(self,interval: float=0.5):
		if not 0 < interval <=10:
			raise ValueError("interval out of range")
		self.interval=interval
	def describe(self) -> str:
		return f"sample interval:{self.interval}s"

config = MonitorConfig(1.0)
print(config.describe())
