class Time(object):
	"""SRM 144 div2"""
	def __init__(self):
		super(Time, self).__init__()
	
	def whatTime(self,time):
		hour=time/3600
		time = time-(3600*hour)
		minute=time/60
		time = time-(60*minute)
		seconds=time
		
		
		
		return str(hour)+":"+str(minute)+":"+str(seconds)

if __name__ == '__main__':
	time=Time()
	print time.whatTime(5436)		