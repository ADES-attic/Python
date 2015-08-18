#!/usr/bin/env python3

import datetime

def iso(ymd):
	dt = datetime.datetime(int(ymd[:4]), int(ymd[5:7]), int(ymd[8:10]))
	dt += datetime.timedelta(float(ymd[10:]))
	return dt.isoformat()

def ra(ra):
	return str(15*(
		int(ra[:2])+
		int(ra[3:5])/60+
		float(ra[6:])/3600))

def dec(dec):
	d = (
		int(dec[1:3])+
		int(dec[4:6])/60+
		float(dec[7:])/3600)
	if dec[0] == '-':
		d = -d
	return str(d)

with open('sample.xml', 'w') as x:
	x.write('''<observationBatch>
  <observations>
''')

	with open('sample.obs') as m:
		for l in m:
			x.write('''    <optical>
      <trkSub>{}</trkSub>
      <mode>CCD</mode>
      <stn>{}</stn>
      <obsTime>{}</obsTime>
      <ra>{}</ra>
      <dec>{}</dec>
      <astCat/>
      <mag>{}</mag>
      <band>{}</band>
    </optical>
'''.format(
		l[5:12].strip(),
		l[77:80],
		iso(l[15:32]),
		ra(l[32:44]),
		dec(l[44:56]),
		l[65:69],
        l[70:71],
	))

	x.write('''  </observations>
</observationBatch>
''')
