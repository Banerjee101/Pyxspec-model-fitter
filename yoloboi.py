import xspec
import pylab
import gc
import numpy as np
import matplotlib.pyplot as plt
from xspec import *
from astropy.io import fits
from astropy.io import ascii


def model_fit(s1,b1,r1,a1,abun,xse,mod,working_directory):
	logFile = Xset.openLog(working_directory+"/tbabs*"+mod+".txt"),			#location of the output log file
	spec1=Spectrum(s1)				#data input
	back1=spec1.background=b1			#background input
	resp1=spec1.response=r1				#response input
	arf1=spec1.response.arf=a1			#arf input
	spec1.show()
	Xset.abund=abun					#solar abundance tables
	Xset.xsect=xse					#crossections
	spec1.ignore("**-0.3 6.0-**")			#change for different energy ignore/notice parameters, and add to it for different energy ranges for different data
	m1 = Model('tbabs*'+mod)		
	#m1.systematic=0.02				#model systematic error set to 2%
	Fit.query="yes"					
	Plot.setRebin(5,5)				#rebinning parameters, syntax: (minSig, maxBins, groupNum, errType)
	Fit.renorm()					#to perform renormalizations
	Fit.perform()
	spec1.response.gain.slope="1 -1"		#freezing the slope to 1.0 Do this for less number of models, with multiple models this gets a bit squeaky
	Fit.perform()					
	Plot.xLog=True					#to convert the plots into log log plots
	Plot.yLog=True
	#Plot.add=True					#to plot the additive compounds, only needed if more than one additive models are used
	#Plot.background=True				#this would only work in /xw however, this helps plot the bkg
	Plot.device = '/null'				#this section is for plotting the data using matplotlib
	Plot('data')					
	energy=Plot.x()					
	Norm_Count=Plot.y()
	folded=Plot.model()
	plt.plot(energy, Norm_Count, 'r.', energy, folded)
	plt.xlabel('channels')
	plt.ylabel('counts/cm^2/sec/chan')
	plt.yscale('log')				#For setting the X and Y scale as log, when plotting energy values
	plt.xscale('log')
	plt.savefig(working_directory+'/Plots/tbabs*'+mod+'.png')					#finally saving the figure in the working directory
	AllModels.clear()
	Xset.closeLog()
