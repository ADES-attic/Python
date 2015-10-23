#!/usr/bin/env python3

import ctypes

class ctxNameList(ctypes.Structure):
  _fields_ = (
    ("len", ctypes.c_int),
    ("names", ctypes.POINTER(ctypes.c_char_p))
  )

class ObservationContext(ctypes.Structure):
  _fields_ = (
    ("observation", ctypes.c_void_p),
    ("observatory", ctypes.c_void_p),
    ("contact", ctypes.c_void_p),
    ("observers", ctypes.c_void_p),
    ("measurers", ctypes.POINTER(ctxNameList)),
    ("telescope", ctypes.c_void_p),
    ("software", ctypes.c_void_p),
    ("comment", ctypes.c_void_p),
    ("coinvestigators", ctypes.c_void_p),
    ("collaborators", ctypes.c_void_p),
    ("fundingSource", ctypes.c_void_p),
    ("orbProd", ctypes.c_void_p),
    ("photProd", ctypes.c_void_p),
  )

class ObservationSegment(ctypes.Structure):
  _fields_ = (
    ("observationContext", ctypes.POINTER(ObservationContext)),
    ("obsList", ctypes.c_void_p)
  )

class ObservationBatch(ctypes.Structure):
  _fields_ = (
    ("len", ctypes.c_int),
    ("segments", ctypes.POINTER(ObservationSegment))
  )

lib = ctypes.CDLL('/home/skeys/lib/libades.so.0')

fn = ctypes.c_char_p(b'a.obs')
po = ctypes.pointer(ObservationBatch())

r = lib.readMPC80File(fn, ctypes.byref(po), 0, 0)
o = po.contents
for i in range(o.len):
  seg = o.segments[i]
  if seg.observationContext:
    nl = seg.observationContext.contents.measurers.contents
    for i in range(nl.len):
      print(str(nl.names[i], encoding='utf-8'))
