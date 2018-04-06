#!/usr/bin/python
#-*-coding:utf-8-*-

import time
import zmq  
import pmt
import sys
import threading
from grc.gr_ble import gr_ble as gr_block
from datetime import datetime, timedelta

gr_buffer = ''
data_channel = 0
#------------------------------------------------------
# 一个线程，只负责跳频
# ----------------------------------------------------- 
def for_hop(hop, setup_time, hopping_time,chM):
	global data_channel
	while 1:
		if datetime.now() >= hopping_time:
			data_channel = (data_channel + hop)% 37
			channel_to(data_channel)
			hopping_time = hopping_time + timedelta(milliseconds=setup_time)
			
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



#-------------------------------------------------------
#从广播信道或者数据信道向物理射频信道的转变
#-------------------------------------------------------
def to_rf_channel(channel):
	channel_list = [37,0,1,2,3,4,5,6,7,8,9,10,38,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,39]
	print channel_list.index(channel)
	return channel_list.index(channel)
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

def channel_to(channel):
	gr_block.set_dv_channel(channel)
	gr_block.set_rf_channel(to_rf_channel(channel))


if __name__ == '__main__':

	context = zmq.Context()  
	socket = context.socket(zmq.SUB)  
	socket.connect("tcp://127.0.0.1:23333")  
	socket.setsockopt(zmq.SUBSCRIBE,'')
	'''
	#------------------------------------------------------
	#启动打印线程
	#------------------------------------------------------
	t1 = threading.Thread(target=for_print,args=())
	t1.setDaemon(True)
	t1.start() 
	'''
	#------------------------------------------------------	
	#启动流图部分
	#------------------------------------------------------
	gr_block = gr_block()
	
	gr_block.start()
	channel_to(38)
	print gr_block.get_freq()
	print gr_block.get_dv_channel()
	
	while 1:
		first_time = datetime.now()
		print first_time
		gr_buffer = socket.recv()[10:]
		print gr_buffer
		#print socket.recv()
		if(gr_buffer[:4]=="1010" and len(gr_buffer)>290):
			'''
			[0:16]head [16:64]initAddr [64:112]advaddr [112:144]Access Address [144:168]CRCinit [168:176]winsize
			[176:192]winoffset [192:208]interval [208:224]latency [224:240]timeout [240:280]chM [280:285]hop
			[285:288]SCA
			'''
			#global data_channel
			#----------------------------------------------------
			#跳频线程的一些准备
			#----------------------------------------------------
			
			Accessaddr =   int(hex(int(gr_buffer[112:144][::-1],2))[:-1][2:],16)
			WinOffset =    int(gr_buffer[176:192][::-1],2)
			WinSize =      int(gr_buffer[168:176][::-1],2)
			Hop =          int(gr_buffer[280:285][::-1],2)
			connInterval = int(gr_buffer[192:208][::-1],2)
			chM =          list(gr_buffer[240:280])
			
			gr_block.set_accaddr(Accessaddr)
			setup_time = 1.25*connInterval
			hopping_time = first_time + timedelta(milliseconds=connInterval) + timedelta(milliseconds=WinOffset) + timedelta(milliseconds=1.25)
			#----------------------------------------------------
			#完成第一跳
			#----------------------------------------------------
			data_channel = Hop
			channel_to(data_channel)
			#----------------------------------------------------
			#跳频线程开启
			#----------------------------------------------------
			t2 = threading.Thread(target=for_hop,args=(Hop, setup_time, hopping_time, chM))
			t2.setDaemon(True)
			t2.start()
			print "Now start hop"
			print "**************************************************************************"
			print "**************************************************************************"
			print "**************************************************************************"

