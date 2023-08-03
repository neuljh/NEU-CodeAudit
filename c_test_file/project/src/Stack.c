/*
 @description: ջʵ�֣�ͨ��ʹ��void*ʵ��ģ��,��ȡֵʱ��Ҫʹ��ǿ������ת��
 @return : none
*/
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>
#include <string.h>
#include "stack.h"
/*
 @description: ջ�ĳ�ʼ��
 @param: ��Ҫ����ͷ�ڵ�ĵ�ַ &(*node)
 @return: none
*/
void stack_initial(node** a) {
	*a = NULL;
}

/*
 @description: �ж�ջ�Ƿ�Ϊ��
 @param: ջ��ͷ�ڵ�
 @return: ��ջΪ�շ���1�����򷵻�0
*/
int stack_empty(node* a) {
	return (a == NULL);
}

/*
 @description: ��ջ�в���Ԫ��
 @param: ��Ҫ����ͷ�ڵ�ĵ�ַ &(*node) ��Ҫ�����Ԫ��
 @return: ������ɹ�����1�����򷵻�0
*/
int stack_insert(node** a, EleType item) {
	node* temp;
	if ((temp = (node*)malloc(sizeof(node))) != NULL) {
		temp->next = *a;
		temp->value = item;
		*a = temp;
		return 1;
	}
	return 0;
}

/*
 @description: ��ջ��ɾ��Ԫ�ز�������ֵ
 @param: ��Ҫ����ͷ�ڵ�ĵ�ַ &(*node)
 @return: ��ջΪ�շ���NULL�����򷵻�ջ��Ԫ�ص�ֵ
*/
EleType stack_delete(node** a) {
	EleType value;
	if (stack_empty(*a))
		return NULL;
	node* temp = *a;
	value = temp->value;
	*a = (*a)->next;
	free(temp);
	return value;
}

/*
 @description: ��ȡջ��Ԫ�ص�ֵ
 @param: ջ��ͷ�ڵ� �� ���ڴ洢ջ��ֵ��ָ��
 @return: ��ջΪ�շ���0�����򷵻�1
*/
int stack_gettop(node* a, EleType* result) {
	if (stack_empty(a))
		return 0;
	*result = a->value;
	return 1;
}


int convert_to_bin(int data) {
	node* stack = (node*)malloc(sizeof(node));
	stack_initial(&stack);
	int remain=0;
	int len = 0, result = 0;
	
	while (data != 0) {
		remain = data % 2;
		stack_insert(&stack, (EleType)remain);
		data = data / 2;
	}
	while (!stack_empty(stack)) {
		remain = (int)stack_delete(&stack);
		result += remain * pow(10, len++);
		printf("%d", remain);
	}
	return result;
}

int compare(char c, char d) {
	if (c == '+' || c == '-') {
		switch (d) {
		case '*':return 0;
		case '/':return 0;
		case '+':return 0;
		case '-':return 0;
		case '(':return 1;
		}
	}

	if (c == '*' || c == '/') {
		switch (d) {
		case '*':return 0;
		case '/':return 0;
		case '+':return 1;
		case '-':return 1;
		case '(':return 1;
		}
		return 1;
	}
	return 1;
}
	
char*  inffix_to_suffix(char* inffix) {
	size_t inffix_len = strlen(inffix);
	char* suffix = (char*)malloc(sizeof(char) * (inffix_len + 1));
	node* stack = (node*)malloc(sizeof(node));
	stack_initial(&stack);
	size_t i,len=0;
	char c;

	EleType temp;

	for (i = 0; i < inffix_len; i++) {
		c = inffix[i];
		if (isdigit(c))
			suffix[len++] = c;
		else if (c == '(')
			stack_insert(&stack, (EleType)c);
		else if (c == ')') {
			while (1) {
				stack_gettop(stack, &temp);
				char k = (char)temp;
				stack_delete(&stack);/*����*/
				if (k == '(') 
					break;
				else /*��������Ĳ���(�����������ʼд��*/
					suffix[len++] = k;
			}
		}
		else {
			while (1) {
				if (stack_empty(stack))
					break;
				stack_gettop(stack, &temp);
				char k = (char)temp;
				if (compare(c, k)) /*c���ڵ�ǰk�ſ��Խ�ջ*/
					break;
				else {
					suffix[len++] = k;
					stack_delete(&stack);
				}
			}
			stack_insert(&stack, (EleType)c);
		}
	}
	/*�������������ε���ջ�еļ���*/
	while (!stack_empty(stack)) {
		stack_gettop(stack, &temp);
		char k = (char)temp;
		suffix[len++] = k;
		stack_delete(&stack);
	}
	suffix[len++] = '\0';/*������*/
	return suffix;
}

float eval_suffix(char* suffix) {
	size_t suffix_len = strlen(suffix);
	node* stack = (node*)malloc(sizeof(node));
	stack_initial(&stack);
	size_t i, len = 0;
	char c;
	EleType temp;
	for (i = 0; i < suffix_len; i++) {
		c = suffix[i];
		if (isdigit(c)) {
			float* k = (float*)malloc(sizeof(float));
			*k =(float)(c - '0');
			stack_insert(&stack,(EleType)k);
		}
			
		else {
			/*��ȡ���������ʼ����,ע��mn��˳�����⣬ m c n ջ�д洢��mn�ȶ�������n*/
			float m, n, result;
			temp= stack_delete(&stack);
			n = *(float*)temp;
			temp = stack_delete(&stack);
			m = *(float*)temp;

			if (c == '+')
				result=m + n;
			else if (c == '-')
				result = m - n;
			else if (c == '*')
				result = m * n;
			else if (c == '/') {
				if (n == 0) {
					printf("the n is 0");
					exit(0);
				}
				result = m / n;
			}
			float* k = (float*)malloc(sizeof(float));
			*k = result;
			stack_insert(&stack, (EleType)k);	
		}
	}
	stack_gettop(stack,&temp);
	float* a = (float*)temp;
	return *a;
}
//int main() {
//	//convert_to_bin(255);
//
//	char* a = "1+(2-3/4)*5";
//	char* b = inffix_to_suffix(a);
//	printf("%s\n", b);
//	printf("%.4f", eval_suffix(b));
//	
//	//node* stack;
//	//stack_initial(&stack);
//	//int a = 2;
//	//int* pa = &a;
//	//EleType top;
//
//	//stack_insert(&stack, (EleType)2);
//	///*�洢ָ������*/
//	///*stack_gettop(stack, &top);
//	//int* pb = (int*)top;
//	//int b = *pb;*/
//	//stack_insert(&stack, (EleType)4);
//	//stack_insert(&stack, (EleType)6);
//	//
//	//if (stack_gettop(stack, &top)) {
//	//	printf("Stack top: %d\n", (int)top);
//	//}
//	//else {
//	//	printf("Stack is empty.\n");
//	//}
//	//while (!stack_empty(stack)) {
//	//	EleType value = stack_delete(&stack);
//	//	printf("Deleted value: %d\n", (int)value);
//	//}
//
//	//return 0;
//}