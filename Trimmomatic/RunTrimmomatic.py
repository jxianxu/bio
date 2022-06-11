#! /bin/python
import signal
import sys
import commands
import os
from xml.dom.minidom import parse

# enable handle for SIGPIPE
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

class RunTimmomatic():
    def __init__(self, xml):
        self.xml_file = xml
        self.command = 'java -jar /home/djiang/bio/trimmomatic/Trimmomatic-0.39/trimmomatic-0.39.jar '

    def runFromXML(self):
        # get xml document object
        domTree = parse(self.xml_file)
        # get root node
        rootNode = domTree.documentElement
        # get <Arguments></Arguments>
        arguments = rootNode.getElementsByTagName('Arguments')

        for i in range(len(arguments)):
            command_line = self.command

            type = arguments[i].getElementsByTagName('type')[0].childNodes[0].data
            command_line += type + ' '
            inputs = arguments[i].getElementsByTagName('input')
            for j in range(len(inputs)):
                inputj = inputs[j].childNodes[0].data
                command_line += inputj + ' '

            outputs = arguments[i].getElementsByTagName('output')
            for k in range(len(outputs)):
                #print('output: ', outputs[k].childNodes[0].data)
                outputk = outputs[k].childNodes[0].data
                command_line += outputk + ' '

            LEADING = arguments[i].getElementsByTagName('LEADING')[0].childNodes[0].data
            TRAILING = arguments[i].getElementsByTagName('TRAILING')[0].childNodes[0].data
            SLIDINGWINDOW = arguments[i].getElementsByTagName('SLIDINGWINDOW')[0].childNodes[0].data
            MINLEN = arguments[i].getElementsByTagName('MINLEN')[0].childNodes[0].data
            phred = arguments[i].getElementsByTagName('phred')[0].childNodes[0].data
            ILLUMINACLIP = arguments[i].getElementsByTagName('ILLUMINACLIP')[0].childNodes[0].data

            command_line += "LEADING:" + LEADING + ' '
            command_line += 'TRAILING:' + TRAILING + ' '
            command_line += 'SLIDINGWINDOW:' + SLIDINGWINDOW + ' '
            command_line += 'MINLEN:' + MINLEN + ' '
            command_line += '-' + phred + ' '
            command_line += 'ILLUMINACLIP:' + ILLUMINACLIP
            print('Run Trimmomatic:\n' + command_line)
            a, b = commands.getstatusoutput("java -jar /home/djiang/bio/trimmomatic/Trimmomatic-0.39/trimmomatic-0.39.jar -h")
            print('Return:', a)
            print('Output:', b)
trimm = RunTimmomatic("Trimmomatic.xml")
trimm.runFromXML()
            
