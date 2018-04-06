#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2017 <+YOU OR YOUR COMPANY+>.
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
import pmt
from bitstring import BitArray
import array

class pack_bin_to_byte(gr.sync_block):
	"""
	docstring for block pack_bin_to_byte
	"""
	def __init__(self, fill):
		gr.sync_block.__init__(self,
			name="pack_bin_to_byte",
			in_sig=None,
			out_sig=None)

		self.fill = fill
		self.message_port_register_in(pmt.intern('in'))
		self.set_msg_handler(pmt.intern('in'), self.handle_msg)
		self.message_port_register_out(pmt.intern('out'))

	def to_send(self ,s):
	#make str bits to bytes
		data_in_bit = BitArray(bin=s)
		print s
		after_dewhite_bin = data_in_bit.tobytes()
		after_dewhite_str = array.array( "B",(after_dewhite_bin))
		self.message_port_pub(pmt.intern('out'), pmt.cons(pmt.PMT_NIL, pmt.init_u8vector(len(after_dewhite_bin), bytearray(after_dewhite_bin))))
	

	def handle_msg(self, msg_pmt):
		s = ''
		a = ''
		#---------------------------------------------------------------------------
		msg = pmt.cdr(msg_pmt)
		if not pmt.is_u8vector(msg):
			print "[ERROR] Received invalid message type. Expected u8vector"
			return

		data = pmt.u8vector_elements(msg)
		#---------------------------------------------------------------------------
		for _ in data:
			if _ == 49L:  #asic2 1
				s = s+'1'
			else:     #asic2 0
				s = s+'0'
	
		if (self.fill == 0):  #how many bits 
			self.to_send(s)
		else:
			for _ in s:
				a=a + '0' * (self.fill-1) + _
			self.to_send(a)	
	











