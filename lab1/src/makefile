#instruction for creating every executable file
all: lab1part2.exe 

#cleans out the bin folder containing the executables
clean:
	rm ../../bin/*.exe

#instructions for creating lab1part2.exe executable file after linking
lab1part2.exe: lab1part2.cpp 
	g++ -o ../bin/lab1part2.exe lab1part2.cpp 
#instruction to execute the lab1part2.exe file
run01: 
	@echo ---------------------
	@echo Running lab1part2.exe
	../bin/lab1part2.exe
	@echo
