########################################################################
#
#    Vision Network - Python source code - file generated by vision
#    Friday 13 April 2007 12:34:25 
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
# $Header: /opt/cvs/python/packages/share1.5/Vision/doc/Examples/matplotlib/BarH_net.py,v 1.3 2007/08/29 20:37:16 vareille Exp $
#
# $Id: BarH_net.py,v 1.3 2007/08/29 20:37:16 vareille Exp $
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
    ReadTable_0 = ReadTable(constrkw = {}, name='ReadTable', library=stdlib)
    masterNet.addNode(ReadTable_0,138,9)
    ReadTable_0.inputPortByName['filename'].widget.set("Data/barh_plot_data.dat", run=False)
    ReadTable_0.inputPortByName['sep'].widget.set(",", run=False)
    ReadTable_0.inputPortByName['datatype'].widget.set("float", run=False)
    apply(ReadTable_0.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore ReadTable named ReadTable in network masterNet"
    print_exc()
    ReadTable_0=None

try:
    ## saving node BarH ##
    from Vision.matplotlibNodes import BarHNE
    BarH_1 = BarHNE(constrkw = {}, name='BarH', library=matplotliblib)
    masterNet.addNode(BarH_1,133,326)
except:
    print "WARNING: failed to restore BarHNE named BarH in network masterNet"
    print_exc()
    BarH_1=None

try:
    ## saving node Index ##
    from Vision.StandardNodes import Index
    Index_2 = Index(constrkw = {}, name='Index', library=stdlib)
    masterNet.addNode(Index_2,14,178)
    apply(Index_2.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore Index named Index in network masterNet"
    print_exc()
    Index_2=None

try:
    ## saving node Index ##
    from Vision.StandardNodes import Index
    Index_3 = Index(constrkw = {}, name='Index', library=stdlib)
    masterNet.addNode(Index_3,156,177)
    apply(Index_3.inputPortByName['index'].widget.configure, (), {'max': 2})
    Index_3.inputPortByName['index'].widget.set(1, run=False)
    apply(Index_3.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore Index named Index in network masterNet"
    print_exc()
    Index_3=None

try:
    ## saving node Index ##
    from Vision.StandardNodes import Index
    Index_4 = Index(constrkw = {}, name='Index', library=stdlib)
    masterNet.addNode(Index_4,300,178)
    apply(Index_4.inputPortByName['index'].widget.configure, (), {'max': 2})
    Index_4.inputPortByName['index'].widget.set(2, run=False)
    apply(Index_4.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore Index named Index in network masterNet"
    print_exc()
    Index_4=None

masterNet.freeze()

## saving connections for network BarH ##
if ReadTable_0 is not None and Index_2 is not None:
    try:
        masterNet.connectNodes(
            ReadTable_0, Index_2, "data", "data", blocking=True)
    except:
        print "WARNING: failed to restore connection between ReadTable_0 and Index_2 in network masterNet"
if ReadTable_0 is not None and Index_3 is not None:
    try:
        masterNet.connectNodes(
            ReadTable_0, Index_3, "data", "data", blocking=True)
    except:
        print "WARNING: failed to restore connection between ReadTable_0 and Index_3 in network masterNet"
if ReadTable_0 is not None and Index_4 is not None:
    try:
        masterNet.connectNodes(
            ReadTable_0, Index_4, "data", "data", blocking=True)
    except:
        print "WARNING: failed to restore connection between ReadTable_0 and Index_4 in network masterNet"
if Index_2 is not None and BarH_1 is not None:
    try:
        masterNet.connectNodes(
            Index_2, BarH_1, "data", "bottom", blocking=True)
    except:
        print "WARNING: failed to restore connection between Index_2 and BarH_1 in network masterNet"
if Index_3 is not None and BarH_1 is not None:
    try:
        masterNet.connectNodes(
            Index_3, BarH_1, "data", "width", blocking=True)
    except:
        print "WARNING: failed to restore connection between Index_3 and BarH_1 in network masterNet"
if Index_4 is not None and BarH_1 is not None:
    try:
        masterNet.connectNodes(
            Index_4, BarH_1, "data", "xerr", blocking=True)
    except:
        print "WARNING: failed to restore connection between Index_4 and BarH_1 in network masterNet"
masterNet.unfreeze()
#masterNet.run()

