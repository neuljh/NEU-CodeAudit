#pragma once
#include"node.h"

void stack_initial(node** a);
int stack_empty(node* a);
int stack_insert(node** a, EleType item);
EleType stack_delete(node** a);
int stack_gettop(node* a, EleType* result);
/*����ת��*/
int convert_to_bin(int data);
/*���ʽ����*/
int compare(char c, char d);
char* inffix_to_suffix(char* inffix);
float eval_suffix(char* suffix);