class Solution:
	def validUtf8(self, data: List[int]) -> bool:
		index = 0
		state = 0 #this is for state-machine
		count = 0 #this is counter for checking 10-start data
		
		while index<len(data):
			match(state):
				case 0: #state-0 check leading byte
					if data[index]>>3==0x1E: #if data start with 11110
						count = 3
						state = 1
						index+=1
					elif data[index]>>4==0x0E: #if data start with 1110
						count = 2
						state = 1
						index+=1
					elif data[index]>>5==0x06: #if data start with 110
						count = 1
						state = 1
						index+=1
					elif data[index]>>7==0x00: #if data start with 0
						index+=1 #no need to go to state-1 since there is no 10-start byte followed by
					else:
						return False #data invalid
				
				case 1: #state-1 check 10-start byte
					if data[index]>>6==0x02:
						count-=1
						if count==0:
							state = 0 #there is no 10-start byte followed by, go back to state-0
						index+=1
					else:
						return False
		
		#data runs out
		if state==0:
			return True #if state back to 0, means data is complete
		return False