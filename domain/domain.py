# -*- coding: utf-8 -*-

from yuelianglib.common.utils import print_err,get_err
import re

# re_name = re.compile(r'^[bpmfdtnlgkhjqxrzcsyw0-9]{1,4}$', re.U)
re_name = re.compile('^[bpmfdtnlgkhjqxrzcsyw]{5}$', re.U)
# re_name = re.compile('^[0-9]{7}$', re.U)
re_tv = re.compile(r'^[a-z0-9]{1,3}\.tv$', re.U)
re_cc = re.compile(r'^[a-z0-9]{1,3}\.cc$', re.U)
re_net = re.compile(r'^[a-z0-9]{1,3}\.net$', re.U)
re_vr = re.compile(r'^(ar|vr|smart|life).*$', re.U)
# re_vr = re.compile(r'^.*(ar|vr|smart|life)$', re.U)
if __name__ == '__main__':
	f = open('123.txt', 'rb')
	for lineno, line in enumerate(f, 1):
		try:
			line = line.strip().decode('utf-8')
			name, com = line.split('.')[:2]
			if com == 'com':
				if re_name.match(name):
					print name,com
				# elif re_vr.match(line)  and com == 'com':
				# 	print name,com
			# elif re_tv.match(line):
			# 	print name,com
			# elif re_cc.match(line):
			# 	print name,com
			# elif re_net.match(line):
			# 	print name,com

		except:
			print_err()
	f.close()