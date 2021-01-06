gxx=g++ -O3

all: one two four six eight twelve twentyfour clean

twentyfour: twentyfour.o config.o
	$(gxx) twentyfour.o config.o -o twentyfour -pthread
twelve: twelve.o config.o
	$(gxx) twelve.o config.o -o twelve -pthread
eight: eight.o config.o
	$(gxx) eight.o config.o -o eight -pthread
six: six.o config.o
	$(gxx) six.o config.o -o six -pthread
four: four.o config.o
	$(gxx) four.o config.o -o four -pthread
two: two.o config.o
	$(gxx) two.o config.o -o two -pthread
one: one.o config.o
	$(gxx) one.o config.o -o one
config.o: config.cpp
	$(gxx) -c config.cpp -o config.o
clean:
	rm *.o