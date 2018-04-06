for k in range(0,40):
	channel = k
	channel_1 = bin(channel).replace('0b','')
	#print channel_1
	channel_2 = list(channel_1.zfill(6))
	#print channel_2
	pre = list(channel_2)
	#print pre
	pre.insert(0,'1')
	#print pre
	new_pre = []
	for n in pre:
  		new_pre.append(int(n))
	pre = new_pre
	out = []
	i = 0
	#print pre
	for i in range(360):
		out.append(pre[6])
		pre[6] = pre[5]
		pre[5] = pre[4]
		pre[4] = out[i]^pre[3]
		pre[3] = pre[2]
		pre[2] = pre[1]
		pre[1] = pre[0]
		pre[0] = out[i]
		
	
	print out
	print ','
	#print k

