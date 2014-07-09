# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.31
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _bhtreelib
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


findFaceSubset = _bhtreelib.findFaceSubset
class BHpoint(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BHpoint, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BHpoint, name)
    __repr__ = _swig_repr
    __swig_setmethods__["x"] = _bhtreelib.BHpoint_x_set
    __swig_getmethods__["x"] = _bhtreelib.BHpoint_x_get
    if _newclass:x = _swig_property(_bhtreelib.BHpoint_x_get, _bhtreelib.BHpoint_x_set)
    __swig_setmethods__["r"] = _bhtreelib.BHpoint_r_set
    __swig_getmethods__["r"] = _bhtreelib.BHpoint_r_get
    if _newclass:r = _swig_property(_bhtreelib.BHpoint_r_get, _bhtreelib.BHpoint_r_set)
    __swig_setmethods__["at"] = _bhtreelib.BHpoint_at_set
    __swig_getmethods__["at"] = _bhtreelib.BHpoint_at_get
    if _newclass:at = _swig_property(_bhtreelib.BHpoint_at_get, _bhtreelib.BHpoint_at_set)
    def __init__(self, *args): 
        this = _bhtreelib.new_BHpoint(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bhtreelib.delete_BHpoint
    __del__ = lambda self : None;
BHpoint_swigregister = _bhtreelib.BHpoint_swigregister
BHpoint_swigregister(BHpoint)

class BHnode(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BHnode, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BHnode, name)
    __repr__ = _swig_repr
    __swig_setmethods__["left"] = _bhtreelib.BHnode_left_set
    __swig_getmethods__["left"] = _bhtreelib.BHnode_left_get
    if _newclass:left = _swig_property(_bhtreelib.BHnode_left_get, _bhtreelib.BHnode_left_set)
    __swig_setmethods__["right"] = _bhtreelib.BHnode_right_set
    __swig_getmethods__["right"] = _bhtreelib.BHnode_right_get
    if _newclass:right = _swig_property(_bhtreelib.BHnode_right_get, _bhtreelib.BHnode_right_set)
    __swig_setmethods__["atom"] = _bhtreelib.BHnode_atom_set
    __swig_getmethods__["atom"] = _bhtreelib.BHnode_atom_get
    if _newclass:atom = _swig_property(_bhtreelib.BHnode_atom_get, _bhtreelib.BHnode_atom_set)
    __swig_setmethods__["cut"] = _bhtreelib.BHnode_cut_set
    __swig_getmethods__["cut"] = _bhtreelib.BHnode_cut_get
    if _newclass:cut = _swig_property(_bhtreelib.BHnode_cut_get, _bhtreelib.BHnode_cut_set)
    __swig_setmethods__["dim"] = _bhtreelib.BHnode_dim_set
    __swig_getmethods__["dim"] = _bhtreelib.BHnode_dim_get
    if _newclass:dim = _swig_property(_bhtreelib.BHnode_dim_get, _bhtreelib.BHnode_dim_set)
    __swig_setmethods__["n"] = _bhtreelib.BHnode_n_set
    __swig_getmethods__["n"] = _bhtreelib.BHnode_n_get
    if _newclass:n = _swig_property(_bhtreelib.BHnode_n_get, _bhtreelib.BHnode_n_set)
    def __init__(self, *args): 
        this = _bhtreelib.new_BHnode(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bhtreelib.delete_BHnode
    __del__ = lambda self : None;
BHnode_swigregister = _bhtreelib.BHnode_swigregister
BHnode_swigregister(BHnode)

class BHtree(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BHtree, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BHtree, name)
    __repr__ = _swig_repr
    __swig_setmethods__["root"] = _bhtreelib.BHtree_root_set
    __swig_getmethods__["root"] = _bhtreelib.BHtree_root_get
    if _newclass:root = _swig_property(_bhtreelib.BHtree_root_get, _bhtreelib.BHtree_root_set)
    __swig_setmethods__["atom"] = _bhtreelib.BHtree_atom_set
    __swig_getmethods__["atom"] = _bhtreelib.BHtree_atom_get
    if _newclass:atom = _swig_property(_bhtreelib.BHtree_atom_get, _bhtreelib.BHtree_atom_set)
    __swig_setmethods__["xmin"] = _bhtreelib.BHtree_xmin_set
    __swig_getmethods__["xmin"] = _bhtreelib.BHtree_xmin_get
    if _newclass:xmin = _swig_property(_bhtreelib.BHtree_xmin_get, _bhtreelib.BHtree_xmin_set)
    __swig_setmethods__["xmax"] = _bhtreelib.BHtree_xmax_set
    __swig_getmethods__["xmax"] = _bhtreelib.BHtree_xmax_get
    if _newclass:xmax = _swig_property(_bhtreelib.BHtree_xmax_get, _bhtreelib.BHtree_xmax_set)
    __swig_setmethods__["maxr"] = _bhtreelib.BHtree_maxr_set
    __swig_getmethods__["maxr"] = _bhtreelib.BHtree_maxr_get
    if _newclass:maxr = _swig_property(_bhtreelib.BHtree_maxr_get, _bhtreelib.BHtree_maxr_set)
    __swig_setmethods__["rm"] = _bhtreelib.BHtree_rm_set
    __swig_getmethods__["rm"] = _bhtreelib.BHtree_rm_get
    if _newclass:rm = _swig_property(_bhtreelib.BHtree_rm_get, _bhtreelib.BHtree_rm_set)
    __swig_setmethods__["nodeLookUp"] = _bhtreelib.BHtree_nodeLookUp_set
    __swig_getmethods__["nodeLookUp"] = _bhtreelib.BHtree_nodeLookUp_get
    if _newclass:nodeLookUp = _swig_property(_bhtreelib.BHtree_nodeLookUp_get, _bhtreelib.BHtree_nodeLookUp_set)
    __swig_setmethods__["nbp"] = _bhtreelib.BHtree_nbp_set
    __swig_getmethods__["nbp"] = _bhtreelib.BHtree_nbp_get
    if _newclass:nbp = _swig_property(_bhtreelib.BHtree_nbp_get, _bhtreelib.BHtree_nbp_set)
    __swig_setmethods__["bfl"] = _bhtreelib.BHtree_bfl_set
    __swig_getmethods__["bfl"] = _bhtreelib.BHtree_bfl_get
    if _newclass:bfl = _swig_property(_bhtreelib.BHtree_bfl_get, _bhtreelib.BHtree_bfl_set)
    def __init__(self, *args): 
        this = _bhtreelib.new_BHtree(*args)
        try: self.this.append(this)
        except: self.this = this
    def closePoints(*args): return _bhtreelib.BHtree_closePoints(*args)
    def closePointsDist(*args): return _bhtreelib.BHtree_closePointsDist(*args)
    def closePointsDist2(*args): return _bhtreelib.BHtree_closePointsDist2(*args)
    def closePointsPairsInTree(*args): return _bhtreelib.BHtree_closePointsPairsInTree(*args)
    def closePointsPairs(*args): return _bhtreelib.BHtree_closePointsPairs(*args)
    def closestPointsArray(*args): return _bhtreelib.BHtree_closestPointsArray(*args)
    def closestPointsArrayDist2(*args): return _bhtreelib.BHtree_closestPointsArrayDist2(*args)
    __swig_destroy__ = _bhtreelib.delete_BHtree
    __del__ = lambda self : None;
BHtree_swigregister = _bhtreelib.BHtree_swigregister
BHtree_swigregister(BHtree)

generateBHtree = _bhtreelib.generateBHtree
findBHnode = _bhtreelib.findBHnode
findBHcloseAtoms = _bhtreelib.findBHcloseAtoms
findBHcloseAtomsdist = _bhtreelib.findBHcloseAtomsdist
findBHcloseAtomsdist2 = _bhtreelib.findBHcloseAtomsdist2
freeBHtree = _bhtreelib.freeBHtree
divideBHnode = _bhtreelib.divideBHnode
freeBHnode = _bhtreelib.freeBHnode
findClosePairsInTree = _bhtreelib.findClosePairsInTree
findClosePairs = _bhtreelib.findClosePairs
findClosestAtoms = _bhtreelib.findClosestAtoms
findClosestAtomsDist2 = _bhtreelib.findClosestAtomsDist2
BH_MAXFINDCOUNT = _bhtreelib.BH_MAXFINDCOUNT
BH_FINDCOUNT = _bhtreelib.BH_FINDCOUNT
BH_MAXBOX = _bhtreelib.BH_MAXBOX
BH_PADDING = _bhtreelib.BH_PADDING
BH_SEARCH_UP = _bhtreelib.BH_SEARCH_UP
BH_SEARCH_DOWN = _bhtreelib.BH_SEARCH_DOWN
RBH_INSERTPADDING = _bhtreelib.RBH_INSERTPADDING
RBH_DELETEPADDING = _bhtreelib.RBH_DELETEPADDING
RBH_SPACEPADDING = _bhtreelib.RBH_SPACEPADDING
BH_LARGE_SPACE_PADDING = _bhtreelib.BH_LARGE_SPACE_PADDING
BH_LEAFPADDING = _bhtreelib.BH_LEAFPADDING
BH_OUTSIDE_TREE = _bhtreelib.BH_OUTSIDE_TREE
BH_FILLED_PADDING = _bhtreelib.BH_FILLED_PADDING
BH_EMPTY_BOX = _bhtreelib.BH_EMPTY_BOX
BH_ALREADY_DELETED = _bhtreelib.BH_ALREADY_DELETED
BH_INVALID_POINT = _bhtreelib.BH_INVALID_POINT
BH_MEMORY_ERROR = _bhtreelib.BH_MEMORY_ERROR
BH_X = _bhtreelib.BH_X
BH_Y = _bhtreelib.BH_Y
BH_Z = _bhtreelib.BH_Z
BH_YES = _bhtreelib.BH_YES
BH_NO = _bhtreelib.BH_NO
NSTEPS = _bhtreelib.NSTEPS
FLAG_OWNSMEMORY = _bhtreelib.FLAG_OWNSMEMORY
FLAG_EMPTY_TREE = _bhtreelib.FLAG_EMPTY_TREE
class TBHPoint(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TBHPoint, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TBHPoint, name)
    __repr__ = _swig_repr
    __swig_setmethods__["Pos"] = _bhtreelib.TBHPoint_Pos_set
    __swig_getmethods__["Pos"] = _bhtreelib.TBHPoint_Pos_get
    if _newclass:Pos = _swig_property(_bhtreelib.TBHPoint_Pos_get, _bhtreelib.TBHPoint_Pos_set)
    __swig_setmethods__["Rad"] = _bhtreelib.TBHPoint_Rad_set
    __swig_getmethods__["Rad"] = _bhtreelib.TBHPoint_Rad_get
    if _newclass:Rad = _swig_property(_bhtreelib.TBHPoint_Rad_get, _bhtreelib.TBHPoint_Rad_set)
    __swig_setmethods__["Data"] = _bhtreelib.TBHPoint_Data_set
    __swig_getmethods__["Data"] = _bhtreelib.TBHPoint_Data_get
    if _newclass:Data = _swig_property(_bhtreelib.TBHPoint_Data_get, _bhtreelib.TBHPoint_Data_set)
    __swig_setmethods__["uInt"] = _bhtreelib.TBHPoint_uInt_set
    __swig_getmethods__["uInt"] = _bhtreelib.TBHPoint_uInt_get
    if _newclass:uInt = _swig_property(_bhtreelib.TBHPoint_uInt_get, _bhtreelib.TBHPoint_uInt_set)
    __swig_setmethods__["ID"] = _bhtreelib.TBHPoint_ID_set
    __swig_getmethods__["ID"] = _bhtreelib.TBHPoint_ID_get
    if _newclass:ID = _swig_property(_bhtreelib.TBHPoint_ID_get, _bhtreelib.TBHPoint_ID_set)
    __swig_setmethods__["Box"] = _bhtreelib.TBHPoint_Box_set
    __swig_getmethods__["Box"] = _bhtreelib.TBHPoint_Box_get
    if _newclass:Box = _swig_property(_bhtreelib.TBHPoint_Box_get, _bhtreelib.TBHPoint_Box_set)
    def __init__(self, *args): 
        this = _bhtreelib.new_TBHPoint(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bhtreelib.delete_TBHPoint
    __del__ = lambda self : None;
TBHPoint_swigregister = _bhtreelib.TBHPoint_swigregister
TBHPoint_swigregister(TBHPoint)

class TBHIndex(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TBHIndex, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TBHIndex, name)
    __repr__ = _swig_repr
    __swig_setmethods__["Pts"] = _bhtreelib.TBHIndex_Pts_set
    __swig_getmethods__["Pts"] = _bhtreelib.TBHIndex_Pts_get
    if _newclass:Pts = _swig_property(_bhtreelib.TBHIndex_Pts_get, _bhtreelib.TBHIndex_Pts_set)
    __swig_setmethods__["NumPts"] = _bhtreelib.TBHIndex_NumPts_set
    __swig_getmethods__["NumPts"] = _bhtreelib.TBHIndex_NumPts_get
    if _newclass:NumPts = _swig_property(_bhtreelib.TBHIndex_NumPts_get, _bhtreelib.TBHIndex_NumPts_set)
    __swig_setmethods__["Size"] = _bhtreelib.TBHIndex_Size_set
    __swig_getmethods__["Size"] = _bhtreelib.TBHIndex_Size_get
    if _newclass:Size = _swig_property(_bhtreelib.TBHIndex_Size_get, _bhtreelib.TBHIndex_Size_set)
    def __init__(self, *args): 
        this = _bhtreelib.new_TBHIndex(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bhtreelib.delete_TBHIndex
    __del__ = lambda self : None;
TBHIndex_swigregister = _bhtreelib.TBHIndex_swigregister
TBHIndex_swigregister(TBHIndex)

class TBHNode(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TBHNode, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TBHNode, name)
    __repr__ = _swig_repr
    __swig_setmethods__["Left"] = _bhtreelib.TBHNode_Left_set
    __swig_getmethods__["Left"] = _bhtreelib.TBHNode_Left_get
    if _newclass:Left = _swig_property(_bhtreelib.TBHNode_Left_get, _bhtreelib.TBHNode_Left_set)
    __swig_setmethods__["Right"] = _bhtreelib.TBHNode_Right_set
    __swig_getmethods__["Right"] = _bhtreelib.TBHNode_Right_get
    if _newclass:Right = _swig_property(_bhtreelib.TBHNode_Right_get, _bhtreelib.TBHNode_Right_set)
    __swig_setmethods__["Parent"] = _bhtreelib.TBHNode_Parent_set
    __swig_getmethods__["Parent"] = _bhtreelib.TBHNode_Parent_get
    if _newclass:Parent = _swig_property(_bhtreelib.TBHNode_Parent_get, _bhtreelib.TBHNode_Parent_set)
    __swig_setmethods__["Buffer"] = _bhtreelib.TBHNode_Buffer_set
    __swig_getmethods__["Buffer"] = _bhtreelib.TBHNode_Buffer_get
    if _newclass:Buffer = _swig_property(_bhtreelib.TBHNode_Buffer_get, _bhtreelib.TBHNode_Buffer_set)
    __swig_setmethods__["Index"] = _bhtreelib.TBHNode_Index_set
    __swig_getmethods__["Index"] = _bhtreelib.TBHNode_Index_get
    if _newclass:Index = _swig_property(_bhtreelib.TBHNode_Index_get, _bhtreelib.TBHNode_Index_set)
    __swig_setmethods__["xmin"] = _bhtreelib.TBHNode_xmin_set
    __swig_getmethods__["xmin"] = _bhtreelib.TBHNode_xmin_get
    if _newclass:xmin = _swig_property(_bhtreelib.TBHNode_xmin_get, _bhtreelib.TBHNode_xmin_set)
    __swig_setmethods__["xmax"] = _bhtreelib.TBHNode_xmax_set
    __swig_getmethods__["xmax"] = _bhtreelib.TBHNode_xmax_get
    if _newclass:xmax = _swig_property(_bhtreelib.TBHNode_xmax_get, _bhtreelib.TBHNode_xmax_set)
    __swig_setmethods__["cut"] = _bhtreelib.TBHNode_cut_set
    __swig_getmethods__["cut"] = _bhtreelib.TBHNode_cut_get
    if _newclass:cut = _swig_property(_bhtreelib.TBHNode_cut_get, _bhtreelib.TBHNode_cut_set)
    __swig_setmethods__["dim"] = _bhtreelib.TBHNode_dim_set
    __swig_getmethods__["dim"] = _bhtreelib.TBHNode_dim_get
    if _newclass:dim = _swig_property(_bhtreelib.TBHNode_dim_get, _bhtreelib.TBHNode_dim_set)
    def __init__(self, *args): 
        this = _bhtreelib.new_TBHNode(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bhtreelib.delete_TBHNode
    __del__ = lambda self : None;
TBHNode_swigregister = _bhtreelib.TBHNode_swigregister
TBHNode_swigregister(TBHNode)

class TBHTree(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TBHTree, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TBHTree, name)
    __repr__ = _swig_repr
    __swig_setmethods__["Root"] = _bhtreelib.TBHTree_Root_set
    __swig_getmethods__["Root"] = _bhtreelib.TBHTree_Root_get
    if _newclass:Root = _swig_property(_bhtreelib.TBHTree_Root_get, _bhtreelib.TBHTree_Root_set)
    __swig_setmethods__["Pts"] = _bhtreelib.TBHTree_Pts_set
    __swig_getmethods__["Pts"] = _bhtreelib.TBHTree_Pts_get
    if _newclass:Pts = _swig_property(_bhtreelib.TBHTree_Pts_get, _bhtreelib.TBHTree_Pts_set)
    __swig_setmethods__["NumPts"] = _bhtreelib.TBHTree_NumPts_set
    __swig_getmethods__["NumPts"] = _bhtreelib.TBHTree_NumPts_get
    if _newclass:NumPts = _swig_property(_bhtreelib.TBHTree_NumPts_get, _bhtreelib.TBHTree_NumPts_set)
    __swig_setmethods__["xmin"] = _bhtreelib.TBHTree_xmin_set
    __swig_getmethods__["xmin"] = _bhtreelib.TBHTree_xmin_get
    if _newclass:xmin = _swig_property(_bhtreelib.TBHTree_xmin_get, _bhtreelib.TBHTree_xmin_set)
    __swig_setmethods__["xmax"] = _bhtreelib.TBHTree_xmax_set
    __swig_getmethods__["xmax"] = _bhtreelib.TBHTree_xmax_get
    if _newclass:xmax = _swig_property(_bhtreelib.TBHTree_xmax_get, _bhtreelib.TBHTree_xmax_set)
    __swig_setmethods__["rm"] = _bhtreelib.TBHTree_rm_set
    __swig_getmethods__["rm"] = _bhtreelib.TBHTree_rm_get
    if _newclass:rm = _swig_property(_bhtreelib.TBHTree_rm_get, _bhtreelib.TBHTree_rm_set)
    __swig_setmethods__["bfl"] = _bhtreelib.TBHTree_bfl_set
    __swig_getmethods__["bfl"] = _bhtreelib.TBHTree_bfl_get
    if _newclass:bfl = _swig_property(_bhtreelib.TBHTree_bfl_get, _bhtreelib.TBHTree_bfl_set)
    def __init__(self, *args): 
        this = _bhtreelib.new_TBHTree(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bhtreelib.delete_TBHTree
    __del__ = lambda self : None;
    def ClosePoints(*args): return _bhtreelib.TBHTree_ClosePoints(*args)
    def ClosePointsDist2(*args): return _bhtreelib.TBHTree_ClosePointsDist2(*args)
TBHTree_swigregister = _bhtreelib.TBHTree_swigregister
TBHTree_swigregister(TBHTree)

class RBHTree(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RBHTree, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RBHTree, name)
    __repr__ = _swig_repr
    __swig_setmethods__["Root"] = _bhtreelib.RBHTree_Root_set
    __swig_getmethods__["Root"] = _bhtreelib.RBHTree_Root_get
    if _newclass:Root = _swig_property(_bhtreelib.RBHTree_Root_get, _bhtreelib.RBHTree_Root_set)
    __swig_setmethods__["Pts"] = _bhtreelib.RBHTree_Pts_set
    __swig_getmethods__["Pts"] = _bhtreelib.RBHTree_Pts_get
    if _newclass:Pts = _swig_property(_bhtreelib.RBHTree_Pts_get, _bhtreelib.RBHTree_Pts_set)
    __swig_setmethods__["FreePts"] = _bhtreelib.RBHTree_FreePts_set
    __swig_getmethods__["FreePts"] = _bhtreelib.RBHTree_FreePts_get
    if _newclass:FreePts = _swig_property(_bhtreelib.RBHTree_FreePts_get, _bhtreelib.RBHTree_FreePts_set)
    __swig_setmethods__["NumPts"] = _bhtreelib.RBHTree_NumPts_set
    __swig_getmethods__["NumPts"] = _bhtreelib.RBHTree_NumPts_get
    if _newclass:NumPts = _swig_property(_bhtreelib.RBHTree_NumPts_get, _bhtreelib.RBHTree_NumPts_set)
    __swig_setmethods__["SizePts"] = _bhtreelib.RBHTree_SizePts_set
    __swig_getmethods__["SizePts"] = _bhtreelib.RBHTree_SizePts_get
    if _newclass:SizePts = _swig_property(_bhtreelib.RBHTree_SizePts_get, _bhtreelib.RBHTree_SizePts_set)
    __swig_setmethods__["xmin"] = _bhtreelib.RBHTree_xmin_set
    __swig_getmethods__["xmin"] = _bhtreelib.RBHTree_xmin_get
    if _newclass:xmin = _swig_property(_bhtreelib.RBHTree_xmin_get, _bhtreelib.RBHTree_xmin_set)
    __swig_setmethods__["xmax"] = _bhtreelib.RBHTree_xmax_set
    __swig_getmethods__["xmax"] = _bhtreelib.RBHTree_xmax_get
    if _newclass:xmax = _swig_property(_bhtreelib.RBHTree_xmax_get, _bhtreelib.RBHTree_xmax_set)
    __swig_setmethods__["rm"] = _bhtreelib.RBHTree_rm_set
    __swig_getmethods__["rm"] = _bhtreelib.RBHTree_rm_get
    if _newclass:rm = _swig_property(_bhtreelib.RBHTree_rm_get, _bhtreelib.RBHTree_rm_set)
    __swig_setmethods__["bfl"] = _bhtreelib.RBHTree_bfl_set
    __swig_getmethods__["bfl"] = _bhtreelib.RBHTree_bfl_get
    if _newclass:bfl = _swig_property(_bhtreelib.RBHTree_bfl_get, _bhtreelib.RBHTree_bfl_set)
    __swig_setmethods__["Flags"] = _bhtreelib.RBHTree_Flags_set
    __swig_getmethods__["Flags"] = _bhtreelib.RBHTree_Flags_get
    if _newclass:Flags = _swig_property(_bhtreelib.RBHTree_Flags_get, _bhtreelib.RBHTree_Flags_set)
    __swig_setmethods__["Granularity"] = _bhtreelib.RBHTree_Granularity_set
    __swig_getmethods__["Granularity"] = _bhtreelib.RBHTree_Granularity_get
    if _newclass:Granularity = _swig_property(_bhtreelib.RBHTree_Granularity_get, _bhtreelib.RBHTree_Granularity_set)
    __swig_setmethods__["LeafPadding"] = _bhtreelib.RBHTree_LeafPadding_set
    __swig_getmethods__["LeafPadding"] = _bhtreelib.RBHTree_LeafPadding_get
    if _newclass:LeafPadding = _swig_property(_bhtreelib.RBHTree_LeafPadding_get, _bhtreelib.RBHTree_LeafPadding_set)
    __swig_setmethods__["SpacePadding"] = _bhtreelib.RBHTree_SpacePadding_set
    __swig_getmethods__["SpacePadding"] = _bhtreelib.RBHTree_SpacePadding_get
    if _newclass:SpacePadding = _swig_property(_bhtreelib.RBHTree_SpacePadding_get, _bhtreelib.RBHTree_SpacePadding_set)
    def __init__(self, *args): 
        this = _bhtreelib.new_RBHTree(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bhtreelib.delete_RBHTree
    __del__ = lambda self : None;
    def ClosePoints(*args): return _bhtreelib.RBHTree_ClosePoints(*args)
    def ClosePointsDist2(*args): return _bhtreelib.RBHTree_ClosePointsDist2(*args)
    def InsertRBHPoint(*args): return _bhtreelib.RBHTree_InsertRBHPoint(*args)
    def DeleteRBHPoint(*args): return _bhtreelib.RBHTree_DeleteRBHPoint(*args)
    def MoveRBHPoint(*args): return _bhtreelib.RBHTree_MoveRBHPoint(*args)
RBHTree_swigregister = _bhtreelib.RBHTree_swigregister
RBHTree_swigregister(RBHTree)

GenerateTBHTree = _bhtreelib.GenerateTBHTree
FindTBHNodeUp = _bhtreelib.FindTBHNodeUp
FindTBHNode = _bhtreelib.FindTBHNode
FreeTBHTree = _bhtreelib.FreeTBHTree
FreeTBHNode = _bhtreelib.FreeTBHNode
MoveTBHPoint = _bhtreelib.MoveTBHPoint
DivideTBHNode = _bhtreelib.DivideTBHNode
FindTBHCloseAtomsDist = _bhtreelib.FindTBHCloseAtomsDist
FindTBHCloseAtomsInNodeDist = _bhtreelib.FindTBHCloseAtomsInNodeDist
FindTBHCloseAtoms = _bhtreelib.FindTBHCloseAtoms
FindTBHCloseAtomsInNode = _bhtreelib.FindTBHCloseAtomsInNode
ModifyBHPoint = _bhtreelib.ModifyBHPoint
GenerateRBHTree = _bhtreelib.GenerateRBHTree
FindRBHNode = _bhtreelib.FindRBHNode
FreeRBHTree = _bhtreelib.FreeRBHTree
InsertRBHPoint = _bhtreelib.InsertRBHPoint
DeleteRBHPoint = _bhtreelib.DeleteRBHPoint
MoveRBHPoint = _bhtreelib.MoveRBHPoint
ModifyRBHPoint = _bhtreelib.ModifyRBHPoint
FindRBHCloseAtomsDist = _bhtreelib.FindRBHCloseAtomsDist
FindRBHCloseAtoms = _bhtreelib.FindRBHCloseAtoms


