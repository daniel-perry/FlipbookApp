########################################################################
#
#    Vision Network - Python source code - file generated by vision
#    Friday 13 April 2007 13:57:30 
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
# $Header: /opt/cvs/python/packages/share1.5/Vision/doc/Examples/matplotlib/TextAlign_net.py,v 1.3 2007/08/29 20:37:16 vareille Exp $
#
# $Id: TextAlign_net.py,v 1.3 2007/08/29 20:37:16 vareille Exp $
#

from traceback import print_exc
## loading libraries ##
from Vision.matplotlibNodes import matplotliblib
masterNet.getEditor().addLibraryInstance(matplotliblib,"Vision.matplotlibNodes", "matplotliblib")

from Vision.StandardNodes import stdlib
masterNet.getEditor().addLibraryInstance(stdlib,"Vision.StandardNodes", "stdlib")

try:
    ## saving node BarH ##
    from Vision.matplotlibNodes import BarHNE
    BarH_162 = BarHNE(constrkw = {}, name='BarH', library=matplotliblib)
    masterNet.addNode(BarH_162,137,538)
    BarH_162.inputPortByName['color'].widget.set("w", run=False)
    BarH_162.inputPortByName['edgecolor'].widget.set("k", run=False)
except:
    print "WARNING: failed to restore BarHNE named BarH in network masterNet"
    print_exc()
    BarH_162=None

try:
    ## saving node ReadTable ##
    from Vision.StandardNodes import ReadTable
    ReadTable_163 = ReadTable(constrkw = {}, name='ReadTable', library=stdlib)
    masterNet.addNode(ReadTable_163,135,21)
    ReadTable_163.inputPortByName['filename'].widget.set("Data/text_align_data.dat", run=False)
    ReadTable_163.inputPortByName['sep'].widget.set(",", run=False)
    ReadTable_163.inputPortByName['datatype'].widget.set("float", run=False)
    apply(ReadTable_163.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore ReadTable named ReadTable in network masterNet"
    print_exc()
    ReadTable_163=None

try:
    ## saving node Index ##
    from Vision.StandardNodes import Index
    Index_164 = Index(constrkw = {}, name='Index', library=stdlib)
    masterNet.addNode(Index_164,4,168)
    apply(Index_164.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore Index named Index in network masterNet"
    print_exc()
    Index_164=None

try:
    ## saving node Index ##
    from Vision.StandardNodes import Index
    Index_165 = Index(constrkw = {}, name='Index', library=stdlib)
    masterNet.addNode(Index_165,139,171)
    apply(Index_165.inputPortByName['index'].widget.configure, (), {'max': 3})
    Index_165.inputPortByName['index'].widget.set(1, run=False)
    apply(Index_165.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore Index named Index in network masterNet"
    print_exc()
    Index_165=None

try:
    ## saving node Index ##
    from Vision.StandardNodes import Index
    Index_166 = Index(constrkw = {}, name='Index', library=stdlib)
    masterNet.addNode(Index_166,274,178)
    apply(Index_166.inputPortByName['index'].widget.configure, (), {'max': 3})
    Index_166.inputPortByName['index'].widget.set(2, run=False)
    apply(Index_166.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore Index named Index in network masterNet"
    print_exc()
    Index_166=None

try:
    ## saving node Index ##
    from Vision.StandardNodes import Index
    Index_167 = Index(constrkw = {}, name='Index', library=stdlib)
    masterNet.addNode(Index_167,407,177)
    apply(Index_167.inputPortByName['index'].widget.configure, (), {'max': 3})
    Index_167.inputPortByName['index'].widget.set(3, run=False)
    apply(Index_167.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore Index named Index in network masterNet"
    print_exc()
    Index_167=None

try:
    ## saving node Draw Area ##
    from Vision.matplotlibNodes import MPLDrawAreaNE
    Draw_Area_168 = MPLDrawAreaNE(constrkw = {}, name='Draw Area', library=matplotliblib)
    masterNet.addNode(Draw_Area_168,432,496)
    Draw_Area_168.inputPortByName['title'].widget.set("", run=False)
    Draw_Area_168.inputPortByName['xlimit'].widget.set("[0,1]", run=False)
    Draw_Area_168.inputPortByName['ylimit'].widget.set("[0,1]", run=False)
    Draw_Area_168.inputPortByName['axison'].widget.set(0, run=False)
    Draw_Area_168.inputPortByName['autoscaleon'].widget.set(0, run=False)
except:
    print "WARNING: failed to restore MPLDrawAreaNE named Draw Area in network masterNet"
    print_exc()
    Draw_Area_168=None

try:
    ## saving node MergeText ##
    from Vision.matplotlibNodes import MPLMergeTextNE
    MergeText_169 = MPLMergeTextNE(constrkw = {}, name='MergeText', library=matplotliblib)
    masterNet.addNode(MergeText_169,578,503)
except:
    print "WARNING: failed to restore MPLMergeTextNE named MergeText in network masterNet"
    print_exc()
    MergeText_169=None

try:
    ## saving node Text ##
    from Vision.matplotlibNodes import Text
    Text_170 = Text(constrkw = {}, name='Text', library=matplotliblib)
    masterNet.addNode(Text_170,391,16)
    Text_170.inputPortByName['posx'].widget.set(0.25, run=False)
    Text_170.inputPortByName['posy'].widget.set(0.25, run=False)
    Text_170.inputPortByName['textlabel'].widget.set("left top", run=False)
    Text_170.inputPortByName['horizontalalignment'].widget.set("left", run=False)
    Text_170.inputPortByName['verticalalignment'].widget.set("top", run=False)
    apply(Text_170.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore Text named Text in network masterNet"
    print_exc()
    Text_170=None

try:
    ## saving node Text ##
    from Vision.matplotlibNodes import Text
    Text_171 = Text(constrkw = {}, name='Text', library=matplotliblib)
    masterNet.addNode(Text_171,542,165)
    Text_171.inputPortByName['posx'].widget.set(0.75, run=False)
    Text_171.inputPortByName['posy'].widget.set(0.75, run=False)
    Text_171.inputPortByName['textlabel'].widget.set("right top", run=False)
    Text_171.inputPortByName['horizontalalignment'].widget.set("right", run=False)
    Text_171.inputPortByName['verticalalignment'].widget.set("top", run=False)
    apply(Text_171.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore Text named Text in network masterNet"
    print_exc()
    Text_171=None

try:
    ## saving node Text ##
    from Vision.matplotlibNodes import Text
    Text_172 = Text(constrkw = {}, name='Text', library=matplotliblib)
    masterNet.addNode(Text_172,666,20)
    Text_172.inputPortByName['posx'].widget.set(0.25, run=False)
    Text_172.inputPortByName['posy'].widget.set(0.25, run=False)
    Text_172.inputPortByName['textlabel'].widget.set("left bottom", run=False)
    Text_172.inputPortByName['horizontalalignment'].widget.set("left", run=False)
    Text_172.inputPortByName['verticalalignment'].widget.set("bottom", run=False)
    apply(Text_172.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore Text named Text in network masterNet"
    print_exc()
    Text_172=None

try:
    ## saving node Text ##
    from Vision.matplotlibNodes import Text
    Text_173 = Text(constrkw = {}, name='Text', library=matplotliblib)
    masterNet.addNode(Text_173,947,21)
    Text_173.inputPortByName['posx'].widget.set(0.75, run=False)
    Text_173.inputPortByName['posy'].widget.set(0.75, run=False)
    Text_173.inputPortByName['textlabel'].widget.set("right bottom", run=False)
    Text_173.inputPortByName['horizontalalignment'].widget.set("right", run=False)
    Text_173.inputPortByName['verticalalignment'].widget.set("bottom", run=False)
    apply(Text_173.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore Text named Text in network masterNet"
    print_exc()
    Text_173=None

try:
    ## saving node Text ##
    from Vision.matplotlibNodes import Text
    Text_174 = Text(constrkw = {}, name='Text', library=matplotliblib)
    masterNet.addNode(Text_174,826,166)
    Text_174.inputPortByName['posx'].widget.set(0.75, run=False)
    Text_174.inputPortByName['posy'].widget.set(0.25, run=False)
    Text_174.inputPortByName['textlabel'].widget.set("center top", run=False)
    Text_174.inputPortByName['verticalalignment'].widget.set("top", run=False)
    apply(Text_174.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore Text named Text in network masterNet"
    print_exc()
    Text_174=None

try:
    ## saving node Text ##
    from Vision.matplotlibNodes import Text
    Text_175 = Text(constrkw = {}, name='Text', library=matplotliblib)
    masterNet.addNode(Text_175,481,319)
    Text_175.inputPortByName['posx'].widget.set(0.25, run=False)
    Text_175.inputPortByName['posy'].widget.set(0.5, run=False)
    Text_175.inputPortByName['textlabel'].widget.set("right center", run=False)
    Text_175.inputPortByName['rotation'].widget.set(90.0, run=False)
    Text_175.inputPortByName['horizontalalignment'].widget.set("right", run=False)
    apply(Text_175.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore Text named Text in network masterNet"
    print_exc()
    Text_175=None

try:
    ## saving node Text ##
    from Vision.matplotlibNodes import Text
    Text_176 = Text(constrkw = {}, name='Text', library=matplotliblib)
    masterNet.addNode(Text_176,766,324)
    Text_176.inputPortByName['posx'].widget.set(0.25, run=False)
    Text_176.inputPortByName['posy'].widget.set(0.5, run=False)
    Text_176.inputPortByName['textlabel'].widget.set("left center", run=False)
    Text_176.inputPortByName['rotation'].widget.set(90.0, run=False)
    Text_176.inputPortByName['horizontalalignment'].widget.set("left", run=False)
    apply(Text_176.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore Text named Text in network masterNet"
    print_exc()
    Text_176=None

try:
    ## saving node Text ##
    from Vision.matplotlibNodes import Text
    Text_177 = Text(constrkw = {}, name='Text', library=matplotliblib)
    masterNet.addNode(Text_177,1049,324)
    Text_177.inputPortByName['posx'].widget.set(0.5, run=False)
    Text_177.inputPortByName['posy'].widget.set(0.5, run=False)
    Text_177.inputPortByName['textlabel'].widget.set("middle", run=False)
    Text_177.inputPortByName['rotation'].widget.set(90.0, run=False)
    apply(Text_177.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore Text named Text in network masterNet"
    print_exc()
    Text_177=None

try:
    ## saving node Text ##
    from Vision.matplotlibNodes import Text
    Text_178 = Text(constrkw = {}, name='Text', library=matplotliblib)
    masterNet.addNode(Text_178,163,312)
    Text_178.inputPortByName['posx'].widget.set(0.25, run=False)
    Text_178.inputPortByName['posy'].widget.set(0.75, run=False)
    Text_178.inputPortByName['textlabel'].widget.set("rotated", run=False)
    Text_178.inputPortByName['rotation'].widget.set(45.0, run=False)
    apply(Text_178.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore Text named Text in network masterNet"
    print_exc()
    Text_178=None

try:
    ## saving node Text ##
    from Vision.matplotlibNodes import Text
    Text_179 = Text(constrkw = {}, name='Text', library=matplotliblib)
    masterNet.addNode(Text_179,1115,165)
    Text_179.inputPortByName['posx'].widget.set(0.75, run=False)
    Text_179.inputPortByName['posy'].widget.set(0.5, run=False)
    Text_179.inputPortByName['textlabel'].widget.set("centered", run=False)
    Text_179.inputPortByName['rotation'].widget.set(90.0, run=False)
    apply(Text_179.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore Text named Text in network masterNet"
    print_exc()
    Text_179=None

masterNet.freeze()

## saving connections for network TextAlign ##
if ReadTable_163 is not None and Index_164 is not None:
    try:
        masterNet.connectNodes(
            ReadTable_163, Index_164, "data", "data", blocking=True)
    except:
        print "WARNING: failed to restore connection between ReadTable_163 and Index_164 in network masterNet"
if ReadTable_163 is not None and Index_165 is not None:
    try:
        masterNet.connectNodes(
            ReadTable_163, Index_165, "data", "data", blocking=True)
    except:
        print "WARNING: failed to restore connection between ReadTable_163 and Index_165 in network masterNet"
if ReadTable_163 is not None and Index_166 is not None:
    try:
        masterNet.connectNodes(
            ReadTable_163, Index_166, "data", "data", blocking=True)
    except:
        print "WARNING: failed to restore connection between ReadTable_163 and Index_166 in network masterNet"
if ReadTable_163 is not None and Index_167 is not None:
    try:
        masterNet.connectNodes(
            ReadTable_163, Index_167, "data", "data", blocking=True)
    except:
        print "WARNING: failed to restore connection between ReadTable_163 and Index_167 in network masterNet"
if Index_164 is not None and BarH_162 is not None:
    try:
        masterNet.connectNodes(
            Index_164, BarH_162, "data", "bottom", blocking=True)
    except:
        print "WARNING: failed to restore connection between Index_164 and BarH_162 in network masterNet"
if Index_165 is not None and BarH_162 is not None:
    try:
        masterNet.connectNodes(
            Index_165, BarH_162, "data", "width", blocking=True)
    except:
        print "WARNING: failed to restore connection between Index_165 and BarH_162 in network masterNet"
if Draw_Area_168 is not None and BarH_162 is not None:
    try:
        masterNet.connectNodes(
            Draw_Area_168, BarH_162, "drawAreaDef", "drawAreaDef", blocking=True)
    except:
        print "WARNING: failed to restore connection between Draw_Area_168 and BarH_162 in network masterNet"
if Index_166 is not None and BarH_162 is not None:
    try:
        masterNet.connectNodes(
            Index_166, BarH_162, "data", "left", blocking=True)
    except:
        print "WARNING: failed to restore connection between Index_166 and BarH_162 in network masterNet"
if Index_167 is not None and BarH_162 is not None:
    try:
        masterNet.connectNodes(
            Index_167, BarH_162, "data", "height", blocking=True)
    except:
        print "WARNING: failed to restore connection between Index_167 and BarH_162 in network masterNet"
if Text_170 is not None and MergeText_169 is not None:
    try:
        masterNet.connectNodes(
            Text_170, MergeText_169, "drawAreaDef", "textlist", blocking=True)
    except:
        print "WARNING: failed to restore connection between Text_170 and MergeText_169 in network masterNet"
if Text_171 is not None and MergeText_169 is not None:
    try:
        masterNet.connectNodes(
            Text_171, MergeText_169, "drawAreaDef", "textlist", blocking=True)
    except:
        print "WARNING: failed to restore connection between Text_171 and MergeText_169 in network masterNet"
if Text_172 is not None and MergeText_169 is not None:
    try:
        masterNet.connectNodes(
            Text_172, MergeText_169, "drawAreaDef", "textlist", blocking=True)
    except:
        print "WARNING: failed to restore connection between Text_172 and MergeText_169 in network masterNet"
if Text_173 is not None and MergeText_169 is not None:
    try:
        masterNet.connectNodes(
            Text_173, MergeText_169, "drawAreaDef", "textlist", blocking=True)
    except:
        print "WARNING: failed to restore connection between Text_173 and MergeText_169 in network masterNet"
if Text_174 is not None and MergeText_169 is not None:
    try:
        masterNet.connectNodes(
            Text_174, MergeText_169, "drawAreaDef", "textlist", blocking=True)
    except:
        print "WARNING: failed to restore connection between Text_174 and MergeText_169 in network masterNet"
if Text_175 is not None and MergeText_169 is not None:
    try:
        masterNet.connectNodes(
            Text_175, MergeText_169, "drawAreaDef", "textlist", blocking=True)
    except:
        print "WARNING: failed to restore connection between Text_175 and MergeText_169 in network masterNet"
if Text_176 is not None and MergeText_169 is not None:
    try:
        masterNet.connectNodes(
            Text_176, MergeText_169, "drawAreaDef", "textlist", blocking=True)
    except:
        print "WARNING: failed to restore connection between Text_176 and MergeText_169 in network masterNet"
if Text_177 is not None and MergeText_169 is not None:
    try:
        masterNet.connectNodes(
            Text_177, MergeText_169, "drawAreaDef", "textlist", blocking=True)
    except:
        print "WARNING: failed to restore connection between Text_177 and MergeText_169 in network masterNet"
if MergeText_169 is not None and BarH_162 is not None:
    try:
        masterNet.connectNodes(
            MergeText_169, BarH_162, "drawAreaDef", "drawAreaDef", blocking=True)
    except:
        print "WARNING: failed to restore connection between MergeText_169 and BarH_162 in network masterNet"
if Text_178 is not None and MergeText_169 is not None:
    try:
        masterNet.connectNodes(
            Text_178, MergeText_169, "drawAreaDef", "textlist", blocking=True)
    except:
        print "WARNING: failed to restore connection between Text_178 and MergeText_169 in network masterNet"
if Text_179 is not None and MergeText_169 is not None:
    try:
        masterNet.connectNodes(
            Text_179, MergeText_169, "drawAreaDef", "textlist", blocking=True)
    except:
        print "WARNING: failed to restore connection between Text_179 and MergeText_169 in network masterNet"
masterNet.unfreeze()
#masterNet.run()

