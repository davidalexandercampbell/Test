# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 15:22:18 2019

@author: david
"""


import pyvisa as visa



class E3631():
    voltage = 0
    current = 0
    
    
    def __init__(self):
        rm = visa.ResourceManager('@sim')
        # SCPI_E3631 = rm.open_resource('')
        SCPI_E3631 = rm.open_resource('ASRL1::INSTR', read_termination='\n')
#    SCPI_E3631.write('*RST')
#    SCPI_E3631.write(':OUTP:STAT %d' % (0))
#    SCPI_E3631.write(':APPL %s,%s,%s' % ('P6V', 'MIN', 'MIN'))
        SCPI_E3631.close()
        rm.close()

    def setVoltage(self,voltage):
        rm = visa.ResourceManager('@sim')
        SCPI_E3631 = rm.open_resource('ASRL1::INSTR', read_termination='\n')
#    SCPI_E3631.write(':APPL %s,%G' % ('P6V', 0.95))
        SCPI_E3631.query('!APPL %.2f' % (voltage))
        SCPI_E3631.close()
        rm.close()

    def getVoltage(self):
        rm = visa.ResourceManager('@sim')
        SCPI_E3631 = rm.open_resource('ASRL1::INSTR', read_termination='\n')
        #temp_values = SCPI_E3631.query_ascii_values(':MEAS:VOLT:DC? %s' % ('P6V'))
        voltage = SCPI_E3631.query(":MEAS")
        SCPI_E3631.close()
        rm.close()
        return(voltage)

    
psu = E3631()
psu.setVoltage(1.95)
reading = psu.getVoltage()
print(reading)