import unittest
from recphyloxml.parser import RecPhyloXMLParser

class UnitTest(unittest.TestCase):
    def test_genefamily0(self):
        parser = RecPhyloXMLParser()
        fileName = '../testFiles/geneFamily0.phyloxml'
        print("Test 1: parses the file" , fileName , "and prints its structure to the screen")
        print(parser.parse(fileName))

    def test_f(self):
        fileName = '../testFiles/geneFamily0.phyloxml'
        f=open(fileName)
        print(f.readline())
        f.close()

#    fileName = '../testFiles/SeveralRecTrees.xml'
#    print "Test 2: parses the file" , fileName , "and prints the number of reconciled trees it contains on the screen"
#
#    RTL = parser.parse(fileName)
#    print len(RTL)
#
#
#    fileName = "../testFiles/genetree_SMALL.reconciled.0.ntg.xml"
#    print "Test 3: parses the file" , fileName , "and prints the species tree. it contains on the screen"
#
#    RTL = parser.parse(fileName)
#    print RTL.spTree
#
#    fileName = "testFiles/lossSeparatedtestFile"
#
#    RTL = parser.parse(fileName)
#
#    for RT in RTL.recTrees:
#        print RT
