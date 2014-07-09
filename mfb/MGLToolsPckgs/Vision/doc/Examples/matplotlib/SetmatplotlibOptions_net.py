########################################################################
#
#    Vision Network - Python source code - file generated by vision
#    Tuesday 17 April 2007 10:25:23 
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
# $Header: /opt/cvs/python/packages/share1.5/Vision/doc/Examples/matplotlib/SetmatplotlibOptions_net.py,v 1.2 2007/08/29 20:37:16 vareille Exp $
#
# $Id: SetmatplotlibOptions_net.py,v 1.2 2007/08/29 20:37:16 vareille Exp $
#

from traceback import print_exc
## loading libraries ##
from Vision.matplotlibNodes import matplotliblib
masterNet.getEditor().addLibraryInstance(matplotliblib,"Vision.matplotlibNodes", "matplotliblib")

try:
    ## saving node Set Matplotlib options ##
    from Vision.matplotlibNodes import MatPlotLibOptions
    Set_Matplotlib_options_20 = MatPlotLibOptions(constrkw = {}, name='Set Matplotlib options', library=matplotliblib)
    masterNet.addNode(Set_Matplotlib_options_20,202,77)
    Set_Matplotlib_options_20.inputPortByName['matplotlibOptions'].widget.set({'edgecolor': 'indigo', 'ytick.color': 'darkgreen', 'figpatch_facecolor': 'lightsalmon', 'facecolor': 'gold', 'figpatch_linewidth': 1.0, 'markeredgewidth': 6.8888888888888777, 'xtick.color': 'darkgreen', 'gridlinewidth': 4.6944444444444366, 'gridlinestyle': '--', 'figpatch_edgecolor': 'white', 'gridcolor': 'firebrick', 'gridOn': 1, 'ytick.labelsize': 19.250000000000046, 'xtick.labelsize': 17.388888888888907, 'linewidth': 5.4444444444444393, 'anchor': 'C'}, run=False)
except:
    print "WARNING: failed to restore MatPlotLibOptions named Set Matplotlib options in network masterNet"
    print_exc()
    Set_Matplotlib_options_20=None

try:
    ## saving node SinFunc ##
    from Vision.matplotlibNodes import SinFunc
    SinFunc_21 = SinFunc(constrkw = {}, name='SinFunc', library=matplotliblib)
    masterNet.addNode(SinFunc_21,35,11)
    apply(SinFunc_21.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore SinFunc named SinFunc in network masterNet"
    print_exc()
    SinFunc_21=None

try:
    ## saving node Plot ##
    from Vision.matplotlibNodes import PlotNE
    Plot_22 = PlotNE(constrkw = {}, name='Plot', library=matplotliblib)
    masterNet.addNode(Plot_22,41,158)
    apply(Plot_22.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore PlotNE named Plot in network masterNet"
    print_exc()
    Plot_22=None

masterNet.freeze()

## saving connections for network new ##
if SinFunc_21 is not None and Plot_22 is not None:
    try:
        masterNet.connectNodes(
            SinFunc_21, Plot_22, "y", "y", blocking=True)
    except:
        print "WARNING: failed to restore connection between SinFunc_21 and Plot_22 in network masterNet"
if Set_Matplotlib_options_20 is not None and Plot_22 is not None:
    try:
        masterNet.connectNodes(
            Set_Matplotlib_options_20, Plot_22, "matplotlibOptions", "drawAreaDef", blocking=True)
    except:
        print "WARNING: failed to restore connection between Set_Matplotlib_options_20 and Plot_22 in network masterNet"
masterNet.unfreeze()
#masterNet.run()
