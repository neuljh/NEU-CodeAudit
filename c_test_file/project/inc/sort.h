#pragma once
#include<stdlib.h>
#include<stdio.h>
#include"node.h"
node* create_node(EleType value, node* next);
/*������node*/
node* create_e_node();
/*
�������
*/
node* create(EleType item);
int length(node* linklist);
int length2(node* linklist);
int empty(node* linklist);
node* find(node* linklist, EleType item);
void insert(node** linklist, EleType item, int index);
EleType delete(node** linklist, int index);
void deleteAll(node* linklist);
void reverse(node** linklist);