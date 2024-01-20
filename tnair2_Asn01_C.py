#""
# CS1026A 2023
#Assignment 01 Project 01 - Part C
#Tamanna Anandan Nair
#tnair2@uwo.ca
#5/10/2023
#""

#to calcualte amount of flops based off number of years and transistors 

print("Project One (01) - Part C: The Moore the Merrier")
num_transistors=int(input("Starting Number of transistors: "))#asking user for number of transistors
start_year=int(input("Starting Year: "))# asking user for the starting year 
total_years= int(input("Total number of Years: "))#asking user for total number of years
end_year=start_year+total_years#calcualtes the total number of years from start to end
flops_name=""#made to hold type of magnitude of flops

#constants 
KILO=1000
MEGA=1000000
GIGA=1000000000
TERA=1000000000000
PETA=1000000000000000
EXA=1000000000000000000
ZETTA=1000000000000000000000
YOTTA=1000000000000000000000000
print("YEAR : TRANSISOTR : FLOPS:")#printing acc to desired output
for i in range(start_year, end_year+1, 2):#loop to calculate and print data for each year and it incements by 2 years
    flops = 50*num_transistors
    dec_flops = 50*num_transistors
    if(flops<1000): #determining the units for flop based off magnitude
        flops_name="FLOPS"
    elif(flops >= KILO and flops < MEGA):#KILO
        dec_flops = flops/KILO
        flops_name=" kiloFLOPS"
    elif(flops >=MEGA  and flops<GIGA):#MEGA
        dec_flops = flops/MEGA
        flops_name=" megaFLOPS"    
    elif(flops>GIGA and flops<TERA):
        dec_flops=flops/GIGA
        flops_name=" gigaFLOPS"
    elif(flops>TERA and flops<PETA):
        dec_flops=flops/TERA
        flops_name=" teraFLOPS"
    elif(flops>PETA and flops<EXA):
        dec_flops=flops/PETA
        flops_name=" petaFLOPS"
    elif(flops>EXA and flops<ZETTA):
        dec_flops=flops/EXA
        flops_name=" exaFLOPS"
    elif(flops>ZETTA and flops<YOTTA):
        dec_flops=flops/ZETTA
        flops_name=" zettaFLOPS"
#formatting numbers with commas 
    flops_comma=f"{flops:,}"
    transistor_comma=f"{num_transistors:,}"
    print("%d %s %.2f %s %s" % (start_year, transistor_comma, dec_flops,flops_name, flops_comma))#print data for current year
    num_transistors = num_transistors*2#incrementing no.of transistors by 2 for every year
    start_year=start_year+2#incrementing years by 2 from start year
print("\nEND: Project One (01) - Part C")
print("Tamanna Nair tnair2 251311049")   


 
