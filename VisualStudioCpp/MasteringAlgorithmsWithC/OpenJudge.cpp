#include "OpenJudge.h"
#include <Windows.h>
//#include <iostream>
using namespace std;

OpenJudge::OpenJudge()
{
}


OpenJudge::~OpenJudge()
{
}

int OpenJudge::DaysOfYear()
{
	/*
	����������
    ��ʱ������:	1000ms  �ڴ�����:10000kB
    ������
	    ������ݣ����������ж�����
	���룺
		һ�У�һ������
	���
		һ�У�һ������
	��������
	    2008
	�������
    366
	*/
	int year = 0;
	int days = 0;
	scanf_s("%d", &year);
	if (year % 400 == 0)
		days = 366;
	else
	{
		if (year % 4 == 0 && year % 100 != 0)
			days = 366;
		else
			days = 365;
	}
	printf("%d\n", days);
	// Sleep(100);
	return 0;
}


/* Openjude �ύʵ��
#include <iostream>
using namespace std;

int main()
{
	int year = 0;
	int days = 0;
	scanf_s("%d", &year); // �ύʱ��Ϊ scanf
	if (year % 400 == 0)
		days = 366;
	else
	{
		if (year % 4 == 0 && year % 100 != 0)
			days = 366;
		else
			days = 365;
	}
	printf("%d\n", days);
	return 0;
}

int main_MOM() {
	int tzNum = 0;
	int i = 0;
	int tzPrices[10001];
	scanf("%d", &tzNum);
	//memset(tzPrices, 0, sizeof(tzPrices));
	for (int t = 0; t < tzNum; t++)
	{
		while (scanf("%f", &tzPrices[i]))
		{
			++i;
			if (i >= 5)
			{
				for (int j = 0; j <= i; j++)
				{
					if ((i - j) == 5)
					{
						printf("%f ", tzPrices[i] - tzPrices[j]);
					}
				}
			}

		}
		printf("\n");
	}
	return 0;
}

*/