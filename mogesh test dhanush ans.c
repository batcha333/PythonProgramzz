#include<stdio.h>
#include<stdbool.h>
#include<malloc.h>
int chargingSmartPhone(int initCharge, int finalCharge)
{
int rate,count=0;
    while(initCharge<finalCharge)
    {
    if((initCharge>=0)&&(initCharge<=10))
    {
        rate=10;
        initCharge=initCharge + rate;
        count++;
    }
    if((initCharge>=11)&&(initCharge<=230))
    {
        rate=5;
        initCharge=initCharge + rate;
        count++;
    }
    if((initCharge>=231)&&(initCharge<=559))
    {
        rate=8;
        initCharge=initCharge + rate;
        count++;
    }
    if((initCharge>=560)&&(initCharge<=1009))
    {
        rate=2;
        initCharge=initCharge + rate;
        count++;
    }
    if((initCharge>=1010)&&(initCharge<=5000))
    {
        rate=7;
        initCharge=initCharge + rate;
        count++;
    }
    if((initCharge>=5001)&&(initCharge<=10000))
    {
        rate=8;
        initCharge=initCharge + rate;
        count++;
    }
    if((initCharge>=10001)&&(initCharge<=1000000000))
    {
        rate=3;
        initCharge=initCharge + rate;
        count++;
    }
    }
   
    return count;
}	
int main()
{
	int T;
	int t_i;
	int initCharge;
	int finalCharge;
	scanf("%d",&T);
	for(t_i=0;t_i<T;t_i++)
	{
		int initCharge;
		scanf("%d",&initCharge);
		int finalCharge;
		scanf("%d",&finalCharge);
		int out_=chargingSmartPhone(initCharge,finalCharge);
		printf("%d",out_);
		printf("\n");
	}
}