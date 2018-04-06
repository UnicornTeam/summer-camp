#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2017 backahasten@360Unicorn Team.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr
import collections
import pmt
import array
import datetime

class BLE_CRC24(gr.sync_block):
	"""
	docstring for block BLE_CRC24
	"""
	def __init__(self, CRCinit):
		gr.sync_block.__init__(self,
			name="BLE_CRC24",
			in_sig=None,
			out_sig=None)
		crc_init = []
		
		self.CRCinit  = bin(eval('0x'+CRCinit))[2:].zfill(24)[::-1]		
		self.message_port_register_in(pmt.intern('in'))
		self.set_msg_handler(pmt.intern('in'), self.handle_msg)
		self.message_port_register_out(pmt.intern('out'))

	def handle_msg(self, msg_pmt):

		input_str = []
		output_str = ''
		#---------------------------------------------------------------------------------------------
		msg = pmt.cdr(msg_pmt)
		if not pmt.is_u8vector(msg):
			print "[ERROR] Received invalid message type. Expected u8vector"
			return

		data = list(pmt.u8vector_elements(msg))
		#print data
		for tmp in data:
			input_data = bin(tmp)[2:]
			input_str.append(input_data)
		output_str = "".join(input_str)
		#------------------------------------------------------------------------------------------------
		crc_bit=[]
		for i in range(24):
			crc_bit.append(int(self.CRCinit[i]))

		if self.CRCinit == '101010101010101010101010':
			length = int(input_data[8:14][::-1],2)*8 + 16
		else:
			length = int(input_data[8:13][::-1],2)*8 + 16

		if (length <= len(input_data)):


			for _ in range(length):
				k = crc_bit[23]^int(input_data[_])
				crc_bit[23] = crc_bit[22]
				crc_bit[22] = crc_bit[21]
				crc_bit[21] = crc_bit[20]
				crc_bit[20] = crc_bit[19]
				crc_bit[19] = crc_bit[18]
				crc_bit[18] = crc_bit[17]
				crc_bit[17] = crc_bit[16]
				crc_bit[16] = crc_bit[15]
				crc_bit[15] = crc_bit[14]
				crc_bit[14] = crc_bit[13]
				crc_bit[13] = crc_bit[12]
				crc_bit[12] = crc_bit[11]
				crc_bit[11] = crc_bit[10]
				crc_bit[10] = crc_bit[9]^k
				crc_bit[9] = crc_bit[8]^k
				crc_bit[8] = crc_bit[7]
				crc_bit[7] = crc_bit[6]
				crc_bit[6] = crc_bit[5]^k
				crc_bit[5] = crc_bit[4]
				crc_bit[4] = crc_bit[3]^k
				crc_bit[3] = crc_bit[2]^k
				crc_bit[2] = crc_bit[1]
				crc_bit[1] = crc_bit[0]^k
				crc_bit[0] = k
			crc_str = ''
			for a in crc_bit:
				crc_str = crc_str+str(a)
			#print crc_str
			#print data[::-1][:24]
			print crc_str == input_data[::-1][:24]















