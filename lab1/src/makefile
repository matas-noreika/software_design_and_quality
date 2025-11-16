#C++ Compiler
CXX= g++ # matas 2025-11-16 - added a variable to allow for easy change to C++ compiler choice

#C Compiler Flags
CXXFLAGS= # matas 2025-11-16 - added a vairable to allow for easy changes to C++ compiler flags

#Local directories
LOCALBIN= ../bin# matas 2025-11-16 - Added vairable to hold relative path to bin directory

#instruction for creating every executable file
all: lab1Part2.exe

#cleans out the bin folder containing the executables
clean:
	-rm $(LOCALBIN)/*.exe 2> /dev/null # matas 2025-11-16 - ensured clean commands dont throw errors

#instructions for creating lab1part2.exe executable file after linking
lab1Part2.exe: lab1Part2.cpp
	$(CXX) -o $(LOCALBIN)/lab1Part2.exe lab1Part2.cpp # matas 2025-11-16 - Added change for command to use compiler variable

#instruction to execute the lab1part2.exe file
run01:
	@echo ---------------------
	@echo Running lab1Part2.exe
	../bin/lab1Part2.exe
	@echo
