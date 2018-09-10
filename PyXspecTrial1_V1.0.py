
import yoloboi
from yoloboi import model_fit
import sys
import optparse

parser = optparse.OptionParser()
parser.add_option('-m', '--ModelName', dest='Model_name', help='The model you wish to use', type=str)
(options, args) = parser.parse_args()
if options.Model_name is None:
	options.Model_name = raw_input('Enter Model Name:')



s1a="/home/ankush/Desktop/PyXspec_Sample_Code/SXT_PC_3s_all_allor.pha"				#put in your data
b1a="/home/ankush/Desktop/PyXspec_Sample_Code/SkyBkg_comb_EL3p5_Cl_Rd16p0_v01.pha"		#put in your background
r1a="/home/ankush/Desktop/PyXspec_Sample_Code/sxt_pc_mat_g0to12.rmf"				#put in your response
a1a="/home/ankush/Desktop/PyXspec_Sample_Code/SXT_PC_3s_all_allor.arf"				#put in your arf
abunA="lodd"											#put in your abundance table
xseA="bcmc"											#put in your crossection table
working_directoryA='/home/ankush/Desktop/PyXspec_Sample_Code/SingleModelLog_1A-1246588'		#put in the location of your working directory where you want the output to print
model_fit(s1a,b1a,r1a,a1a,abunA,xseA,options.Model_name,working_directoryA)
