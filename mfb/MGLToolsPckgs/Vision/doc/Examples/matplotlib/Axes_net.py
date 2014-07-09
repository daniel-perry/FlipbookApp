#!/bin/ksh ~/.mgltools/pythonsh
########################################################################
#
#    Vision Network - Python source code - file generated by vision
#    Friday 31 July 2009 13:50:43 
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
# $Header: /opt/cvs/python/packages/share1.5/Vision/doc/Examples/matplotlib/Axes_net.py,v 1.4 2009/07/31 20:51:41 vareille Exp $
#
# $Id: Axes_net.py,v 1.4 2009/07/31 20:51:41 vareille Exp $
#


if __name__=='__main__':
    from sys import argv
    if '--help' in argv or '-h' in argv or '-w' in argv: # run without Vision
        withoutVision = True
        from Vision.VPE import NoGuiExec
        ed = NoGuiExec()
        from NetworkEditor.net import Network
        import os
        masterNet = Network("process-"+str(os.getpid()))
        ed.addNetwork(masterNet)
    else: # run as a stand alone application while vision is hidden
        withoutVision = False
        from Vision import launchVisionToRunNetworkAsApplication, mainLoopVisionToRunNetworkAsApplication
	if '-noSplash' in argv:
	    splash = False
	else:
	    splash = True
        masterNet = launchVisionToRunNetworkAsApplication(splash=splash)
        import os
        masterNet.filename = os.path.abspath(__file__)
from traceback import print_exc
## loading libraries ##
from Vision.matplotlibNodes import matplotliblib
from Vision.StandardNodes import stdlib
try:
    masterNet
except (NameError, AttributeError): # we run the network outside Vision
    from NetworkEditor.net import Network
    masterNet = Network()

masterNet.getEditor().addLibraryInstance(matplotliblib,"Vision.matplotlibNodes", "matplotliblib")

masterNet.getEditor().addLibraryInstance(stdlib,"Vision.StandardNodes", "stdlib")

try:
    ## saving node ReadTable ##
    from Vision.StandardNodes import ReadTable
    ReadTable_0 = ReadTable(constrkw={}, name='ReadTable', library=stdlib)
    masterNet.addNode(ReadTable_0,71,7)
    ReadTable_0.inputPortByName['filename'].widget.set(r"Data/axes_data.dat", run=False)
    ReadTable_0.inputPortByName['numOfTopLinesToJump'].widget.set(0, run=False)
    apply(ReadTable_0.inputPortByName['numOfBottomLinesToJump'].widget.configure, (), {'oneTurn': 10.0})
    ReadTable_0.inputPortByName['numOfBottomLinesToJump'].widget.set(2, run=False)
    ReadTable_0.inputPortByName['sep'].widget.set(r",", run=False)
    ReadTable_0.inputPortByName['datatype'].widget.set(r"float", run=False)
    apply(ReadTable_0.configure, (), {'paramPanelImmediate': 1, 'expanded': False})
except:
    print "WARNING: failed to restore ReadTable named ReadTable in network masterNet"
    print_exc()
    ReadTable_0=None

try:
    ## saving node Index ##
    from Vision.StandardNodes import Index
    Index_1 = Index(constrkw={}, name='Index', library=stdlib)
    masterNet.addNode(Index_1,17,143)
    Index_1.inputPortByName['index'].widget.set(0, run=False)
    apply(Index_1.configure, (), {'paramPanelImmediate': 1})
except:
    print "WARNING: failed to restore Index named Index in network masterNet"
    print_exc()
    Index_1=None

try:
    ## saving node Index ##
    from Vision.StandardNodes import Index
    Index_2 = Index(constrkw={}, name='Index', library=stdlib)
    masterNet.addNode(Index_2,137,143)
    apply(Index_2.inputPortByName['index'].widget.configure, (), {'max': 3})
    Index_2.inputPortByName['index'].widget.set(1, run=False)
    apply(Index_2.configure, (), {'paramPanelImmediate': 1})
except:
    print "WARNING: failed to restore Index named Index in network masterNet"
    print_exc()
    Index_2=None

try:
    ## saving node Index ##
    from Vision.StandardNodes import Index
    Index_3 = Index(constrkw={}, name='Index', library=stdlib)
    masterNet.addNode(Index_3,254,134)
    apply(Index_3.inputPortByName['index'].widget.configure, (), {'max': 1, 'min': -2})
    Index_3.inputPortByName['index'].widget.set(0, run=False)
    apply(Index_3.configure, (), {'paramPanelImmediate': 1})
except:
    print "WARNING: failed to restore Index named Index in network masterNet"
    print_exc()
    Index_3=None

try:
    ## saving node Index ##
    from Vision.StandardNodes import Index
    Index_4 = Index(constrkw={}, name='Index', library=stdlib)
    masterNet.addNode(Index_4,375,137)
    apply(Index_4.inputPortByName['index'].widget.configure, (), {'max': 1, 'min': -2})
    Index_4.inputPortByName['index'].widget.set(1, run=False)
    apply(Index_4.configure, (), {'paramPanelImmediate': 1})
except:
    print "WARNING: failed to restore Index named Index in network masterNet"
    print_exc()
    Index_4=None

try:
    ## saving node Plot ##
    from Vision.matplotlibNodes import PlotNE
    Plot_5 = PlotNE(constrkw={}, name='Plot', library=matplotliblib)
    masterNet.addNode(Plot_5,211,331)
    Plot_5.inputPortByName['lineStyle'].widget.set(r"solid", run=False)
    Plot_5.inputPortByName['color'].widget.set(r"blue", run=False)
    Plot_5.inputPortByName['line_antialiased'].widget.set(1, run=False)
    Plot_5.inputPortByName['line_linewidth'].widget.set(2, run=False)
    Plot_5.inputPortByName['solid_joinstyle'].widget.set(r"miter", run=False)
    Plot_5.inputPortByName['solid_capstyle'].widget.set(r"projecting", run=False)
    Plot_5.inputPortByName['dash_capstyle'].widget.set(r"butt", run=False)
    Plot_5.inputPortByName['dash_joinstyle'].widget.set(r"miter", run=False)
except:
    print "WARNING: failed to restore PlotNE named Plot in network masterNet"
    print_exc()
    Plot_5=None

try:
    ## saving node Draw Area ##
    from Vision.matplotlibNodes import MPLDrawAreaNE
    Draw_Area_6 = MPLDrawAreaNE(constrkw={}, name='Draw Area', library=matplotliblib)
    masterNet.addNode(Draw_Area_6,208,263)
    Draw_Area_6.inputPortByName['left'].widget.set(0.2, run=False)
    Draw_Area_6.inputPortByName['bottom'].widget.set(0.6, run=False)
    Draw_Area_6.inputPortByName['width'].widget.set(0.2, run=False)
    Draw_Area_6.inputPortByName['height'].widget.set(0.2, run=False)
    Draw_Area_6.inputPortByName['frameon'].widget.set(1, run=False)
    Draw_Area_6.inputPortByName['hold'].widget.set(0, run=False)
    Draw_Area_6.inputPortByName['title'].widget.set(r"Impulse Response", run=False)
    Draw_Area_6.inputPortByName['xlabel'].widget.set(r"", run=False)
    Draw_Area_6.inputPortByName['ylabel'].widget.set(r"", run=False)
    Draw_Area_6.inputPortByName['xlimit'].widget.set(r"", run=False)
    Draw_Area_6.inputPortByName['ylimit'].widget.set(r"", run=False)
    Draw_Area_6.inputPortByName['xticklabels'].widget.set(0, run=False)
    Draw_Area_6.inputPortByName['yticklabels'].widget.set(0, run=False)
    Draw_Area_6.inputPortByName['axison'].widget.set(1, run=False)
    Draw_Area_6.inputPortByName['autoscaleon'].widget.set(1, run=False)
except:
    print "WARNING: failed to restore MPLDrawAreaNE named Draw Area in network masterNet"
    print_exc()
    Draw_Area_6=None

try:
    ## saving node Set Matplotlib options ##
    from Vision.matplotlibNodes import MatPlotLibOptions
    Set_Matplotlib_options_7 = MatPlotLibOptions(constrkw={}, name='Set Matplotlib options', library=matplotliblib)
    masterNet.addNode(Set_Matplotlib_options_7,332,262)
    Set_Matplotlib_options_7.inputPortByName['matplotlibOptions'].widget.set({'ytick.color': 'black', 'figpatch_facecolor': 'darkgray', 'facecolor': 'yellow', 'xtick.color': 'black', 'markeredgewidth': 0.0, 'xtick.labelrotation': 0, 'xtick.major.pad': 3, 'xtick.minor.pad': 3}, run=False)
except:
    print "WARNING: failed to restore MatPlotLibOptions named Set Matplotlib options in network masterNet"
    print_exc()
    Set_Matplotlib_options_7=None

try:
    ## saving node Figure ##
    from Vision.matplotlibNodes import MPLFigureNE
    Figure_8 = MPLFigureNE(constrkw={}, name='Figure', library=matplotliblib)
    masterNet.addNode(Figure_8,231,458)
    Figure_8.inputPortByName['width'].widget.set(8.125, run=False)
    Figure_8.inputPortByName['height'].widget.set(6.125, run=False)
    Figure_8.inputPortByName['linewidth'].widget.set(1, run=False)
    Figure_8.inputPortByName['dpi'].widget.set(80, run=False)
    Figure_8.inputPortByName['nbRows'].widget.set(1, run=False)
    Figure_8.inputPortByName['nbColumns'].widget.set(1, run=False)
    Figure_8.inputPortByName['frameon'].widget.set(1, run=False)
    Figure_8.inputPortByName['hold'].widget.set(0, run=False)
    Figure_8.inputPortByName['toolbar'].widget.set(1, run=False)
    Figure_8.inputPortByName['packOpts'].widget.set(r"{'side':'top', 'fill':'both', 'expand':1}", run=False)
except:
    print "WARNING: failed to restore MPLFigureNE named Figure in network masterNet"
    print_exc()
    Figure_8=None

try:
    ## saving node Plot ##
    from Vision.matplotlibNodes import PlotNE
    Plot_9 = PlotNE(constrkw={}, name='Plot', library=matplotliblib)
    masterNet.addNode(Plot_9,17,330)
    Plot_9.inputPortByName['lineStyle'].widget.set(r"solid", run=False)
    Plot_9.inputPortByName['color'].widget.set(r"blue", run=False)
    Plot_9.inputPortByName['line_antialiased'].widget.set(1, run=False)
    Plot_9.inputPortByName['line_linewidth'].widget.set(1, run=False)
    Plot_9.inputPortByName['solid_joinstyle'].widget.set(r"miter", run=False)
    Plot_9.inputPortByName['solid_capstyle'].widget.set(r"projecting", run=False)
    Plot_9.inputPortByName['dash_capstyle'].widget.set(r"butt", run=False)
    Plot_9.inputPortByName['dash_joinstyle'].widget.set(r"miter", run=False)
except:
    print "WARNING: failed to restore PlotNE named Plot in network masterNet"
    print_exc()
    Plot_9=None

try:
    ## saving node Draw Area ##
    from Vision.matplotlibNodes import MPLDrawAreaNE
    Draw_Area_10 = MPLDrawAreaNE(constrkw={}, name='Draw Area', library=matplotliblib)
    masterNet.addNode(Draw_Area_10,56,274)
    Draw_Area_10.inputPortByName['left'].widget.set(0.1, run=False)
    Draw_Area_10.inputPortByName['bottom'].widget.set(0.1, run=False)
    Draw_Area_10.inputPortByName['width'].widget.set(0.8, run=False)
    Draw_Area_10.inputPortByName['height'].widget.set(0.8, run=False)
    Draw_Area_10.inputPortByName['frameon'].widget.set(1, run=False)
    Draw_Area_10.inputPortByName['hold'].widget.set(0, run=False)
    Draw_Area_10.inputPortByName['title'].widget.set(r"Gaussian colored noise", run=False)
    Draw_Area_10.inputPortByName['xlabel'].widget.set(r"time(s)", run=False)
    Draw_Area_10.inputPortByName['ylabel'].widget.set(r"current(nA)", run=False)
    Draw_Area_10.inputPortByName['xlimit'].widget.set(r"[0,1]", run=False)
    Draw_Area_10.inputPortByName['ylimit'].widget.set(r"[-.02,0.035]", run=False)
    Draw_Area_10.inputPortByName['xticklabels'].widget.set(1, run=False)
    Draw_Area_10.inputPortByName['yticklabels'].widget.set(1, run=False)
    Draw_Area_10.inputPortByName['axison'].widget.set(1, run=False)
    Draw_Area_10.inputPortByName['autoscaleon'].widget.set(0, run=False)
except:
    print "WARNING: failed to restore MPLDrawAreaNE named Draw Area in network masterNet"
    print_exc()
    Draw_Area_10=None

try:
    ## saving node Histogram ##
    from Vision.matplotlibNodes import HistogramNE
    Histogram_11 = HistogramNE(constrkw={}, name='Histogram', library=matplotliblib)
    masterNet.addNode(Histogram_11,391,322)
    Histogram_11.inputPortByName['bins'].widget.set(400, run=False)
    Histogram_11.inputPortByName['normed'].widget.set(1, run=False)
    Histogram_11.inputPortByName['patch_antialiased'].widget.set(1, run=False)
    Histogram_11.inputPortByName['patch_linewidth'].widget.set(1, run=False)
    Histogram_11.inputPortByName['patch_edgecolor'].widget.set(r"black", run=False)
    Histogram_11.inputPortByName['patch_facecolor'].widget.set(r"blue", run=False)
except:
    print "WARNING: failed to restore HistogramNE named Histogram in network masterNet"
    print_exc()
    Histogram_11=None

try:
    ## saving node Draw Area ##
    from Vision.matplotlibNodes import MPLDrawAreaNE
    Draw_Area_12 = MPLDrawAreaNE(constrkw={}, name='Draw Area', library=matplotliblib)
    masterNet.addNode(Draw_Area_12,553,262)
    Draw_Area_12.inputPortByName['left'].widget.set(0.65, run=False)
    Draw_Area_12.inputPortByName['bottom'].widget.set(0.6, run=False)
    Draw_Area_12.inputPortByName['width'].widget.set(0.2, run=False)
    Draw_Area_12.inputPortByName['height'].widget.set(0.2, run=False)
    Draw_Area_12.inputPortByName['frameon'].widget.set(1, run=False)
    Draw_Area_12.inputPortByName['hold'].widget.set(0, run=False)
    Draw_Area_12.inputPortByName['title'].widget.set(r"Probability", run=False)
    Draw_Area_12.inputPortByName['xlabel'].widget.set(r"", run=False)
    Draw_Area_12.inputPortByName['ylabel'].widget.set(r"", run=False)
    Draw_Area_12.inputPortByName['xlimit'].widget.set(r"", run=False)
    Draw_Area_12.inputPortByName['ylimit'].widget.set(r"", run=False)
    Draw_Area_12.inputPortByName['xticklabels'].widget.set(0, run=False)
    Draw_Area_12.inputPortByName['yticklabels'].widget.set(0, run=False)
    Draw_Area_12.inputPortByName['axison'].widget.set(1, run=False)
    Draw_Area_12.inputPortByName['autoscaleon'].widget.set(1, run=False)
except:
    print "WARNING: failed to restore MPLDrawAreaNE named Draw Area in network masterNet"
    print_exc()
    Draw_Area_12=None

try:
    ## saving node ReadTable ##
    from Vision.StandardNodes import ReadTable
    ReadTable_13 = ReadTable(constrkw={}, name='ReadTable', library=stdlib)
    masterNet.addNode(ReadTable_13,353,7)
    ReadTable_13.inputPortByName['filename'].widget.set(r"Data/axes_data.dat", run=False)
    apply(ReadTable_13.inputPortByName['numOfTopLinesToJump'].widget.configure, (), {'oneTurn': 10.0})
    ReadTable_13.inputPortByName['numOfTopLinesToJump'].widget.set(2, run=False)
    ReadTable_13.inputPortByName['numOfBottomLinesToJump'].widget.set(0, run=False)
    ReadTable_13.inputPortByName['sep'].widget.set(r",", run=False)
    ReadTable_13.inputPortByName['datatype'].widget.set(r"float", run=False)
    apply(ReadTable_13.configure, (), {'paramPanelImmediate': 1, 'expanded': False})
except:
    print "WARNING: failed to restore ReadTable named ReadTable in network masterNet"
    print_exc()
    ReadTable_13=None

#masterNet.run()
masterNet.freeze()

## saving connections for network Axes ##
if ReadTable_0 is not None and Index_1 is not None:
    try:
        masterNet.connectNodes(
            ReadTable_0, Index_1, "data", "data", blocking=True
            , splitratio=[0.55438560191785424, 0.25525704259920123])
    except:
        print "WARNING: failed to restore connection between ReadTable_0 and Index_1 in network masterNet"
if ReadTable_0 is not None and Index_2 is not None:
    try:
        masterNet.connectNodes(
            ReadTable_0, Index_2, "data", "data", blocking=True
            , splitratio=[0.20186193362403329, 0.57002647351380153])
    except:
        print "WARNING: failed to restore connection between ReadTable_0 and Index_2 in network masterNet"
if Index_4 is not None and Plot_5 is not None:
    try:
        masterNet.connectNodes(
            Index_4, Plot_5, "data", "y", blocking=True
            , splitratio=[0.40697243920043913, 0.23394622808726456])
    except:
        print "WARNING: failed to restore connection between Index_4 and Plot_5 in network masterNet"
if Draw_Area_6 is not None and Plot_5 is not None:
    try:
        masterNet.connectNodes(
            Draw_Area_6, Plot_5, "drawAreaDef", "drawAreaDef", blocking=True
            , splitratio=[0.20595410707112688, 0.71644889427604341])
    except:
        print "WARNING: failed to restore connection between Draw_Area_6 and Plot_5 in network masterNet"
if Set_Matplotlib_options_7 is not None and Plot_5 is not None:
    try:
        masterNet.connectNodes(
            Set_Matplotlib_options_7, Plot_5, "matplotlibOptions", "drawAreaDef", blocking=True
            , splitratio=[0.54510966817293682, 0.21171641614632988])
    except:
        print "WARNING: failed to restore connection between Set_Matplotlib_options_7 and Plot_5 in network masterNet"
if Index_3 is not None and Plot_5 is not None:
    try:
        masterNet.connectNodes(
            Index_3, Plot_5, "data", "x", blocking=True
            , splitratio=[0.30457652550221609, 0.60473156285545304])
    except:
        print "WARNING: failed to restore connection between Index_3 and Plot_5 in network masterNet"
if Index_1 is not None and Plot_9 is not None:
    try:
        masterNet.connectNodes(
            Index_1, Plot_9, "data", "x", blocking=True
            , splitratio=[0.62512385280665039, 0.51790181766779386])
    except:
        print "WARNING: failed to restore connection between Index_1 and Plot_9 in network masterNet"
if Index_2 is not None and Plot_9 is not None:
    try:
        masterNet.connectNodes(
            Index_2, Plot_9, "data", "y", blocking=True
            , splitratio=[0.49815788096874569, 0.419525866516405])
    except:
        print "WARNING: failed to restore connection between Index_2 and Plot_9 in network masterNet"
if Draw_Area_10 is not None and Plot_9 is not None:
    try:
        masterNet.connectNodes(
            Draw_Area_10, Plot_9, "drawAreaDef", "drawAreaDef", blocking=True
            , splitratio=[0.49431623929873819, 0.26959589338912937])
    except:
        print "WARNING: failed to restore connection between Draw_Area_10 and Plot_9 in network masterNet"
if Index_2 is not None and Histogram_11 is not None:
    try:
        masterNet.connectNodes(
            Index_2, Histogram_11, "data", "values", blocking=True
            , splitratio=[0.51533935539990461, 0.59018237688161657])
    except:
        print "WARNING: failed to restore connection between Index_2 and Histogram_11 in network masterNet"
if Draw_Area_12 is not None and Histogram_11 is not None:
    try:
        masterNet.connectNodes(
            Draw_Area_12, Histogram_11, "drawAreaDef", "drawAreaDef", blocking=True
            , splitratio=[0.47709068820650991, 0.36104088908193221])
    except:
        print "WARNING: failed to restore connection between Draw_Area_12 and Histogram_11 in network masterNet"
if Set_Matplotlib_options_7 is not None and Histogram_11 is not None:
    try:
        masterNet.connectNodes(
            Set_Matplotlib_options_7, Histogram_11, "matplotlibOptions", "drawAreaDef", blocking=True
            , splitratio=[0.48749995121892287, 0.5088787708763769])
    except:
        print "WARNING: failed to restore connection between Set_Matplotlib_options_7 and Histogram_11 in network masterNet"
if Plot_9 is not None and Figure_8 is not None:
    try:
        masterNet.connectNodes(
            Plot_9, Figure_8, "plot", "plots", blocking=True
            , splitratio=[0.28044155582573271, 0.59141832051622767])
    except:
        print "WARNING: failed to restore connection between Plot_9 and Figure_8 in network masterNet"
if Histogram_11 is not None and Figure_8 is not None:
    try:
        masterNet.connectNodes(
            Histogram_11, Figure_8, "plot", "plots", blocking=True
            , splitratio=[0.20339315653950057, 0.57233429894184595])
    except:
        print "WARNING: failed to restore connection between Histogram_11 and Figure_8 in network masterNet"
if Plot_5 is not None and Figure_8 is not None:
    try:
        masterNet.connectNodes(
            Plot_5, Figure_8, "plot", "plots", blocking=True
            , splitratio=[0.62878176713748468, 0.73686982238443144])
    except:
        print "WARNING: failed to restore connection between Plot_5 and Figure_8 in network masterNet"
if ReadTable_13 is not None and Index_3 is not None:
    try:
        masterNet.connectNodes(
            ReadTable_13, Index_3, "data", "data", blocking=True
            , splitratio=[0.71730437728421825, 0.56152267667869604])
    except:
        print "WARNING: failed to restore connection between ReadTable_13 and Index_3 in network masterNet"
if ReadTable_13 is not None and Index_4 is not None:
    try:
        masterNet.connectNodes(
            ReadTable_13, Index_4, "data", "data", blocking=True
            , splitratio=[0.37355536907911602, 0.43804263084754258])
    except:
        print "WARNING: failed to restore connection between ReadTable_13 and Index_4 in network masterNet"
masterNet.runOnNewData.value = True

if __name__=='__main__':
    from sys import argv
    lNodePortValues = []
    if (len(argv) > 1) and argv[1].startswith('-'):
        lArgIndex = 2
    else:
        lArgIndex = 1
    while lArgIndex < len(argv) and argv[lArgIndex][-3:]!='.py':
        lNodePortValues.append(argv[lArgIndex])
        lArgIndex += 1
    masterNet.setNodePortValues(lNodePortValues)
    if '--help' in argv or '-h' in argv: # show help
        masterNet.helpForNetworkAsApplication()
    elif '-w' in argv: # run without Vision and exit
         # create communicator
        from NetworkEditor.net import Communicator
        masterNet.communicator = Communicator(masterNet)
        print 'Communicator listening on port:', masterNet.communicator.port

        import socket
        f = open(argv[0]+'.sock', 'w')
        f.write("%s %i"%(socket.gethostbyname(socket.gethostname()),
                         masterNet.communicator.port))
        f.close()

        # create communication socket
        import socket
        HOST = ''                 # Symbolic name meaning the local host
        PORT = 50010              # Arbitrary non-privileged port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(5)
        s.setblocking(0)
        masterNet.socket = s
        masterNet.socketConnections = []
        masterNet.HOST = HOST
        masterNet.PORT = PORT

        masterNet.run()

    else: # stand alone application while vision is hidden
        if '-e' in argv: # run and exit
            masterNet.run()
        elif '-r' in argv or len(masterNet.userPanels) == 0: # no user panel => run
            masterNet.run()
            mainLoopVisionToRunNetworkAsApplication(masterNet.editor)
        else: # user panel
            mainLoopVisionToRunNetworkAsApplication(masterNet.editor)
