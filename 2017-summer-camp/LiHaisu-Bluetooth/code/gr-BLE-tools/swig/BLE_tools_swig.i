/* -*- c++ -*- */

#define BLE_TOOLS_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "BLE_tools_swig_doc.i"

%{
#include "BLE_tools/find_pack_by_preamble.h"
%}


%include "BLE_tools/find_pack_by_preamble.h"
GR_SWIG_BLOCK_MAGIC2(BLE_tools, find_pack_by_preamble);
