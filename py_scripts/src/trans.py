#!/usr/bin/python

from string import maketrans

orig_str = "g fmnc wms bgblr rpyl qjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

cap_in = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cap_out = "CDEFGHIJKLMNOPQRSTUVWXYZAB"
intab = cap_in.lower()
outtab = cap_out.lower()

trans = maketrans(intab, outtab)

print(orig_str.translate(trans))

