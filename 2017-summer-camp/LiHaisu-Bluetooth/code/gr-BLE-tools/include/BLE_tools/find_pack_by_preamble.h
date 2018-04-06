/* -*- c++ -*- */
/* 
 * Copyright 2017 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
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


#ifndef INCLUDED_BLE_TOOLS_FIND_PACK_BY_PREAMBLE_H
#define INCLUDED_BLE_TOOLS_FIND_PACK_BY_PREAMBLE_H

#include <BLE_tools/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace BLE_tools {

    /*!
     * \brief <+description of block+>
     * \ingroup BLE_tools
     *
     */
    class BLE_TOOLS_API find_pack_by_preamble : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<find_pack_by_preamble> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of BLE_tools::find_pack_by_preamble.
       *
       * To avoid accidental use of raw pointers, BLE_tools::find_pack_by_preamble's
       * constructor is in a private implementation
       * class. BLE_tools::find_pack_by_preamble::make is the public interface for
       * creating new instances.
       */
      static sptr make();
    };

  } // namespace BLE_tools
} // namespace gr

#endif /* INCLUDED_BLE_TOOLS_FIND_PACK_BY_PREAMBLE_H */

