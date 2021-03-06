# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.7
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
            fp, pathname, description = imp.find_module('_SubnetTree', [dirname(__file__)])
        except ImportError:
            import _SubnetTree
            return _SubnetTree
        if fp is not None:
            try:
                _mod = imp.load_module('_SubnetTree', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _SubnetTree = swig_import_helper()
    del swig_import_helper
else:
    import _SubnetTree
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


class inx_addr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, inx_addr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, inx_addr, name)
    __repr__ = _swig_repr
    __swig_setmethods__["sin"] = _SubnetTree.inx_addr_sin_set
    __swig_getmethods__["sin"] = _SubnetTree.inx_addr_sin_get
    if _newclass:sin = _swig_property(_SubnetTree.inx_addr_sin_get, _SubnetTree.inx_addr_sin_set)
    __swig_setmethods__["sin6"] = _SubnetTree.inx_addr_sin6_set
    __swig_getmethods__["sin6"] = _SubnetTree.inx_addr_sin6_get
    if _newclass:sin6 = _swig_property(_SubnetTree.inx_addr_sin6_get, _SubnetTree.inx_addr_sin6_set)
    def __init__(self): 
        this = _SubnetTree.new_inx_addr()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _SubnetTree.delete_inx_addr
    __del__ = lambda self : None;
inx_addr_swigregister = _SubnetTree.inx_addr_swigregister
inx_addr_swigregister(inx_addr)

class SubnetTree(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SubnetTree, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SubnetTree, name)
    __repr__ = _swig_repr
    def __init__(self, binary_lookup_mode=False): 
        this = _SubnetTree.new_SubnetTree(binary_lookup_mode)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _SubnetTree.delete_SubnetTree
    __del__ = lambda self : None;
    def insert(self, *args): return _SubnetTree.SubnetTree_insert(self, *args)
    def remove(self, *args): return _SubnetTree.SubnetTree_remove(self, *args)
    def lookup(self, *args): return _SubnetTree.SubnetTree_lookup(self, *args)
    def todict(self): return _SubnetTree.SubnetTree_todict(self)
    def get_binary_lookup_mode(self): return _SubnetTree.SubnetTree_get_binary_lookup_mode(self)
    def set_binary_lookup_mode(self, binary_lookup_mode=True): return _SubnetTree.SubnetTree_set_binary_lookup_mode(self, binary_lookup_mode)
    def __contains__(self, *args): return _SubnetTree.SubnetTree___contains__(self, *args)
    def __getitem__(self, *args): return _SubnetTree.SubnetTree___getitem__(self, *args)
    def __setitem__(self, *args): return _SubnetTree.SubnetTree___setitem__(self, *args)
    def __delitem__(self, *args): return _SubnetTree.SubnetTree___delitem__(self, *args)
SubnetTree_swigregister = _SubnetTree.SubnetTree_swigregister
SubnetTree_swigregister(SubnetTree)

# This file is compatible with both classic and new-style classes.


