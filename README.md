# Employment_reEducation_USA
Employment and Re-Education Opportunities in the USA using data from Labor Bureau of Statistics, US Census and NSCG

FOR NCES - IPEDS Dataset

MapReduce (Used for Profiling and Cleaning)
Dir - /user/tsb348/C_A - Contains Input files in /C_A, Mapper code, reducer code and output.
Using a script ca_script.sh we get the output for the year (2008-2017) and move it to /user/tsb349/hive_ca

Dir - /user/tsb348/hive_cipcode - Contains information on the cipcodes

Dir - /user/tsb348/HD - Contains information on universities. Input files in /files, Mapper code, reducer code and output at /user/tsb348/HD.
Moved it to /user/tsb349/hive_hd and created a new table in hive with distinct  UNITID.


FOR NSCG Dataset

all item are in:   /user/hi348/ 

cestocip/cestocip.csv	<--Mapping Table
conversion/conversion.csv	<--Mapping Table
edoc/edoc.csv		<--Mapping Table
naics/output/part-m-00000           <---jobind table
indnai/indnai.csv               <--ind_to_naics table
proj/output/part-m-00000        <--nscg table after cleaning and profiling
tsb                             <---copy of ipeds hive data
tsbcip/CIPcode2020.csv  <---copy of cipcode tables
tsbhd/hd.txt        <--- copy of institute details
earn/earn.csv	<--- Earning Data
