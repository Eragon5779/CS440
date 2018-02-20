#include <stdio.h>
#include <unistd.h>

void initLine();
int genGen();
void Arrive(int * id, int * gender);
void UseFacilities(int * id, int * gender, int * time);
void Depart(int * id, int * gender);
void OnePerson(int * id, int * gender, int * time);

// 3 people max in restroom at any given time
// 2 people max in restroom if opposite gender is waiting

struct Person {
  int id;
  int gender;
  int timeIn;
};

struct Person line[20];		// Where the ID is the place in line
struct Person bathroom[3];

int main() {
	srand(time(NULL));

	initLine();

	printf("%d\n", line[11].gender);

	return 0;
}

//Initialization Functions
void initLine() {
	for (int i = 0; i < 20; i++) {
		line[i].id = i;
		line[i].gender = genGen();	   //Weighted generation function, will write it later
		line[i].timeIn = rand() % (7 + 1 - 3) + 3;
	}
}

int genGen() {

	int gender = rand() % (100+1);

	if (gender <= 60) {
		return 0;
	}
	else {
		return 1;
	}

}

// Main functions
void Arrive(Person * p) {

}

// sleeps for time seconds
void UseFacilities(Person * p) {

	sleep(p.timeIn);
	return;

}

void Depart(int * id, int * gender) {

}

void OnePerson(int * id, int * gender, int * time) {

}
