#include <stdio.h>

void Arrive(int * id, int * gender);
void UseFacilities(int * id, int * gender, int * time);
void Depart(int * id, int * gender);
void OnePerson(int * id, int * gender, int * time);

// 3 people max in restroom at any given time
// 2 people max in restroom if opposite gender is waiting

int inRestroom[3];
int maleQueue[20];
int femaleQueue[20];

int main() {

    memset(inRestroom, -1, sizeof inRestroom);
    memset(maleQueue, -1, sizeof maleQueue);
    memset(femaleQueue, -1, sizeof femaleQueue);

    return 0;
}

void Arrive(int * id, int * gender) {

    // Add to queue

    for (int i = 0; i < 20; i++) {
        if (*gender == 0) {
            
        }
    }

}

void UseFacilities(int * id, int * gender, int * time) {

}

void Depart(int * id, int * gender) {

}

void OnePerson(int * id, int * gender, int * time) {

}