#define stack_size 100
//A(B(c,D),E(F))
typedef struct anode {
	char value;
	struct anode* left, * right;
}btnode;
/*
 @description: ���ܹ����(Ƕ�����Ŷ���)�����룬���������
 @return : none
*/
btnode* case7_1();
void preorder(btnode* tree);
/*�ǵݹ��㷨�������*/
void inorder(btnode* tree);
/*�ǵݹ�ĺ�����������ջд��*/
void postorder(btnode* tree);
/*˫ջʵ�֣�flag���¼��ǰ�Ľڵ�񱻷���*/
void postorder2(btnode* tree);
void layerorder(btnode* tree);
int similar(btnode* a, btnode* b);

void sortTree_insert(btnode** ptree, char item);
btnode* sortTree_create(char item[], int n);
void sortTree_insert2(btnode** ptree, char item);
btnode* sortTree_search(btnode* tree, char item);
btnode* sortTree_search2(btnode* tree, char item);