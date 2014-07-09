########################################################################
#
#    Vision Network - Python source code - file generated by vision
#    Friday 13 April 2007 13:48:20 
#    
#       The Scripps Research Institute (TSRI)
#       Molecular Graphics Lab
#       La Jolla, CA 92037, USA
#
# Copyright: Daniel Stoffler, Michel Sanner and TSRI
#   
# revision: Guillaume Vareille
#  
#########################################################################
#
# $Header: /opt/cvs/python/packages/share1.5/Vision/doc/Examples/matplotlib/Specgram_net.py,v 1.3 2007/08/29 20:37:16 vareille Exp $
#
# $Id: Specgram_net.py,v 1.3 2007/08/29 20:37:16 vareille Exp $
#

from traceback import print_exc
## loading libraries ##
from Vision.matplotlibNodes import matplotliblib
masterNet.getEditor().addLibraryInstance(matplotliblib,"Vision.matplotlibNodes", "matplotliblib")

from Vision.StandardNodes import stdlib
masterNet.getEditor().addLibraryInstance(stdlib,"Vision.StandardNodes", "stdlib")

try:
    ## saving node ReadTable ##
    from Vision.StandardNodes import ReadTable
    ReadTable_140 = ReadTable(constrkw = {}, name='ReadTable', library=stdlib)
    masterNet.addNode(ReadTable_140,65,22)
    ReadTable_140.inputPortByName['filename'].widget.set("Data/specgram_data.dat", run=False)
    ReadTable_140.inputPortByName['sep'].widget.set(",", run=False)
    ReadTable_140.inputPortByName['datatype'].widget.set("float", run=False)
    apply(ReadTable_140.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore ReadTable named ReadTable in network masterNet"
    print_exc()
    ReadTable_140=None

try:
    ## saving node Index ##
    from Vision.StandardNodes import Index
    Index_141 = Index(constrkw = {}, name='Index', library=stdlib)
    masterNet.addNode(Index_141,87,192)
    apply(Index_141.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore Index named Index in network masterNet"
    print_exc()
    Index_141=None

try:
    ## saving node Specgram ##
    from Vision.matplotlibNodes import SpecgramNE
    Specgram_142 = SpecgramNE(constrkw = {}, name='Specgram', library=matplotliblib)
    masterNet.addNode(Specgram_142,101,312)
    Specgram_142.inputPortByName['NFFT'].widget.set("256", run=False)
    Specgram_142.inputPortByName['nOverlap'].widget.set("0", run=False)
except:
    print "WARNING: failed to restore SpecgramNE named Specgram in network masterNet"
    print_exc()
    Specgram_142=None

try:
    ## saving node ColorBar ##
    from Vision.matplotlibNodes import ColorBarNE
    ColorBar_143 = ColorBarNE(constrkw = {}, name='ColorBar', library=matplotliblib)
    masterNet.addNode(ColorBar_143,103,375)
except:
    print "WARNING: failed to restore ColorBarNE named ColorBar in network masterNet"
    print_exc()
    ColorBar_143=None

masterNet.freeze()

## saving connections for network Specgram ##
if ReadTable_140 is not None and Index_141 is not None:
    try:
        masterNet.connectNodes(
            ReadTable_140, Index_141, "data", "data", blocking=True)
    except:
        print "WARNING: failed to restore connection between ReadTable_140 and Index_141 in network masterNet"
if Index_141 is not None and Specgram_142 is not None:
    try:
        masterNet.connectNodes(
            Index_141, Specgram_142, "data", "arraylistx", blocking=True)
    except:
        print "WARNING: failed to restore connection between Index_141 and Specgram_142 in network masterNet"
if Specgram_142 is not None and ColorBar_143 is not None:
    try:
        masterNet.connectNodes(
            Specgram_142, ColorBar_143, "axes", "plot", blocking=True)
    except:
        print "WARNING: failed to restore connection between Specgram_142 and ColorBar_143 in network masterNet"
if Specgram_142 is not None and ColorBar_143 is not None:
    try:
        masterNet.connectNodes(
            Specgram_142, ColorBar_143, "image", "current_image", blocking=True)
    except:
        print "WARNING: failed to restore connection between Specgram_142 and ColorBar_143 in network masterNet"
masterNet.unfreeze()
#masterNet.run()

