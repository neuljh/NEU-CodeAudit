#pragma once
#include <stdio.h>
void insert_sort(int k[], int n);
void bin_insert_sort(int k[], int n);
void select_sort(int k[], int n);
void bubble_sort(int k[], int n);
void shell_sort(int k[], int n);

void swap(int* a, int* b);
//����������Ϊ�ָ��ֵ
void Quick(int k[], int left, int right);

void quick_sort(int k[], int n);
//����indexΪi�Ľڵ�
void heap_adjust(int k[], int i, int n);
void heap_sort(int k[], int n);

void print_k(int k[], int n);
