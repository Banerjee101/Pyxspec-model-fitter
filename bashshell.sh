#This code takes the list file for models and passes it as an argument to the python script that would be used to load data files and parameters into the main pyxspec code,
#which would then create a session of xspec and run the data using the mdel specified


declare -a myarray
let i=0
while IFS=$'\n' read -r line_data; 
do
    	myarray[i]="${line_data}" 
#	echo $myarrar$line_data
    	python PyXspecTrial1_V1.0.py -m $myarrar$line_data
    	((i++))
done < /home/ankush/Desktop/PyXspec_Sample_Code/AdditiveModels.txt		#change this to point to the input list file containing the additive models you want to fit the data with
