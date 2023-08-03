#include "graph.h"
#include "binaryTree.h"
#include "linklist.h"
#include "sort.h"
#include "stack.h"
#include<limits.h>
#include<stdio.h>
#include <string.h>
#define MaxValue INT_MAX

int main() {
	//graph ����
	int edata[][3] = {
		{1,2,1},{1,3,1},{1,4,1},
		{2,1,1},{2,4,1},
		{3,1,1},{3,4,1},{3,5,1},
		{4,1,1},{4,2,1},{4,3,1},{4,5,1},
		{5,3,1},{5,4,1},
		{6,7,1},{6,9,1},
		{7,6,1},{7,8,1},
		{8,7,1},{8,9,1},
		{9,6,1},{9,8,1},
	};
	int GE[6][6] = {
		{INT_MAX,16     ,20     ,19     ,INT_MAX,INT_MAX},
		{16     ,INT_MAX,11     ,INT_MAX,6      ,5      },
		{20     ,11     ,INT_MAX,22     ,14     ,INT_MAX},
		{19     ,INT_MAX,22     ,INT_MAX,18     ,INT_MAX},
		{INT_MAX,6      ,14     ,18     ,INT_MAX,9      },
		{INT_MAX,5      ,INT_MAX,INT_MAX,9      ,INT_MAX},
	};
	ver G[9];
	graph_create_link(G, 9, 22,edata);//����
	graph_link_print(G, 9);//��ӡ�������ʽ�洢ͼ
	printf("---------DFS\n");
	graph_dfs(G, 9);
	printf("---------BFS\n");
	graph_bfs(G, 9);
	short_path(GE, 6, 0);
	//queue ����
	char* a = "45126";

	btnode* tree=case7_1();
	tree = sortTree_create(a, strlen(a));
	printf("ǰ�������\n");
	preorder(tree);
	btnode *item=sortTree_search(tree, '1');
	printf("the find result:%c", item->value);
	
	/*printf("���������\n");
	inorder(tree);
	printf("���������\n");
	postorder(tree);
	printf("���������\n");
	postorder2(tree);
	printf("��α�����\n");
	layerorder(tree);*/
}