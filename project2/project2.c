#include <stdio.h>

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
  int timeUsing;
  int timeOut;
  int left;
};

struct Person init[20];		// Where the ID is the place in line
struct Person line[20];
struct Person bathroom[3];
int currentTime = 0;

int main() {
	srand(time(NULL));
	int done = 0;
	for(; done == 0; curentTime++) {
		// Check to see if everyone is done and line is empty
		int checkAllDone = -1;
		for (int i = 0; i < 20; i++) {
			if (init[i].left == 1) {
				checkAllDone += 1;
			}
			else {
				break;
			}
		}
		if (checkAlldone == 19) {
			done = 1;
			break;
		}

		// Check the status of the bathroom
		// Check for empty spot
		int empty[3];
		int totalEmpty = 0;
		for (int i = 0; i < 3; i++) {
			if (bathroom[i] == NULL) {
				empty[i] == 1;
				totalEmpty += 1;
			}
		}
		// Bathroom is empty
		if (totalEmpty == 3) {
			// Line checks
			int currentGender = -1; //No gender yet
			int arrived = 0;		//No one has arrived yet
			int max = 3;			//Current max number of people that can arrive
			for (int i = 0; i < 20; i++) {
				//Make sure next in line is same gender as we are looking for
				if (currentGender == -1 || line[i].gender == currentGender) {
					// Check next in line to see gender
					if (currentGender != -1 && line[i+1].gender != currentGender) {
						// Set max arrived to 2 if next person is opposite gender
						max = 2;
					}
					// Check if arrived is less than max
					if (arrived < max) {
						for (int j = 0; j < 3; j++) {
							// If slot in bathroom empty
							if (bathroom[j] == NULL) {
								// Arrive and leave bathrom loop
								Arrive(line[i]);
								j = 3;
								break;
							}
						}
						// One more person has arrives
						arrived += 1;
					}
				}
				// Check if max has been put into the bathroom
				if (arrived == max) {
					i = 20;
					break;
				}
				
			}
		}

	}

	return 0;
}

//Initialization Functions
void allAtOnce() {
	for (int i = 0; i < 20; i++) {
		line[i].id = i;
		line[i].gender = genGen();	   //Weighted generation function, will write it later
		line[i].timeUsing = rand() % (7 + 1 - 3) + 3;
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
void Arrive(int * id, int * gender) {
	for (int i = 0; i < 3; i++) {
		if (bathroom[i] == NULL) {
			bathroom[i] == *p;
		}
	}

}

void UseFacilities(int * id, int * gender, int * time) {

}

void Depart(int * id, int * gender) {

}

void OnePerson(int * id, int * gender, int * time) {

}
