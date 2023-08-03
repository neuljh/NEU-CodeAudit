#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include"binaryTree.h"
//A(B(c,D),E(F))
/*
 @description: ���ܹ����(Ƕ�����Ŷ���)�����룬���������
 @return : none
*/
btnode* case7_1() {
	btnode* stack[stack_size], * p=NULL, * t = NULL;
	char cmdc[] = "A(B(D,E(G)),C(F(,H)))@";
	char c;
	int flag=1, top = -1;
	for (size_t i = 0;i<strlen(cmdc);i++){
		/*scanf_s("%c", &c);*/
		c = cmdc[i];
		switch (c)
		{
		case '@':return(t);
		case '(':
			stack[++top] = p; //������������һ����ĸ������ջ,ջ��top�洢��Ϊ��ǰ�������ڵ�
			flag = 1;
			break;
		case ',':
			flag = 2;
			break;
		case ')'://�����ŵ���ջ��
			top--;
			break;

		default: /*ȡ����ĸ*/
			p = (btnode*)malloc(sizeof(btnode));
			p->value = c;
			p->left = NULL;
			p->right = NULL;
			if (t == NULL)
				t = p;
			else if(flag==1) {
				stack[top]->left = p;
			}
			else {
				stack[top]->right = p;
			}
		}
	}
}


void preorder(btnode* tree) {
	// ��-�ݹ�ǰ�����������
	btnode* stack[stack_size], * node;
	int k = -1;
	if (tree == NULL) {
		printf("tree is empty-- \n");
		return;
	}
	else {
		stack[++k] = tree; // �����ڵ���ջ
		while (k > -1) {
			//��ջ
			node = stack[k--];
			printf("%c\n", node->value);
			// �Ȱ��������Ž�ȥ��ջ���Ƚ�ȥ���������������������ȳ�
			if (node->right != NULL) {
				stack[++k] = node->right;
			}
			if (node->left != NULL) {
				stack[++k] = node->left;
			}
		}
	}
}
/*�ǵݹ��㷨�������*/
void inorder(btnode* tree) {
	if (tree == NULL) {
		printf("tree is empty-- \n");
		return;
	}
	btnode* stack[stack_size],*p=tree;
	int top = -1;
	while (!(p == NULL && top == -1)) {
		//�ҵ���ǰ�������Ԫ��
		while (p != NULL) {
			stack[++top] = p;
			p = p->left;
		}
		p=stack[top--];//��ȡ��ǰջ��������ȡԪ��
		printf("%c\n", p->value);
		p = p->right;
	}

}
/*�ǵݹ�ĺ�����������ջд��*/
void postorder(btnode* tree) {
	if (tree == NULL) {
		printf("tree is empty-- \n");
		return;
	}
	btnode* stack[stack_size];
	int top = -1;
	btnode* p = tree,*r=NULL;
	while (p != NULL || top != -1) {
		//Ѱ�����������
		if(p != NULL) {
			stack[++top] = p;
			p = p->left;
		}
		else {
			p = stack[top];
			if (p->right != NULL && p->right!=r) //��ǰ�ڵ㲻Ϊ�գ���û�з��ʹ��ұ߽ڵ�
				p = p->right;
			else {
				top--;   //top������ע���ʱp�Ѿ��洢�˵���node����Ϣ
				printf("%c\n", p->value);
				r = p;      //��¼������ʹ��Ľڵ�
				p = NULL;  //�������¸�ֵ,��������޷��ж���ѭ���������� p != NULL || top != -1
			}
		}
		
	}
}
/*˫ջʵ�֣�flag���¼��ǰ�Ľڵ�񱻷���*/
void postorder2(btnode* tree) {
	if (tree == NULL) {
		printf("tree is empty-- \n");
		return;
	}
	btnode* node_stack[stack_size],*p=tree;
	int top=-1,flag=0;
	int flag_stack[stack_size];
	while (p != NULL || top != -1) {
		//������߽ڵ�
		while (p != NULL) {
			node_stack[++top] = p;
			flag_stack[top] = 0; //��ֵ��Ϊ1��ʾû�з���
			p = p->left;
		}
		p = node_stack[top];
		//�ж��Ƿ��ܹ������ұ߽ڵ�
		flag = flag_stack[top--];
		if (flag == 0) {
			node_stack[++top] = p;
			flag_stack[top] = 1;
			p = p->right;
		}
		else {
			printf("%c\n", p->value);
			p = NULL;
		}
	}
}
void layerorder(btnode* tree) {
/*
 @description: ��η�����
 @return : none
*/
	if (tree == NULL) {
		printf("tree is empty-- \n");
		return;
	}
	btnode* queue[stack_size],*p=tree;
	int front=-1, rear=0;
	queue[0] = p;
	while (front < rear) {
		p = queue[++front];
		printf("%c\n", p->value);
		//������Ҫ�Ƚ���
		if (p->left != NULL) queue[++rear] = p->left;
		if (p->right != NULL) queue[++rear] = p->right;
	};
}
int similar(btnode* a, btnode* b) {
	/*
 @description: �ж��������Ƿ�����
 @return : none
*/
	if (a == NULL && b == NULL)
		return 1;
	else {
		if (similar(a->left, b->left) && similar(a->right, b->right))
			return 1;
		else return 0;
	}
}

void sortTree_insert(btnode **ptree,char item) {
	/*
	 @description: �����������Ĳ���ǵݹ��㷨
	 @return : none
	*/
	btnode* q = *ptree,*p=*ptree;
	/*�����ýڵ�*/
	p = (btnode*)malloc(sizeof(btnode));
	p->value = item;
	p->left = NULL;
	p->right = NULL;

	if (q == NULL) {
		*ptree = p;
		return;
	}
	else {
		while (1) {
			if (item < q->value) {
				if (q->left != NULL)
					q = q->left;
				else {
					q->left = p;
					break;
				}
			}
			else{
				if(q->right!=NULL)
					q = q->right;
				else {
					q->right = p;
					break;
				}
			}
		}
		
	}
}

void sortTree_insert2(btnode** ptree, char item) {
	/*
	 @description: �����������Ĳ���ݹ��㷨
	 @return : none
	*/
	btnode* q = *ptree, * p = *ptree;
	/*�����ýڵ�*/
	p = (btnode*)malloc(sizeof(btnode));
	p->value = item;
	p->left = NULL;
	p->right = NULL;

	if (q == NULL) {
		*ptree = p;
		return;
	}
	else {
		if (item < q->value) 
			sortTree_insert2(q->left, item);
		else 
			sortTree_insert2(q->right, item);

	}
}
btnode* sortTree_create(char item[], int n) {
	btnode* tree = NULL;
	int i;
	if (n > 0)
		for (i = 0; i < n; i++)
			sortTree_insert(&tree, item[i]);
	return tree;
}
btnode* sortTree_search(btnode* tree, char item) {
	while (tree != NULL) {
		if (item == tree->value)
			return tree;
		else if (item < tree->value)
			tree = tree->left;
		else
			tree = tree->right;
	}
	return NULL;
}
btnode* sortTree_search2(btnode* tree, char item) {
	if (tree == NULL)
		return NULL;
	if (item == tree->value)
		return tree;
	else if (item < tree->value)
		sortTree_search2(tree->left,item);
	else
		sortTree_search2(tree->right, item);
}
//
//int main() {
//	char* a = "45126";
//	btnode* tree=case7_1();
//	tree = sortTree_create(a, strlen(a));
//	printf("ǰ�������\n");
//	preorder(tree);
//	btnode *item=sortTree_search(tree, '1');
//	printf("the find result:%c", item->value);
//
//	/*printf("���������\n");
//	inorder(tree);
//	printf("���������\n");
//	postorder(tree);
//	printf("���������\n");
//	postorder2(tree);
//	printf("��α�����\n");
//	layerorder(tree);*/
//
//
//}