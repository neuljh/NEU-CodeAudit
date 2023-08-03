/*
 @description: ˳��洢�ṹ
 @return : none
*/
#include <stdio.h>
#include <math.h>

#define EleType int
#define queueSize 100

EleType queue[queueSize];
int front,rear;


void queue_initial(int *front,int* rear) {
	*front=0;
	*rear =0;
}

int queue_empty(int front,int rear) {
	return front==rear;
}

int queue_insert(int *rear,EleType item) {
	if (*rear==queueSize-1) {
		return 0;/*�ж϶����Ѿ���*/
	}
	else {
		queue[++(*rear)] = item;
		return 1;
	}
}
