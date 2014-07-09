# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.9
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_isocontour', [dirname(__file__)])
        except ImportError:
            import _isocontour
            return _isocontour
        if fp is not None:
            try:
                _mod = imp.load_module('_isocontour', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _isocontour = swig_import_helper()
    del swig_import_helper
else:
    import _isocontour
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


CONTOUR_UCHAR = _isocontour.CONTOUR_UCHAR
CONTOUR_USHORT = _isocontour.CONTOUR_USHORT
CONTOUR_FLOAT = _isocontour.CONTOUR_FLOAT
CONTOUR_2D = _isocontour.CONTOUR_2D
CONTOUR_3D = _isocontour.CONTOUR_3D
CONTOUR_REG_2D = _isocontour.CONTOUR_REG_2D
CONTOUR_REG_3D = _isocontour.CONTOUR_REG_3D
NO_COLOR_VARIABLE = _isocontour.NO_COLOR_VARIABLE
class DatasetInfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DatasetInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DatasetInfo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["datatype"] = _isocontour.DatasetInfo_datatype_set
    __swig_getmethods__["datatype"] = _isocontour.DatasetInfo_datatype_get
    if _newclass:datatype = _swig_property(_isocontour.DatasetInfo_datatype_get, _isocontour.DatasetInfo_datatype_set)
    __swig_setmethods__["meshtype"] = _isocontour.DatasetInfo_meshtype_set
    __swig_getmethods__["meshtype"] = _isocontour.DatasetInfo_meshtype_get
    if _newclass:meshtype = _swig_property(_isocontour.DatasetInfo_meshtype_get, _isocontour.DatasetInfo_meshtype_set)
    __swig_setmethods__["nvars"] = _isocontour.DatasetInfo_nvars_set
    __swig_getmethods__["nvars"] = _isocontour.DatasetInfo_nvars_get
    if _newclass:nvars = _swig_property(_isocontour.DatasetInfo_nvars_get, _isocontour.DatasetInfo_nvars_set)
    __swig_setmethods__["ntime"] = _isocontour.DatasetInfo_ntime_set
    __swig_getmethods__["ntime"] = _isocontour.DatasetInfo_ntime_get
    if _newclass:ntime = _swig_property(_isocontour.DatasetInfo_ntime_get, _isocontour.DatasetInfo_ntime_set)
    __swig_setmethods__["dim"] = _isocontour.DatasetInfo_dim_set
    __swig_getmethods__["dim"] = _isocontour.DatasetInfo_dim_get
    if _newclass:dim = _swig_property(_isocontour.DatasetInfo_dim_get, _isocontour.DatasetInfo_dim_set)
    __swig_setmethods__["orig"] = _isocontour.DatasetInfo_orig_set
    __swig_getmethods__["orig"] = _isocontour.DatasetInfo_orig_get
    if _newclass:orig = _swig_property(_isocontour.DatasetInfo_orig_get, _isocontour.DatasetInfo_orig_set)
    __swig_setmethods__["span"] = _isocontour.DatasetInfo_span_set
    __swig_getmethods__["span"] = _isocontour.DatasetInfo_span_get
    if _newclass:span = _swig_property(_isocontour.DatasetInfo_span_get, _isocontour.DatasetInfo_span_set)
    __swig_setmethods__["minext"] = _isocontour.DatasetInfo_minext_set
    __swig_getmethods__["minext"] = _isocontour.DatasetInfo_minext_get
    if _newclass:minext = _swig_property(_isocontour.DatasetInfo_minext_get, _isocontour.DatasetInfo_minext_set)
    __swig_setmethods__["maxext"] = _isocontour.DatasetInfo_maxext_set
    __swig_getmethods__["maxext"] = _isocontour.DatasetInfo_maxext_get
    if _newclass:maxext = _swig_property(_isocontour.DatasetInfo_maxext_get, _isocontour.DatasetInfo_maxext_set)
    __swig_setmethods__["minvar"] = _isocontour.DatasetInfo_minvar_set
    __swig_getmethods__["minvar"] = _isocontour.DatasetInfo_minvar_get
    if _newclass:minvar = _swig_property(_isocontour.DatasetInfo_minvar_get, _isocontour.DatasetInfo_minvar_set)
    __swig_setmethods__["maxvar"] = _isocontour.DatasetInfo_maxvar_set
    __swig_getmethods__["maxvar"] = _isocontour.DatasetInfo_maxvar_get
    if _newclass:maxvar = _swig_property(_isocontour.DatasetInfo_maxvar_get, _isocontour.DatasetInfo_maxvar_set)
    def _dim(self) -> "void" : return _isocontour.DatasetInfo__dim(self)
    def _orig(self) -> "void" : return _isocontour.DatasetInfo__orig(self)
    def _span(self) -> "void" : return _isocontour.DatasetInfo__span(self)
    def _minext(self) -> "void" : return _isocontour.DatasetInfo__minext(self)
    def _maxext(self) -> "void" : return _isocontour.DatasetInfo__maxext(self)
    def __init__(self): 
        this = _isocontour.new_DatasetInfo()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _isocontour.delete_DatasetInfo
    __del__ = lambda self : None;
DatasetInfo_swigregister = _isocontour.DatasetInfo_swigregister
DatasetInfo_swigregister(DatasetInfo)

class Seed(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Seed, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Seed, name)
    __repr__ = _swig_repr
    __swig_setmethods__["min"] = _isocontour.Seed_min_set
    __swig_getmethods__["min"] = _isocontour.Seed_min_get
    if _newclass:min = _swig_property(_isocontour.Seed_min_get, _isocontour.Seed_min_set)
    __swig_setmethods__["max"] = _isocontour.Seed_max_set
    __swig_getmethods__["max"] = _isocontour.Seed_max_get
    if _newclass:max = _swig_property(_isocontour.Seed_max_get, _isocontour.Seed_max_set)
    __swig_setmethods__["cell_id"] = _isocontour.Seed_cell_id_set
    __swig_getmethods__["cell_id"] = _isocontour.Seed_cell_id_get
    if _newclass:cell_id = _swig_property(_isocontour.Seed_cell_id_get, _isocontour.Seed_cell_id_set)
    def __init__(self): 
        this = _isocontour.new_Seed()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _isocontour.delete_Seed
    __del__ = lambda self : None;
Seed_swigregister = _isocontour.Seed_swigregister
Seed_swigregister(Seed)

class SeedData(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SeedData, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SeedData, name)
    __repr__ = _swig_repr
    __swig_setmethods__["nseeds"] = _isocontour.SeedData_nseeds_set
    __swig_getmethods__["nseeds"] = _isocontour.SeedData_nseeds_get
    if _newclass:nseeds = _swig_property(_isocontour.SeedData_nseeds_get, _isocontour.SeedData_nseeds_set)
    __swig_setmethods__["seeds"] = _isocontour.SeedData_seeds_set
    __swig_getmethods__["seeds"] = _isocontour.SeedData_seeds_get
    if _newclass:seeds = _swig_property(_isocontour.SeedData_seeds_get, _isocontour.SeedData_seeds_set)
    def __init__(self): 
        this = _isocontour.new_SeedData()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _isocontour.delete_SeedData
    __del__ = lambda self : None;
SeedData_swigregister = _isocontour.SeedData_swigregister
SeedData_swigregister(SeedData)

class Signature(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Signature, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Signature, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _isocontour.Signature_name_set
    __swig_getmethods__["name"] = _isocontour.Signature_name_get
    if _newclass:name = _swig_property(_isocontour.Signature_name_get, _isocontour.Signature_name_set)
    __swig_setmethods__["nval"] = _isocontour.Signature_nval_set
    __swig_getmethods__["nval"] = _isocontour.Signature_nval_get
    if _newclass:nval = _swig_property(_isocontour.Signature_nval_get, _isocontour.Signature_nval_set)
    __swig_setmethods__["fx"] = _isocontour.Signature_fx_set
    __swig_getmethods__["fx"] = _isocontour.Signature_fx_get
    if _newclass:fx = _swig_property(_isocontour.Signature_fx_get, _isocontour.Signature_fx_set)
    __swig_setmethods__["fy"] = _isocontour.Signature_fy_set
    __swig_getmethods__["fy"] = _isocontour.Signature_fy_get
    if _newclass:fy = _swig_property(_isocontour.Signature_fy_get, _isocontour.Signature_fy_set)
    def getFx(self, *args) -> "void" : return _isocontour.Signature_getFx(self, *args)
    def getFy(self, *args) -> "void" : return _isocontour.Signature_getFy(self, *args)
    def __init__(self): 
        this = _isocontour.new_Signature()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _isocontour.delete_Signature
    __del__ = lambda self : None;
Signature_swigregister = _isocontour.Signature_swigregister
Signature_swigregister(Signature)

class SliceData(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SliceData, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SliceData, name)
    __repr__ = _swig_repr
    __swig_setmethods__["width"] = _isocontour.SliceData_width_set
    __swig_getmethods__["width"] = _isocontour.SliceData_width_get
    if _newclass:width = _swig_property(_isocontour.SliceData_width_get, _isocontour.SliceData_width_set)
    __swig_setmethods__["height"] = _isocontour.SliceData_height_set
    __swig_getmethods__["height"] = _isocontour.SliceData_height_get
    if _newclass:height = _swig_property(_isocontour.SliceData_height_get, _isocontour.SliceData_height_set)
    __swig_setmethods__["datatype"] = _isocontour.SliceData_datatype_set
    __swig_getmethods__["datatype"] = _isocontour.SliceData_datatype_get
    if _newclass:datatype = _swig_property(_isocontour.SliceData_datatype_get, _isocontour.SliceData_datatype_set)
    __swig_setmethods__["ucdata"] = _isocontour.SliceData_ucdata_set
    __swig_getmethods__["ucdata"] = _isocontour.SliceData_ucdata_get
    if _newclass:ucdata = _swig_property(_isocontour.SliceData_ucdata_get, _isocontour.SliceData_ucdata_set)
    __swig_setmethods__["usdata"] = _isocontour.SliceData_usdata_set
    __swig_getmethods__["usdata"] = _isocontour.SliceData_usdata_get
    if _newclass:usdata = _swig_property(_isocontour.SliceData_usdata_get, _isocontour.SliceData_usdata_set)
    __swig_setmethods__["fdata"] = _isocontour.SliceData_fdata_set
    __swig_getmethods__["fdata"] = _isocontour.SliceData_fdata_get
    if _newclass:fdata = _swig_property(_isocontour.SliceData_fdata_get, _isocontour.SliceData_fdata_set)
    def __init__(self): 
        this = _isocontour.new_SliceData()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _isocontour.delete_SliceData
    __del__ = lambda self : None;
SliceData_swigregister = _isocontour.SliceData_swigregister
SliceData_swigregister(SliceData)

class Contour2dData(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Contour2dData, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Contour2dData, name)
    __repr__ = _swig_repr
    __swig_setmethods__["nvert"] = _isocontour.Contour2dData_nvert_set
    __swig_getmethods__["nvert"] = _isocontour.Contour2dData_nvert_get
    if _newclass:nvert = _swig_property(_isocontour.Contour2dData_nvert_get, _isocontour.Contour2dData_nvert_set)
    __swig_setmethods__["nedge"] = _isocontour.Contour2dData_nedge_set
    __swig_getmethods__["nedge"] = _isocontour.Contour2dData_nedge_get
    if _newclass:nedge = _swig_property(_isocontour.Contour2dData_nedge_get, _isocontour.Contour2dData_nedge_set)
    def __init__(self): 
        this = _isocontour.new_Contour2dData()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _isocontour.delete_Contour2dData
    __del__ = lambda self : None;
Contour2dData_swigregister = _isocontour.Contour2dData_swigregister
Contour2dData_swigregister(Contour2dData)

class Contour3dData(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Contour3dData, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Contour3dData, name)
    __repr__ = _swig_repr
    __swig_setmethods__["nvert"] = _isocontour.Contour3dData_nvert_set
    __swig_getmethods__["nvert"] = _isocontour.Contour3dData_nvert_get
    if _newclass:nvert = _swig_property(_isocontour.Contour3dData_nvert_get, _isocontour.Contour3dData_nvert_set)
    __swig_setmethods__["ntri"] = _isocontour.Contour3dData_ntri_set
    __swig_getmethods__["ntri"] = _isocontour.Contour3dData_ntri_get
    if _newclass:ntri = _swig_property(_isocontour.Contour3dData_ntri_get, _isocontour.Contour3dData_ntri_set)
    __swig_setmethods__["vfun"] = _isocontour.Contour3dData_vfun_set
    __swig_getmethods__["vfun"] = _isocontour.Contour3dData_vfun_get
    if _newclass:vfun = _swig_property(_isocontour.Contour3dData_vfun_get, _isocontour.Contour3dData_vfun_set)
    __swig_setmethods__["colorvar"] = _isocontour.Contour3dData_colorvar_set
    __swig_getmethods__["colorvar"] = _isocontour.Contour3dData_colorvar_get
    if _newclass:colorvar = _swig_property(_isocontour.Contour3dData_colorvar_get, _isocontour.Contour3dData_colorvar_set)
    __swig_setmethods__["fmin"] = _isocontour.Contour3dData_fmin_set
    __swig_getmethods__["fmin"] = _isocontour.Contour3dData_fmin_get
    if _newclass:fmin = _swig_property(_isocontour.Contour3dData_fmin_get, _isocontour.Contour3dData_fmin_set)
    __swig_setmethods__["fmax"] = _isocontour.Contour3dData_fmax_set
    __swig_getmethods__["fmax"] = _isocontour.Contour3dData_fmax_get
    if _newclass:fmax = _swig_property(_isocontour.Contour3dData_fmax_get, _isocontour.Contour3dData_fmax_set)
    def __init__(self): 
        this = _isocontour.new_Contour3dData()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _isocontour.delete_Contour3dData
    __del__ = lambda self : None;
Contour3dData_swigregister = _isocontour.Contour3dData_swigregister
Contour3dData_swigregister(Contour3dData)

class ConDataset(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ConDataset, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ConDataset, name)
    __repr__ = _swig_repr
    __swig_setmethods__["vnames"] = _isocontour.ConDataset_vnames_set
    __swig_getmethods__["vnames"] = _isocontour.ConDataset_vnames_get
    if _newclass:vnames = _swig_property(_isocontour.ConDataset_vnames_get, _isocontour.ConDataset_vnames_set)
    __swig_setmethods__["nsfun"] = _isocontour.ConDataset_nsfun_set
    __swig_getmethods__["nsfun"] = _isocontour.ConDataset_nsfun_get
    if _newclass:nsfun = _swig_property(_isocontour.ConDataset_nsfun_get, _isocontour.ConDataset_nsfun_set)
    __swig_setmethods__["sfun"] = _isocontour.ConDataset_sfun_set
    __swig_getmethods__["sfun"] = _isocontour.ConDataset_sfun_get
    if _newclass:sfun = _swig_property(_isocontour.ConDataset_sfun_get, _isocontour.ConDataset_sfun_set)
    __swig_setmethods__["data"] = _isocontour.ConDataset_data_set
    __swig_getmethods__["data"] = _isocontour.ConDataset_data_get
    if _newclass:data = _swig_property(_isocontour.ConDataset_data_get, _isocontour.ConDataset_data_set)
    __swig_setmethods__["plot"] = _isocontour.ConDataset_plot_set
    __swig_getmethods__["plot"] = _isocontour.ConDataset_plot_get
    if _newclass:plot = _swig_property(_isocontour.ConDataset_plot_get, _isocontour.ConDataset_plot_set)
    def getSignature(self, *args) -> "Signature *" : return _isocontour.ConDataset_getSignature(self, *args)
    def __init__(self): 
        this = _isocontour.new_ConDataset()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _isocontour.delete_ConDataset
    __del__ = lambda self : None;
ConDataset_swigregister = _isocontour.ConDataset_swigregister
ConDataset_swigregister(ConDataset)


def setVerboseLevel(*args) -> "void" :
  return _isocontour.setVerboseLevel(*args)
setVerboseLevel = _isocontour.setVerboseLevel

def newDatasetUnstr(*args) -> "ConDataset *" :
  return _isocontour.newDatasetUnstr(*args)
newDatasetUnstr = _isocontour.newDatasetUnstr

def newDatasetReg(*args) -> "ConDataset *" :
  return _isocontour.newDatasetReg(*args)
newDatasetReg = _isocontour.newDatasetReg

def loadDataset(*args) -> "ConDataset *" :
  return _isocontour.loadDataset(*args)
loadDataset = _isocontour.loadDataset

def getDatasetInfo(*args) -> "DatasetInfo *" :
  return _isocontour.getDatasetInfo(*args)
getDatasetInfo = _isocontour.getDatasetInfo

def getVariableNames(*args) -> "char **" :
  return _isocontour.getVariableNames(*args)
getVariableNames = _isocontour.getVariableNames

def getSeedCells(*args) -> "SeedData *" :
  return _isocontour.getSeedCells(*args)
getSeedCells = _isocontour.getSeedCells

def getNumberOfSignatures(*args) -> "int" :
  return _isocontour.getNumberOfSignatures(*args)
getNumberOfSignatures = _isocontour.getNumberOfSignatures

def getSignatureFunctions(*args) -> "Signature *" :
  return _isocontour.getSignatureFunctions(*args)
getSignatureFunctions = _isocontour.getSignatureFunctions

def getSignatureValues(*args) -> "float *" :
  return _isocontour.getSignatureValues(*args)
getSignatureValues = _isocontour.getSignatureValues

def getSlice(*args) -> "SliceData *" :
  return _isocontour.getSlice(*args)
getSlice = _isocontour.getSlice

def getContour2d(*args) -> "Contour2dData *" :
  return _isocontour.getContour2d(*args)
getContour2d = _isocontour.getContour2d

def getContour3d(*args) -> "Contour3dData *" :
  return _isocontour.getContour3d(*args)
getContour3d = _isocontour.getContour3d

def saveContour2d(*args) -> "void" :
  return _isocontour.saveContour2d(*args)
saveContour2d = _isocontour.saveContour2d

def saveContour3d(*args) -> "void" :
  return _isocontour.saveContour3d(*args)
saveContour3d = _isocontour.saveContour3d

def writeIsoComponents(*args) -> "void" :
  return _isocontour.writeIsoComponents(*args)
writeIsoComponents = _isocontour.writeIsoComponents

def clearDataset(*args) -> "void" :
  return _isocontour.clearDataset(*args)
clearDataset = _isocontour.clearDataset

def newDatasetRegFloat3D(*args) -> "ConDataset *" :
  return _isocontour.newDatasetRegFloat3D(*args)
newDatasetRegFloat3D = _isocontour.newDatasetRegFloat3D

def delDatasetReg(*args) -> "void" :
  return _isocontour.delDatasetReg(*args)
delDatasetReg = _isocontour.delDatasetReg

def delContour3d(*args) -> "void" :
  return _isocontour.delContour3d(*args)
delContour3d = _isocontour.delContour3d

def newDatasetRegShort3D(*args) -> "ConDataset *" :
  return _isocontour.newDatasetRegShort3D(*args)
newDatasetRegShort3D = _isocontour.newDatasetRegShort3D

def newDatasetRegUchar3D(*args) -> "ConDataset *" :
  return _isocontour.newDatasetRegUchar3D(*args)
newDatasetRegUchar3D = _isocontour.newDatasetRegUchar3D

def setOrig3D(*args) -> "void" :
  return _isocontour.setOrig3D(*args)
setOrig3D = _isocontour.setOrig3D

def setSpan3D(*args) -> "void" :
  return _isocontour.setSpan3D(*args)
setSpan3D = _isocontour.setSpan3D

def newDatasetRegFloat2D(*args) -> "ConDataset *" :
  return _isocontour.newDatasetRegFloat2D(*args)
newDatasetRegFloat2D = _isocontour.newDatasetRegFloat2D

def newDatasetRegShort2D(*args) -> "ConDataset *" :
  return _isocontour.newDatasetRegShort2D(*args)
newDatasetRegShort2D = _isocontour.newDatasetRegShort2D

def newDatasetRegUchar2D(*args) -> "ConDataset *" :
  return _isocontour.newDatasetRegUchar2D(*args)
newDatasetRegUchar2D = _isocontour.newDatasetRegUchar2D

def setOrig2D(*args) -> "void" :
  return _isocontour.setOrig2D(*args)
setOrig2D = _isocontour.setOrig2D

def setSpan2D(*args) -> "void" :
  return _isocontour.setSpan2D(*args)
setSpan2D = _isocontour.setSpan2D

def getContour3dData(*args) -> "void" :
  return _isocontour.getContour3dData(*args)
getContour3dData = _isocontour.getContour3dData

def getContour2dData(*args) -> "void" :
  return _isocontour.getContour2dData(*args)
getContour2dData = _isocontour.getContour2dData
# This file is compatible with both classic and new-style classes.

string2Float = _isocontour.string2Float
getSliceArray = _isocontour.getSliceArray
