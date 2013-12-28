class BinaryCode(object):
	"""Solution for srm 144 div1 of topCoder"""
	def __init__(self):
		super(BinaryCode, self).__init__()
		
	def decode(self, message):
		"""
		message : A string in the format "123210122"
		"""
		allowed = [0,1]
		output=()
		
		#iterate the input
		for num,strNum in enumerate(allowed):
			# if 'p' has been declared earlier,save it
			if 'p' in locals() and (output != "NONE"):
				#convert everything to string
				prevP=""
				for tmp in p:
					prevP = prevP + str(tmp)

				output = prevP

			p = [num]
			for idx,val in enumerate(message):
				if(idx==0):
					p.append(int(message[idx]) - p[idx])
				else:
					p.append(int(message[idx]) - p[idx] - p[idx-1])
				# check for invalid values
				if(p[idx+1] not in allowed):
					if(len(output)>0):
						output = str(output),("NONE")
					else:
						output = ("NONE")
					break
				#end of decoding	
				if(idx == (len(message)-2)):
					#check the consistency of the work
					if(int(message[idx+1]) == (p[idx]+p[idx+1])):
						#convert everything to string
						prevP=""
						for tmp in p:
							prevP = prevP + str(tmp)
					#else the answer is wrong
					else:
						prevP="NONE"
					#save the answer
					if(len(output)>0):
						output = str(output),prevP
					else:
						output = prevP	
					# output = str(output),
					break
		return output

if __name__ == '__main__':

	for message in ["123210122","11","22111","123210120","3","12221112222221112221111111112221111"]:
	# for message in ["123210120"]:

		bc = BinaryCode()
		print message+"-->"+str(bc.decode(message))
			