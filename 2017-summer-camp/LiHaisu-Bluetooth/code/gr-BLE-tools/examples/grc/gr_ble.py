#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Bluetooth LE Receiver
# Author: backahasten
# Generated: Thu Aug 24 11:51:55 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import BLE_tools
import osmosdr
import time
import wx


class gr_ble(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Bluetooth LE Receiver")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.transition_width = transition_width = 300e3
        self.sample_rate = sample_rate = 4e6
        self.rf_channel = rf_channel = 0
        self.data_rate = data_rate = 1e6
        self.cutoff_freq = cutoff_freq = 850e3
        self.ble_channel_spacing = ble_channel_spacing = 2e6
        self.ble_base_freq = ble_base_freq = 2402e6
        self.squelch_threshold = squelch_threshold = -100
        self.rf_gain = rf_gain = 10
        self.lowpass_filter = lowpass_filter = firdes.low_pass(1, sample_rate, cutoff_freq, transition_width, firdes.WIN_HAMMING, 6.76)
        self.gmsk_sps = gmsk_sps = int(sample_rate / data_rate)
        self.gmsk_omega_limit = gmsk_omega_limit = 0.035
        self.gmsk_mu = gmsk_mu = 0.5
        self.gmsk_gain_mu = gmsk_gain_mu = 0.7
        self.freq_offset = freq_offset = 1e6
        self.freq = freq = ble_base_freq+(ble_channel_spacing * rf_channel)
        self.dv_channel = dv_channel = 37
        self.accaddr = accaddr = int("0x8E89BED6",16)

        ##################################################
        # Blocks
        ##################################################
        self.zeromq_pub_msg_sink_0 = zeromq.pub_msg_sink("tcp://*:23333", 0)
        _squelch_threshold_sizer = wx.BoxSizer(wx.VERTICAL)
        self._squelch_threshold_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_squelch_threshold_sizer,
        	value=self.squelch_threshold,
        	callback=self.set_squelch_threshold,
        	label='squelch_threshold',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._squelch_threshold_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_squelch_threshold_sizer,
        	value=self.squelch_threshold,
        	callback=self.set_squelch_threshold,
        	minimum=-100,
        	maximum=0,
        	num_steps=1,
        	style=wx.SL_VERTICAL,
        	cast=int,
        	proportion=1,
        )
        self.Add(_squelch_threshold_sizer)
        self.osmosdr_source = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_source.set_sample_rate(sample_rate)
        self.osmosdr_source.set_center_freq(freq+freq_offset, 0)
        self.osmosdr_source.set_freq_corr(0, 0)
        self.osmosdr_source.set_dc_offset_mode(2, 0)
        self.osmosdr_source.set_iq_balance_mode(0, 0)
        self.osmosdr_source.set_gain_mode(False, 0)
        self.osmosdr_source.set_gain(rf_gain, 0)
        self.osmosdr_source.set_if_gain(20, 0)
        self.osmosdr_source.set_bb_gain(20, 0)
        self.osmosdr_source.set_antenna("", 0)
        self.osmosdr_source.set_bandwidth(0, 0)
          
        self.freq_xlating_fir_filter_lp = filter.freq_xlating_fir_filter_ccc(1, (lowpass_filter), -freq_offset, sample_rate)
        self.digital_gfsk_demod_0 = digital.gfsk_demod(
        	samples_per_symbol=int(sample_rate/1e6),
        	sensitivity=(3.1415926 / 2) / (sample_rate/1e6),
        	gain_mu=0.175,
        	mu=0.5,
        	omega_relative_limit=0.005,
        	freq_error=0.0,
        	verbose=False,
        	log=False,
        )
        self.analog_simple_squelch = analog.simple_squelch_cc(-350, 0.1)
        self.BLE_tools_pack_bin_to_byte_0 = BLE_tools.pack_bin_to_byte(0)
        self.BLE_tools_find_pack_by_preamble_0 = BLE_tools.find_pack_by_preamble()
        self.BLE_tools_BLE_pack_collect_0 = BLE_tools.BLE_pack_collect(dv_channel, str(hex(accaddr))[2:])

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.BLE_tools_BLE_pack_collect_0, 'out'), (self.BLE_tools_pack_bin_to_byte_0, 'in'))    
        self.msg_connect((self.BLE_tools_find_pack_by_preamble_0, 'out'), (self.BLE_tools_BLE_pack_collect_0, 'in'))    
        self.msg_connect((self.BLE_tools_pack_bin_to_byte_0, 'out'), (self.zeromq_pub_msg_sink_0, 'in'))    
        self.connect((self.analog_simple_squelch, 0), (self.freq_xlating_fir_filter_lp, 0))    
        self.connect((self.digital_gfsk_demod_0, 0), (self.BLE_tools_find_pack_by_preamble_0, 0))    
        self.connect((self.freq_xlating_fir_filter_lp, 0), (self.digital_gfsk_demod_0, 0))    
        self.connect((self.osmosdr_source, 0), (self.analog_simple_squelch, 0))    

    def get_transition_width(self):
        return self.transition_width

    def set_transition_width(self, transition_width):
        self.transition_width = transition_width
        self.set_lowpass_filter(firdes.low_pass(1, self.sample_rate, self.cutoff_freq, self.transition_width, firdes.WIN_HAMMING, 6.76))

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self.osmosdr_source.set_sample_rate(self.sample_rate)
        self.set_lowpass_filter(firdes.low_pass(1, self.sample_rate, self.cutoff_freq, self.transition_width, firdes.WIN_HAMMING, 6.76))
        self.set_gmsk_sps(int(self.sample_rate / self.data_rate))

    def get_rf_channel(self):
        return self.rf_channel

    def set_rf_channel(self, rf_channel):
        self.rf_channel = rf_channel
        self.set_freq(self.ble_base_freq+(self.ble_channel_spacing * self.rf_channel))

    def get_data_rate(self):
        return self.data_rate

    def set_data_rate(self, data_rate):
        self.data_rate = data_rate
        self.set_gmsk_sps(int(self.sample_rate / self.data_rate))

    def get_cutoff_freq(self):
        return self.cutoff_freq

    def set_cutoff_freq(self, cutoff_freq):
        self.cutoff_freq = cutoff_freq
        self.set_lowpass_filter(firdes.low_pass(1, self.sample_rate, self.cutoff_freq, self.transition_width, firdes.WIN_HAMMING, 6.76))

    def get_ble_channel_spacing(self):
        return self.ble_channel_spacing

    def set_ble_channel_spacing(self, ble_channel_spacing):
        self.ble_channel_spacing = ble_channel_spacing
        self.set_freq(self.ble_base_freq+(self.ble_channel_spacing * self.rf_channel))

    def get_ble_base_freq(self):
        return self.ble_base_freq

    def set_ble_base_freq(self, ble_base_freq):
        self.ble_base_freq = ble_base_freq
        self.set_freq(self.ble_base_freq+(self.ble_channel_spacing * self.rf_channel))

    def get_squelch_threshold(self):
        return self.squelch_threshold

    def set_squelch_threshold(self, squelch_threshold):
        self.squelch_threshold = squelch_threshold
        self._squelch_threshold_slider.set_value(self.squelch_threshold)
        self._squelch_threshold_text_box.set_value(self.squelch_threshold)

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self.osmosdr_source.set_gain(self.rf_gain, 0)

    def get_lowpass_filter(self):
        return self.lowpass_filter

    def set_lowpass_filter(self, lowpass_filter):
        self.lowpass_filter = lowpass_filter
        self.freq_xlating_fir_filter_lp.set_taps((self.lowpass_filter))

    def get_gmsk_sps(self):
        return self.gmsk_sps

    def set_gmsk_sps(self, gmsk_sps):
        self.gmsk_sps = gmsk_sps

    def get_gmsk_omega_limit(self):
        return self.gmsk_omega_limit

    def set_gmsk_omega_limit(self, gmsk_omega_limit):
        self.gmsk_omega_limit = gmsk_omega_limit

    def get_gmsk_mu(self):
        return self.gmsk_mu

    def set_gmsk_mu(self, gmsk_mu):
        self.gmsk_mu = gmsk_mu

    def get_gmsk_gain_mu(self):
        return self.gmsk_gain_mu

    def set_gmsk_gain_mu(self, gmsk_gain_mu):
        self.gmsk_gain_mu = gmsk_gain_mu

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset
        self.freq_xlating_fir_filter_lp.set_center_freq(-self.freq_offset)
        self.osmosdr_source.set_center_freq(self.freq+self.freq_offset, 0)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.osmosdr_source.set_center_freq(self.freq+self.freq_offset, 0)

    def get_dv_channel(self):
        return self.dv_channel

    def set_dv_channel(self, dv_channel):
        self.dv_channel = dv_channel
        self.BLE_tools_BLE_pack_collect_0.reset_channel(self.dv_channel)

    def get_accaddr(self):
        return self.accaddr

    def set_accaddr(self, accaddr):
        self.accaddr = accaddr
        self.BLE_tools_BLE_pack_collect_0.reset_accaddr(str(hex(self.accaddr))[2:])


def main(top_block_cls=gr_ble, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
