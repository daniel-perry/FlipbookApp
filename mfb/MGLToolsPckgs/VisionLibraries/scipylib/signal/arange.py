########################################################################
#
#    Vision Node - Python source code - file generated by vision
#    Thursday 08 November 2007 10:33:01 
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
# $Header: /opt/cvs/VisionLibraries/scipylib/signal/arange.py,v 1.1 2007/11/28 23:09:08 mgltools Exp $
#
# $Id: arange.py,v 1.1 2007/11/28 23:09:08 mgltools Exp $
#

# import node's base class node
from NetworkEditor.items import NetworkNode
class arange(NetworkNode):
    mRequiredTypes = {}
    mRequiredSynonyms = [
    ]
    def __init__(self, constrkw = {},  name='arange', **kw):
        kw['constrkw'] = constrkw
        kw['name'] = name
        apply( NetworkNode.__init__, (self,), kw)
        code = """def doit(self, in0, in1,in2):
    import scipy
    data=scipy.arange(in0,in1,in2)
    self.outputData(out0=data)
"""
        self.configure(function=code)
        self.inputPortsDescr.append(
            {'singleConnection': True, 'name': 'in0', 'cast': True, 'datatype': 'float', 'required': True, 'height': 8, 'width': 12, 'shape': 'circle', 'color': 'green', 'originalDatatype': 'None'})
        self.inputPortsDescr.append(
            {'singleConnection': True, 'name': 'in1', 'cast': True, 'datatype': 'float', 'required': True, 'height': 8, 'width': 12, 'shape': 'circle', 'color': 'green', 'originalDatatype': 'None'})
        self.inputPortsDescr.append(
            {'singleConnection': True, 'name': 'in2', 'cast': True, 'datatype': 'float', 'required': True, 'height': 8, 'width': 12, 'shape': 'circle', 'color': 'green', 'originalDatatype': 'None'})
        self.outputPortsDescr.append(
            {'name': 'out0', 'datatype': 'None', 'height': 8, 'width': 12, 'shape': 'diamond', 'color': 'white'})
        self.widgetDescr['in0'] = {
            'initialValue': 0.0, 'widgetGridCfgnode': {'rowspan': 1, 'labelSide': 'left', 'column': 1, 'ipady': 0, 'ipadx': 0, 'columnspan': 1, 'pady': 0, 'padx': 0, 'row': 0}, 'increment':0.1, 'height': 20, 'labelGridCfg': {'rowspan': 1, 'column': 0, 'sticky': 'w', 'ipady': 0, 'ipadx': 0, 'columnspan': 1, 'pady': 0, 'padx': 0, 'row': 0}, 'width': 60, 'master': 'node', 'wheelPad': 1, 'widgetGridCfg': {'column': 1, 'labelSide': 'left', 'row': 0}, 'labelCfg': {'text': 'in0'}, 'class': 'NEThumbWheel', 'oneTurn': 10.0}
        self.widgetDescr['in1'] = {
            'initialValue': 1.0, 'widgetGridCfgnode': {'rowspan': 1, 'labelSide': 'left', 'column': 1, 'ipady': 0, 'ipadx': 0, 'columnspan': 1, 'pady': 0, 'padx': 0, 'row': 1}, 'increment':0.1, 'height': 20, 'labelGridCfg': {'rowspan': 1, 'column': 0, 'sticky': 'w', 'ipady': 0, 'ipadx': 0, 'columnspan': 1, 'pady': 0, 'padx': 0, 'row': 1}, 'width': 60, 'master': 'node', 'wheelPad': 1, 'widgetGridCfg': {'column': 1, 'labelSide': 'left', 'row': 0}, 'labelCfg': {'text': 'in1'}, 'class': 'NEThumbWheel', 'oneTurn': 10.0}
        self.widgetDescr['in2'] = {
            'initialValue': 0.1, 'widgetGridCfgnode': {'rowspan': 1, 'labelSide': 'left', 'column': 1, 'ipady': 0, 'ipadx': 0, 'columnspan': 1, 'pady': 0, 'padx': 0, 'row': 2},'increment':0.1, 'height': 20, 'labelGridCfg': {'rowspan': 1, 'column': 0, 'sticky': 'w', 'ipady': 0, 'ipadx': 0, 'columnspan': 1, 'pady': 0, 'padx': 0, 'row': 2}, 'width': 60, 'master': 'node', 'wheelPad': 1, 'widgetGridCfg': {'column': 1, 'labelSide': 'left', 'row': 0}, 'labelCfg': {'text': 'in2'}, 'class': 'NEThumbWheel', 'oneTurn': 10.0}


    def beforeAddingToNetwork(self, net):
        try:
            ed = net.getEditor()
        except:
            import traceback; traceback.print_exc()
            print 'Warning! Could not import widgets'

