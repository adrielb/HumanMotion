VLROOT=/home/abergman/apps/vlfeat
export LD_LIBRARY_PATH:=${VLROOT}/bin/glnxa64:${LD_LIBRARY_PATH}

all: run

vlfeat-test: main.cpp
	g++ $< -o $@ -I${VLROOT} -L${VLROOT}/bin/glnxa64/ -lvl

run: vlfeat-test
	./vlfeat-test
