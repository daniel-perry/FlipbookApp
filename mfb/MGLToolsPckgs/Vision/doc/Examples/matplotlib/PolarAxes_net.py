########################################################################
#
#    Vision Network - Python source code - file generated by vision
#    Monday 16 April 2007 14:16:54 
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
# $Header: /opt/cvs/python/packages/share1.5/Vision/doc/Examples/matplotlib/PolarAxes_net.py,v 1.3 2007/08/29 20:37:16 vareille Exp $
#
# $Id: PolarAxes_net.py,v 1.3 2007/08/29 20:37:16 vareille Exp $
#

from traceback import print_exc
## loading libraries ##
from Vision.matplotlibNodes import matplotliblib
masterNet.getEditor().addLibraryInstance(matplotliblib,"Vision.matplotlibNodes", "matplotliblib")

from Vision.StandardNodes import stdlib
masterNet.getEditor().addLibraryInstance(stdlib,"Vision.StandardNodes", "stdlib")

try:
    ## saving node PolarAxes ##
    from Vision.matplotlibNodes import PolarAxesNE
    PolarAxes_0 = PolarAxesNE(constrkw = {}, name='PolarAxes', library=matplotliblib)
    masterNet.addNode(PolarAxes_0,171,326)
except:
    print "WARNING: failed to restore PolarAxesNE named PolarAxes in network masterNet"
    print_exc()
    PolarAxes_0=None

try:
    ## saving node ReadTable ##
    from Vision.StandardNodes import ReadTable
    ReadTable_1 = ReadTable(constrkw = {}, name='ReadTable', library=stdlib)
    masterNet.addNode(ReadTable_1,156,28)
    ReadTable_1.inputPortByName['filename'].widget.set("Data/polar_data.dat", run=False)
    ReadTable_1.inputPortByName['sep'].widget.set(",", run=False)
    ReadTable_1.inputPortByName['datatype'].widget.set("float", run=False)
    apply(ReadTable_1.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore ReadTable named ReadTable in network masterNet"
    print_exc()
    ReadTable_1=None

try:
    ## saving node Index ##
    from Vision.StandardNodes import Index
    Index_2 = Index(constrkw = {}, name='Index', library=stdlib)
    masterNet.addNode(Index_2,65,203)
    apply(Index_2.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore Index named Index in network masterNet"
    print_exc()
    Index_2=None

try:
    ## saving node Index ##
    from Vision.StandardNodes import Index
    Index_3 = Index(constrkw = {}, name='Index', library=stdlib)
    masterNet.addNode(Index_3,284,194)
    apply(Index_3.inputPortByName['index'].widget.configure, (), {'max': 1})
    Index_3.inputPortByName['index'].widget.set(1, run=False)
    apply(Index_3.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore Index named Index in network masterNet"
    print_exc()
    Index_3=None

masterNet.freeze()

## saving connections for network PolarAxes ##
if ReadTable_1 is not None and Index_2 is not None:
    try:
        masterNet.connectNodes(
            ReadTable_1, Index_2, "data", "data", blocking=True)
    except:
        print "WARNING: failed to restore connection between ReadTable_1 and Index_2 in network masterNet"
if ReadTable_1 is not None and Index_3 is not None:
    try:
        masterNet.connectNodes(
            ReadTable_1, Index_3, "data", "data", blocking=True)
    except:
        print "WARNING: failed to restore connection between ReadTable_1 and Index_3 in network masterNet"
if Index_2 is not None and PolarAxes_0 is not None:
    try:
        masterNet.connectNodes(
            Index_2, PolarAxes_0, "data", "y", blocking=True)
    except:
        print "WARNING: failed to restore connection between Index_2 and PolarAxes_0 in network masterNet"
if Index_3 is not None and PolarAxes_0 is not None:
    try:
        masterNet.connectNodes(
            Index_3, PolarAxes_0, "data", "x", blocking=True)
    except:
        print "WARNING: failed to restore connection between Index_3 and PolarAxes_0 in network masterNet"
masterNet.unfreeze()
#masterNet.run()

