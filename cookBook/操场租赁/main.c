#include <stdio.h>
#include <stdlib.h>
#define rentCash 10
#define MaxGroundNum 100;  //����100������
typedef struct groundbook{
    int groundID;          //ÿ�����صı��
    int rentTime;         //�ó��ص������ڣ���λ��Сʱ
    int usedTime;          //�ѱ�ʹ��ʱ��
    bool door;              //���ص�ʹ��״̬��on /off
    int rentCash;           //���ص���𣬵�λ��Ԫ
   }groundbook;

typedef struct groundUser{
 string userName;
int userID;
int playTime;             //������ʱ�䣬��λ��Сʱ��Ӧ�ͳ����ѱ�ʹ�õ�ʱ����ͬ
int rentNum;                 //���޵ĳ�����Ŀ��
int rentFirstGoundID;        //���޵ĵ�һ�����صı��
bool playStation;          //�û�ʹ��״̬��on / off

}groundUser;


int main()
{
    printf("Hello world!\n");
    return 0;
}
