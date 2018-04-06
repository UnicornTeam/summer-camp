#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Dronedb
# Generated: Tue Aug 22 02:23:20 2017
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

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys
import time


class DroneDB(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Dronedb")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Dronedb")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "DroneDB")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6
        self.head = head = int(2e6)
        self.cent_freq = cent_freq = 2.462e9
        self.band = band = 2e6

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(2),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(cent_freq, 0)
        self.uhd_usrp_source_0.set_gain(0, 0)
        self.uhd_usrp_source_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_source_0.set_center_freq(cent_freq, 1)
        self.uhd_usrp_source_0.set_gain(0, 1)
        self.uhd_usrp_source_0.set_antenna("RX2", 1)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=8,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=8,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_number_sink_0_0_1_0 = qtgui.number_sink(
            gr.sizeof_char,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0_0_1_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0_1_0.set_title("rightGFSK")
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                 "", "", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0_1_0.set_min(i, -1)
            self.qtgui_number_sink_0_0_1_0.set_max(i, 1)
            self.qtgui_number_sink_0_0_1_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_1_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_1_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_1_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_1_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0_0_1_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_1_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0_1_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_0_1_0_win)
        self.qtgui_number_sink_0_0_1 = qtgui.number_sink(
            gr.sizeof_char,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0_0_1.set_update_time(0.10)
        self.qtgui_number_sink_0_0_1.set_title("leftGFSK")
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                 "", "", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0_1.set_min(i, -1)
            self.qtgui_number_sink_0_0_1.set_max(i, 1)
            self.qtgui_number_sink_0_0_1.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_1.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_1.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_1.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_1.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0_0_1.enable_autoscale(False)
        self._qtgui_number_sink_0_0_1_win = sip.wrapinstance(self.qtgui_number_sink_0_0_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_0_1_win)
        self.qtgui_number_sink_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0_0.set_title("rightFRMS")
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                 "", "", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0_0.set_min(i, -1)
            self.qtgui_number_sink_0_0_0.set_max(i, 1)
            self.qtgui_number_sink_0_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_0_0_win)
        self.qtgui_number_sink_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0.set_title("leftFRMS")
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                 "", "", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0.set_min(i, -1)
            self.qtgui_number_sink_0_0.set_max(i, 1)
            self.qtgui_number_sink_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_0_win)
        self.fft_vxx_0_0 = fft.fft_vcc(1024, True, (window.blackmanharris(1024)), True, 1)
        self.fft_vxx_0 = fft.fft_vcc(1024, True, (window.blackmanharris(1024)), True, 1)
        self.digital_gfsk_demod_0_0 = digital.gfsk_demod(
        	samples_per_symbol=2,
        	sensitivity=1.0,
        	gain_mu=0.175,
        	mu=0.5,
        	omega_relative_limit=0.005,
        	freq_error=0.0,
        	verbose=False,
        	log=False,
        )
        self.digital_gfsk_demod_0 = digital.gfsk_demod(
        	samples_per_symbol=2,
        	sensitivity=1.0,
        	gain_mu=0.175,
        	mu=0.5,
        	omega_relative_limit=0.005,
        	freq_error=0.0,
        	verbose=False,
        	log=False,
        )
        self.blocks_vector_to_stream_0_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, 1024)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, 1024)
        self.blocks_stream_to_vector_0_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 1024)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 1024)
        self.blocks_skiphead_0_1_0 = blocks.skiphead(gr.sizeof_char*1, head/2)
        self.blocks_skiphead_0_1 = blocks.skiphead(gr.sizeof_char*1, head/2)
        self.blocks_skiphead_0_0 = blocks.skiphead(gr.sizeof_float*1, head)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_float*1, head)
        self.blocks_rms_xx_0_0 = blocks.rms_cf(0.0001)
        self.blocks_rms_xx_0 = blocks.rms_cf(0.0001)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((100, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((100, ))
        self.blocks_file_sink_0_0_1_0 = blocks.file_sink(gr.sizeof_char*1, "/home/summit/DroneIndicator/rightGFSK.dat", False)
        self.blocks_file_sink_0_0_1_0.set_unbuffered(False)
        self.blocks_file_sink_0_0_1 = blocks.file_sink(gr.sizeof_char*1, "/home/summit/DroneIndicator/leftGFSK.dat", False)
        self.blocks_file_sink_0_0_1.set_unbuffered(False)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_float*1, "/home/summit/DroneIndicator/rightFRMS.dat", False)
        self.blocks_file_sink_0_0_0.set_unbuffered(False)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_float*1, "/home/summit/DroneIndicator/leftFRMS.dat", False)
        self.blocks_file_sink_0_0.set_unbuffered(False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_skiphead_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_skiphead_0_0, 0))    
        self.connect((self.blocks_rms_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_rms_xx_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.blocks_skiphead_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.blocks_skiphead_0_0, 0), (self.rational_resampler_xxx_0_0, 0))    
        self.connect((self.blocks_skiphead_0_1, 0), (self.blocks_file_sink_0_0_1, 0))    
        self.connect((self.blocks_skiphead_0_1, 0), (self.qtgui_number_sink_0_0_1, 0))    
        self.connect((self.blocks_skiphead_0_1_0, 0), (self.blocks_file_sink_0_0_1_0, 0))    
        self.connect((self.blocks_skiphead_0_1_0, 0), (self.qtgui_number_sink_0_0_1_0, 0))    
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.fft_vxx_0, 0))    
        self.connect((self.blocks_stream_to_vector_0_0_0, 0), (self.fft_vxx_0_0, 0))    
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_rms_xx_0, 0))    
        self.connect((self.blocks_vector_to_stream_0_0, 0), (self.blocks_rms_xx_0_0, 0))    
        self.connect((self.digital_gfsk_demod_0, 0), (self.blocks_skiphead_0_1, 0))    
        self.connect((self.digital_gfsk_demod_0_0, 0), (self.blocks_skiphead_0_1_0, 0))    
        self.connect((self.fft_vxx_0, 0), (self.blocks_vector_to_stream_0, 0))    
        self.connect((self.fft_vxx_0_0, 0), (self.blocks_vector_to_stream_0_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_file_sink_0_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_number_sink_0_0, 0))    
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_file_sink_0_0_0, 0))    
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.qtgui_number_sink_0_0_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_stream_to_vector_0_0, 0))    
        self.connect((self.uhd_usrp_source_0, 1), (self.blocks_stream_to_vector_0_0_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.digital_gfsk_demod_0, 0))    
        self.connect((self.uhd_usrp_source_0, 1), (self.digital_gfsk_demod_0_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "DroneDB")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_head(self):
        return self.head

    def set_head(self, head):
        self.head = head

    def get_cent_freq(self):
        return self.cent_freq

    def set_cent_freq(self, cent_freq):
        self.cent_freq = cent_freq
        self.uhd_usrp_source_0.set_center_freq(self.cent_freq, 0)
        self.uhd_usrp_source_0.set_center_freq(self.cent_freq, 1)

    def get_band(self):
        return self.band

    def set_band(self, band):
        self.band = band


def main(top_block_cls=DroneDB, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
