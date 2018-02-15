#include <stdio.h>

void Arrive(int * id, int * gender);
void UseFacilities(int * id, int * gender, int * time);
void Depart(int * id, int * gender);
void OnePerson(int * id, int * gender, int * time);

// 3 people max in restroom at any given time
// 2 people max in restroom if opposite gender is waiting

int inRestroom[3] = {0, 0, 0};
int inQueue[20] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

int main() {


    return 0;
}

void Arrive(int * id, int * gender) {

    // Add to queue

    for (int i = 0; i < 20; i++) {
        if (inQueue[i] == 0) {
            inQueue[i] = *id;
        }
    }

}

void UseFacilities(int * id, int * gender, int * time) {

}

void Depart(int * id, int * gender) {

}

void OnePerson(int * id, int * gender, int * time) {

}