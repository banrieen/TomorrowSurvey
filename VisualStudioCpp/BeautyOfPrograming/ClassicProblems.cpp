#include "pch.h"
#include "ClassicProblems.h"
#include <string>
using namespace std;


// #define rentCash 10
#define MaxGroundNum 100;  //����100������

typedef struct groundbook {
    int groundID;          //ÿ�����صı��
    int rentTime;         //�ó��ص������ڣ���λ��Сʱ
    int usedTime;          //�ѱ�ʹ��ʱ��
    bool door;              //���ص�ʹ��״̬��on /off
    const int rentCash = 10;           //���ص���𣬵�λ��Ԫ
}groundbook;

typedef struct groundUser {
    string userName;
    int userID;
    int playTime;             //������ʱ�䣬��λ��Сʱ��Ӧ�ͳ����ѱ�ʹ�õ�ʱ����ͬ
    int rentNum;                 //���޵ĳ�����Ŀ��
    int rentFirstGoundID;        //���޵ĵ�һ�����صı��
    bool playStation;          //�û�ʹ��״̬��on / off

}groundUser;



rentBaskballGround::rentBaskballGround()
{
}

rentBaskballGround::~rentBaskballGround()
{
}


int rentBaskballGround::rentor()
{
    string name;
    int  pennies;
    int nickels;
    int dimes;
    int quarters;
    int dollars;
    int totalDollars;
    int change;
    int totalCents;
    //Read user' first name.
    std::cout << "Enter your first name : ";
    std::cin >> name;
    //Read  in the count of nickels and pennies.
    cout << "Enter the number of dollars:";
    cin >> dollars;
    cout << "Enter the number of quarters: ";
    cin >> quarters;
    cout << "enter the number of dimes: ";
    cin >> dimes;
    cout << "Enter the nuber of nickels: ";
    cin >> nickels;
    cout << "Enter the number of pennies: ";
    cin >> pennies;
    //compute the total value in cent.
    totalCents = 100 * dollars + 25 * quarters + 10 * dimes + 5 * nickels + pennies;
    //find the value in dollars and change.
    totalDollars = totalCents / 100;
    change = totalCents % 100;
    //display the value in dollars and change.
    cout << "Coin credit: " << name;
    cout << "Dollars:" << totalDollars;
    cout << "Cents: " << change;
    return 0;
}

RandomNumber::RandomNumber()
{
}

RandomNumber::~RandomNumber()
{
}

void display(unsigned int arr[], unsigned SZ)
{
    printf("The num list: \n");
    for (unsigned k = 0; k < SZ; ++k)
    {
        printf(" %d ", arr[k]);
    }
}

unsigned find_minimum(unsigned int arr[], unsigned SZ)
{
    unsigned miniNum = arr[SZ - 1];
    for (unsigned k = 0; k < SZ; ++k)
    {
        if (miniNum <= arr[k])
            miniNum = arr[k];
    };
    return miniNum;
}

unsigned RandomNumber::RandomInt()
{
    unsigned tempRand = 0;
    srand(time(NULL));
    const unsigned MOD = 100, SZ = rand() % MOD;
    unsigned* arr = (unsigned*)malloc(SZ * sizeof(SZ));
    printf("���ɵ����������Ϊ��%d ,�ֽڴ�СΪ: %d \n", SZ, sizeof(SZ));
    for (unsigned k = 0; k < SZ; k++)
    {
        //tempRand = rand() % MOD;
        //if (tempRand)
        //    arr[k] = tempRand;
        cout << k;
        arr[k] = 2;
    }
    display(arr, SZ);  //��ӡ���������

    unsigned min = find_minimum(arr, SZ);
    if (0 != SZ)
        printf("minimum in all; %d \n", arr[min]);

    free(arr);
    return 0;
}