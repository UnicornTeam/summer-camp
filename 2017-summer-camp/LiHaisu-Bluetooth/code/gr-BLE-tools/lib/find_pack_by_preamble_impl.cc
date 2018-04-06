/* -*- c++ -*- */
/* 
 * Copyright 2017 qihoo-360  backahasten.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "find_pack_by_preamble_impl.h"

namespace gr {
  namespace BLE_tools {
    unsigned char buf[375];
	  int i;               //计数器
	  int n;               //计数器
    int k=0;  
    unsigned char out[47];        
    find_pack_by_preamble::sptr
    find_pack_by_preamble::make()
    {
      return gnuradio::get_initial_sptr
        (new find_pack_by_preamble_impl());
    }

    /*
     * The private constructor
     */
    find_pack_by_preamble_impl::find_pack_by_preamble_impl()
      : gr::sync_block("find_pack_by_preamble",
              gr::io_signature::make(1, 1, sizeof(unsigned char)),
              gr::io_signature::make(0, 0, 0))
    {
       set_output_multiple(376*sizeof(char));
       message_port_register_out(pmt::mp("out"));
    }

    /*
     * Our virtual destructor.
     */
    find_pack_by_preamble_impl::~find_pack_by_preamble_impl()
    {
    }
    
    int
    find_pack_by_preamble_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
//**********************************************************************
//work here
//----------------------------------------------------------------------
      const unsigned char *in = (const unsigned char *) input_items[0];
      unsigned int index_tmp = 0;
      for(n=0;n<noutput_items;n++)
      {
        for(i=0;i<375;i++)
	      {
          buf[i] = buf[i+1];
        }
        buf[375] = in[n];
        //前导码查找 01010101(小端序) 地址是0xD6小端序(01101011)，0xBE以此类推。。。。
        //保证前九个都是交替位
        if((buf[0]==0 && buf[1]==1 && buf[2]==0 && buf[3]==1 && buf[4]==0&& buf[5]==1&& buf[6]==0&& buf[7]==1 && buf[8]==0) || (buf[0]==1 && buf[1]==0 && buf[2]==1 && buf[3]==0 && buf[4]==1&& buf[5]==0&& buf[6]==1&& buf[7]==0 && buf[8]==1))
        
	//&& buf[9]==1 && buf[10]==1 && buf[11]==0 && buf[12]==1 && buf[13]==0 && buf[14]==1 && buf[15]==1 && buf[16]==0 && buf[17]==1 && buf[18]==1 && buf[19]==1 && buf[20]==1 && buf[21]==1 &&buf[22]==0 && buf[23] == 1 && buf[24] == 1 && buf[25]==0 && buf[26]==0 && buf[27]==1 && buf[28]==0 && buf[29]==0 && buf[30]==0 && buf[31]==1 && buf[32]==0 && buf[33]==1 && buf[34]==1 && buf[35]==1 && buf[36]==0 && buf[37]==0 && buf[38]==0 && buf[39]==1这一部分交给后续的python模块检查，此处不再需要
        {

	  /*for(i=0;i<40;i++)
	  {
            printf("%d",out[i]);
          }
          printf("\n");*/
	  pmt::pmt_t pdu(pmt::cons(pmt::PMT_NIL,pmt::init_u8vector(376,buf)));   //设置缓冲区和格式
	  
          message_port_pub(pmt::mp("out"), pdu);                  //发送，格式是byte，低地址位有效LSB
        }
      }

//***********************************************************************
      return noutput_items;
    }

  } /* namespace BLE_tools */
} /* namespace gr */


