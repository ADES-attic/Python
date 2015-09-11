#!/usr/bin/env python3

import lxml.etree

with open('example.xsd') as f:
  sd = lxml.etree.parse(f)

sc = lxml.etree.XMLSchema(sd)

with open('example.xml') as f:
  od = lxml.etree.parse(f)

sc.assertValid(od)
