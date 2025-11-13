# C++ Compiler
CXX= g++
# C++ Compiler Flags
CXXFLAGS=-I./include/

#local directories
LOCALSRC=./src
LOCALOBJ=./obj
LOCALBIN=./bin

SRCS=$(wildcard $(LOCALSRC)/*.cpp )
OBJS=$(SRCS:$(LOCALSRC)/%.cpp=$(LOCALOBJ)/%.o)
EXES=$(SRCS:$(LOCALSRC)/%.cpp=$(LOCALBIN)/%.exe)

all: $(EXES)

clean: 
	-@rm -f $(LOCALBIN)/*.exe 2> /dev/null

$(LOCALOBJ)/%.o: $(LOCALSRC)/%.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

$(LOCALBIN)/%.exe: $(LOCALOBJ)/%.o
	$(CXX) $(CXXFLAGS) $< -o $@
