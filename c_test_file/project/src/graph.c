#include<limits.h>
#define MaxValue INT_MAX
#include <stdio.h>
#include <stdlib.h>
#include "graph.h"
void graph_create_array(int a[][100], int n, int e) {
	/*
	 @description:�Գ�����洢���ڽӱ�
	 @return : none
	*/
	int i, j, k, weigth;
	for(i=0;i<n;i++)
		for (j = 0; j < n; j++) {
			a[i][j] = MaxValue; /* �����ֵ */
		}
	for (k = 0; k < e; k++) {
		scanf_s("%d %d %d \n", &i, &j, &weigth);
		a[i][j] = weigth;
		a[j][i] = weigth;
	}
}
void graph_create_link(ver G[],int n,int e,int edata[][3]) {
	/*
	 @description:����洢���ڽӱ�
	 @return : none
	*/
	int i, begin, end,weight;
	edge *p,*q;

	for (i = 0; i < n; i++) {
		G[i].data = i + 1; /*�ڵ�洢����Ϣ��������*/
		G[i].next = NULL;
	}
	for (i = 0; i < e; i++) {
		begin = edata[i][0];
		end = edata[i][1];
		weight= edata[i][2];
		p = (edge*)malloc(sizeof(edge));
		p->loaction = end - 1;
		p->next = NULL;
		p->weight = weight;
		if (!G[begin - 1].next)
			G[begin - 1].next = p;
		else {
			q = G[begin - 1].next;
			while (q->next)  q = q->next;
			q->next = p;
		}
	}
}
void graph_link_print(ver G[],int n) {
	/*
	 @description:��ӡ����洢��ͼ
	 @return : none
	*/
	int i;
	int ver_data;
	edge* p;
	for (i = 0; i < n; i++) {
		ver_data = G[i].data;
		printf("���㣺%d����·�����յ������", ver_data);
		p = G[i].next;
		while (p) {
			printf("--%d", p->loaction + 1);
			p = p->next;
		}
		printf("\n");
	}
}

void visit_ver(ver node) {
	printf("���ʽڵ㣺%d\n", node.data);
}
/*
 @description: ������ȱ���
 @param : GΪ����洢���ڽӱ�vΪ�����Ķ��㣬visited��¼�ڵ������Ϣ
*/
void DFS(ver G[], int v, int visited[]) {
	if (visited[v] == 1)
		return;
	edge* p;
	visit_ver(G[v]);
	visited[v] = 1;
	p = G[v].next;
	while(p) {
		DFS(G, p->loaction, visited);
		p = p->next;
	}
}
void graph_dfs(ver G[], int n) {
	int i;
	int* visits = (int*)calloc(sizeof(int),n);
	//calloc���� �����ڴ沢��ֵΪ0�����������Ϊ   ��С������
	for (i = 0; i < n; i++)
		if (visits[i] == 0)
			DFS(G, i, visits);
}
/*
 @description: �������ʹ�õݹ��㷨
 @return : none
*/
void BFS(ver G[], int v, int visited[]) {
	if (visited[v] == 1)
		return;
	edge* p = G[v].next;
	//ͨ��ջʵ������ �߽ڵ�Ĵ洢
	int queue[100];
	int front = -1, rear = -1,temp;
	//���ʵ�ǰ�ڵ�
	visit_ver(G[v]);
	visited[v] = 1;
	while (p) {
		//���ʱ߽ڵ�
		temp = p->loaction;
		if (visited[temp] == 0) {
			queue[++rear] = temp;
			visit_ver(G[temp]);
			visited[temp] = 1;
		}
		p = p->next;
	}
	//�ݹ����ʣ��ջ
	while (front != rear) {
		BFS(G, queue[++front],visited);
	}
}
/*
 @description:��ʹ�õݹ��㷨
 @return : none
*/
void BFS2(ver G[], int v, int visited[]) {
	edge* p;
	ver node;
	//����vָ��Ķ���,��ʵ��ֻ�г�ʼ�ڵ���Ҫ��ѭ���ⲿ����
	visit_ver(G[v]);
	visited[v] = 1;
	//ͨ��ջʵ������ �߽ڵ�Ĵ洢
	int queue[100];
	int front = -1, rear = -1, temp;

	queue[++rear] = v;
	while (front != rear) {
		//��ȡ��ǰ����(��ǰ�ڵ�һ���Ѿ������ʹ���)
		node = G[queue[++front]];
		//�������ڵ�
		p = node.next;
		while (p != NULL) {
			temp = p->loaction;
			if (visited[temp] == 0) {
				visit_ver(G[temp]); 
				visited[temp] = 1;
				queue[++rear] = temp;//��ջ
			}
			p = p->next;			
		}
	}
}
void graph_bfs(ver G[], int n) {
	int i;
	int* visits = (int*)calloc(sizeof(int), n);
	//calloc���� �����ڴ沢��ֵΪ0�����������Ϊ   ��С������
	for (i = 0; i < n; i++)
		if (visits[i] == 0)
			BFS2(G, i, visits);
}

void prim_minspant(int GE[6][6], int n) {
	/*
	 @description: ����ķ�㷨��ȡ��С��������GEΪ�����ͼ
	 @return : none
	*/
	//int cost[6];
	//int node_result[6];//��¼cost������Ӧ�Ľڵ�
	int* cost = (int*)calloc(n, sizeof(int));
	int* node_result = (int*)calloc(n, sizeof(int));
	int i,j,mincost=INT_MAX,minIndex;

	
	node_result[0] =0;
	for (i = 0; i < n; i++)
		cost[i] = GE[0][i];
	cost[0] = 0;//��ʼ��������һ���ڵ������С��

	for (int k = 1; k < n;k++) {//ѭ��n-1�ν����нڵ����������
		mincost = INT_MAX;
		for (j = 0; j < n; j++) {
		//Ѱ����С�ĵ�ǰ��������С·��
			if (cost[j]>0 && cost[j] < mincost) { //ע������cost=0
				mincost = cost[j];
				minIndex = j;
			}
		}
		printf("%d,%d\n",node_result[minIndex], minIndex);
		cost[minIndex] = 0; //����С·����Ӧ�Ľڵ������С������0;
		for (i = 0; i < n; i++) {
		//����������·��
			if (GE[minIndex][i] < cost[i]) {
				cost[i] = GE[minIndex][i];
				node_result[i] = minIndex;
			}
		}
	}

}
void short_path(int GE[6][6],int n,int head) {
	/*
	 @description: �Ͻ�˹�����㷨  ��ȡ���·����GEΪ�����ͼ,iΪָ���Ľڵ�
	 @return : none
	*/
	int cost[6]={0};
	int flag[6]={0};//ȫ����ֵΪ0
	int path[6][6]={0};//��¼cost��Ӧ��·��
	int path_len[6] = { 0 };//��¼ÿһ��·���ĳ���
	//int* cost = (int*)calloc(n, sizeof(int));
	//int* node_result = (int*)calloc(n, sizeof(int));
	int i, j, mincost = INT_MAX, minIndex;

	//��ʼ��
	for (i = 0; i < n; i++) {
		cost[i] = GE[head][i];
		path[i][0] = head;
		path_len[i] = 1;
	}
	cost[head] = 0;
	flag[head] = 1;

	for (int k = 1; k < n; k++) {
		//ѡȡ��ǰ���� head����Ľڵ㣬��û�б�����
		mincost = INT_MAX;
		for (j = 0; j < n; j++) {
			if (flag[j]==0 && cost[j] < mincost) {
				mincost = cost[j];
				minIndex = j;
			}
		}
		flag[minIndex] = 1;
		path[minIndex][path_len[minIndex]++] = minIndex;//���벢�޸Ĵ洢��·������
		//·��������·������
		for (i = 0; i < n; i++) {
			if (GE[minIndex][i]< cost[i] - mincost ) {  //ע��ʹ�üӷ��жϻ����
				cost[i] = GE[minIndex][i] + mincost;
				for (j = 0; j < path_len[minIndex]; j++) {
					path[i][j] = path[minIndex][j];
				}
				path_len[i] = path_len[minIndex];
			}
		}
	}
}

//
//int main() {
//	int edata[][3] = {
//		{1,2,1},{1,3,1},{1,4,1},
//		{2,1,1},{2,4,1},
//		{3,1,1},{3,4,1},{3,5,1},
//		{4,1,1},{4,2,1},{4,3,1},{4,5,1},
//		{5,3,1},{5,4,1},
//		{6,7,1},{6,9,1},
//		{7,6,1},{7,8,1},
//		{8,7,1},{8,9,1},
//		{9,6,1},{9,8,1},
//	};
//	int GE[6][6] = {
//		{INT_MAX,16     ,20     ,19     ,INT_MAX,INT_MAX},
//		{16     ,INT_MAX,11     ,INT_MAX,6      ,5      },
//		{20     ,11     ,INT_MAX,22     ,14     ,INT_MAX},
//		{19     ,INT_MAX,22     ,INT_MAX,18     ,INT_MAX},
//		{INT_MAX,6      ,14     ,18     ,INT_MAX,9      },
//		{INT_MAX,5      ,INT_MAX,INT_MAX,9      ,INT_MAX},
//	};
//	ver G[9];
//	graph_create_link(G, 9, 22,edata);
//	graph_link_print(G, 9);
//	graph_link_print(G, 9);
//	printf("---------DFS\n");
//	graph_dfs(G, 9);
//	printf("---------BFS\n");
//	graph_bfs(G, 9);
//	short_path(GE, 6,0);
//}