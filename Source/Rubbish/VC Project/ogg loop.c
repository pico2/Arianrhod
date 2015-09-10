#include <stdio.h>
void main()
{
	char i;
	int h;
	do
	{
		float a,d,e;
		float b,c;
		printf("请输入要编辑的OGG文件的采样率(单位:KHz):");
Check1:{scanf("%d",&a);
	   if(a<0)
	   {printf("采样率不能小于零!请重新输入(单位:KHz):");
	   goto Check1;}
	   }

Check2:{printf("\n请输入循环的开始时间(单位:秒):");
		scanf("%d",&b);
		if(b<0.0)
	   {printf("开始时间不能小于零!请重新输入(单位:秒):");
	   goto Check2;}
	   }
		printf("\n请输入循环的结束时间(单位:秒):");
Check3:{scanf("%d",&c);
	 if(c<=b)
	 {printf("\n结束时间不大于开始时间,请重新输入(单位:秒):");
	 goto Check3;}
	 }
	 
	 if(c>b)
	 {d=a*b;e=c*a-d;                          
	 printf("loopstart=%f\nlooplength=%f\n\n\n",d,e);
	 }
	 printf("\n是否要继续?(Y or N)");
	 scanf("%d",&i);
	 printf("\n");
	 if(i==121 || i==121) h=1;
	 else h=0;
	}
	while(h==1);
}
