#include "SortAndQuery.h"



SortAndQuery::SortAndQuery()
{
}


SortAndQuery::~SortAndQuery()
{
}

int SortAndQuery::QuickSort()
{
	return 0;
}
/*
#include <iostream>
#include "Calculator.h"
using namespace std;

int main()
{
	double x = 0.0;
	double y = 0.0;
	double result = 0.0;
	char oper = '+';
	cout << "����Ҫ��������֣� " << endl;
	Calculator H;
	while (true)
	{
		cin >> x >> oper >> y;
		result = H.Calculate(x, oper, y);
		cout << "Result is: " << result << endl;
	}

}

void quickSort(int a[], int, int);
void merge(int a[], int low, int mid, int high);
void mergeSort(int a[], int low, int high);
void display(int a[], int len);
void quick_sort(int array[], int low, int high);


int main_bak_cpu()
{
	for (; ; )
	{
		for (int i = 0; i < 960000; i++)
			;
		//sleep(10);
	}
	return 0;
}

int main_bak()
{
	int a, *iptr, *jptr, *kptr;
	//cout << 'The point init addr of : '<< &a;
	iptr = &a;

	std::cout << "Hello Sort World!\n";
	int array[] = { 34,65,12,43,67,5,78,10,3,70 };
	int len = sizeof(array) / sizeof(int);
	display(array, len);
	cout << "The orginal arrayare:" << endl;
	//quickSort(array, 0, len - 1);
	int low, high;
	low = 0;
	high = len - 1;
	//mergeSort(array, low, high);
	quick_sort(array, low, high);
	cout << "The sorted arrayare:" << endl;
	display(array, len);
	system("pause");
	return 0;
}

void display(int array[],int len)
{
	int k;
	for (k = 0; k < len; k++)
		cout << array[k] << ",";
	cout << endl;
}

void quickSort(int s[], int l, int r)
{
	if (l < r)
	{
		int i = l, j = r, x = s[l];
		while (i < j)
		{
			while (i < j && s[j] >= x) // ���������ҵ�һ��С��x����
				j--;
			if (i < j)
				s[i++] = s[j];
			while (i < j && s[i] < x) // ���������ҵ�һ�����ڵ���x����
				i++;
			if (i < j)
				s[j--] = s[i];
		}
		s[i] = x;
		quickSort(s, l, i - 1); // �ݹ����
		quickSort(s, i + 1, r);
	}
}
// ���г���: Ctrl + F5 ����� >����ʼִ��(������)���˵�
// ���Գ���: F5 ����� >����ʼ���ԡ��˵�



void merge(int a[], int low, int mid, int high) {
	// subarray1 = a[low..mid], subarray2 = a[mid+1..high], both sorted
	// �鲢����
	int N = high - low + 1;
	int *b = new int[N]; // ����: Ϊʲô������Ҫһ����ʱ������ b?
	int left = low, right = mid + 1, bIdx = 0;
	while (left <= mid && right <= high) // �鲢
		b[bIdx++] = (a[left] <= a[right]) ? a[left++] : a[right++];
	while (left <= mid) b[bIdx++] = a[left++]; // leftover, if any
	while (right <= high) b[bIdx++] = a[right++]; // leftover, if any
	for (int k = 0; k < N; k++) a[low + k] = b[k]; // copy back
}

void mergeSort(int a[], int low, int high) {
	// Ҫ����������� a[low..high]
	if (low < high) { // base case: low >= high (0 or 1 item)
		int mid = (low + high) / 2;
		mergeSort(a, low, mid); // �ֳ�һ��

		mergeSort(a, mid + 1, high); // �ݹ�ؽ���������
		merge(a, low, mid, high); // ���: �鲢�ӳ���
	}
}

int partition(int a[], int i, int j)
{
	int pivot = a[i];
	int m = i;
	for (int k = i+1; k < j; k++)
	{
		if (a[k] < pivot)
		{
			m++;
			swap(a[k], a[m]);
		}
	}
	swap(a[i], a[m]);
	return m;
}

void quick_sort(int array[], int low, int high)
{
	if (low < high)
	{
		int m = partition(array, low, high);
		quick_sort(array, low, m-1);
		quick_sort(array, m+1, high);
	}

}
*/