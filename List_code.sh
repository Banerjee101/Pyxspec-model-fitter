#This script is to be used after PyXspecTrial1.py when one has all the log files into a seprate directory so that this program can access that directory and print out the reduced chi square values for each into another file
gawk 'function basename(file, a, n) 
	{
    		n = split(file, a, "/")
    		return a[n]
  	}
      	{prevlast = last; last = $0}
      	ENDFILE {if (FNR >= 2) print "Model", basename(FILENAME) ":", prevlast}' /home/ankush/Desktop/PyXspec_Sample_Code/SingleModelLog_1A-1246588/*.txt > /home/ankush/Desktop/PyXspec_Sample_Code/Output_results.txt
#Change the locations of the files {input_file > output_file} in the previous line. Don't change the *.txt at the end
