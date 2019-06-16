#!/usr/bin/python
# Converts a number from number system A to B. Systems are specified by listing
# their digits in ascending order

class converter:
    def makeTable(self, srcSym):
        self.srcTab = {};
        for j in range (0, len(srcSym)):
            self.srcTab[srcSym[j]] = j;
        self.srcRad = len(srcSym);

    def makeSymArr(self, dstSym):
        self.symArr = [];
        for j in range (0, len(dstSym)):
            self.symArr.append(dstSym[j]);
        self.dstRad = len(dstSym);

    def __init__(self, srcSym, dstSym):
        self.makeTable(srcSym);
        self.makeSymArr(dstSym);

    def convert(self, srcVal):
        val = 0;
        for i in range(0, len(srcVal)):
            digVal = self.srcTab[srcVal[i]];
            val = (val * self.srcRad) + digVal;
        dstVal = "";
        while val:
            dstVal = self.symArr[val%self.dstRad] + dstVal;
            val /= self.dstRad;
        return dstVal;

x = int(raw_input());
for i in range(0, x):
    line = raw_input().split();
    srcVal, srcSym, dstSym = line[0], line[1], line[2];
    conv = converter(srcSym, dstSym);
    dstVal = conv.convert(srcVal);
    print("Case #"+str(i+1)+": "+dstVal);
