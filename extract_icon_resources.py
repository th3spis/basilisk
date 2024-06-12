#! /usr/bin/env python3

#EXTRACT ICON FILES FROM PEs

import pefile
import sys 
import os
import struct 

dumpdir = sys.argv[1].split(".")[0]
pe = pefile.PE(sys.argv[1])


# Create the directory if it does not exist
if not os.path.exists(dumpdir):
    os.makedirs(dumpdir)

rt_icon_idx = [
  entry.id for entry in 
  pe.DIRECTORY_ENTRY_RESOURCE.entries].index(pefile.RESOURCE_TYPE['RT_ICON'])

# Get the directory entry
#
rt_icon_directory = pe.DIRECTORY_ENTRY_RESOURCE.entries[rt_icon_idx]

# For each of the entries (which will each contain a block of 16? icons)
#
i = 0
for entry in rt_icon_directory.directory.entries:

  # Get the RVA of the string data and
  # size of the string data
  #
  data_rva = entry.directory.entries[0].data.struct.OffsetToData
  size = entry.directory.entries[0].data.struct.Size
  obj = entry.directory.entries[0].data.struct
  
  # Retrieve the actual data and start processing the icons
  #
  data = pe.get_memory_mapped_image()[data_rva:data_rva+size]
  # Fix raw data header to make it an actual ICO file
  #
  #reserved
  # resource type -> 0x01 = ICO
  # number of images
  #width
  #heigth
  #colorcount
  #reserved
  #color planes
  #bits per pixel
  # size of the ico
  # offset in the array
  header = b"\x00\x00" \
    + b"\x01\x00" \
    + b"\x01\x00" \
    + data[4].to_bytes(1, byteorder='big') + data[8].to_bytes(1, byteorder='big') \
    + b"\x00" + b"\x00" \
    + data[12].to_bytes(1, byteorder='big') + data[13].to_bytes(1, byteorder='big') \
    + data[14].to_bytes(1, byteorder='big') + data[15].to_bytes(1, byteorder='big') \
    + struct.pack('<i', size) \
    + b"\x16\x00\x00\x00"
  
  data = header + data


  fname = "fileico"+ str(i) + ".ico"
  file_path = os.path.join(dumpdir, fname)
  print(fname)
  i = i +1
  with open(file_path, 'wb') as file:
      file.write(data)
