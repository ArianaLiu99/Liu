/*************************************************************************** 
 * Name:A math test
 * Author:LiuBingqing
 * Date:June 2016
 *Description��This program will help elementary students practice math 
***************************************************************************/ 
#include<stdio.h>
#include<stdlib.h>
#include<time.h> 
#include<string.h>
/*！！！！！！！！！！！！The main program！！！！！！！！！！！！！！！！*/
char ID[6] ;
int main()
{
  char a,b;
  int c,i,selection;
  void IDcheck();/*declare the IDcheck function*/
  void Test();/*Declare the Test function*/
  void check();/*Declare the record checking function*/
	
  printf("！！！！！！！！！！！！！！Welcome!！！！！！！！！！！！！！！！！！\n"); 
  IDcheck();
  while(ID!=0)
  {
  printf("\nYou have three choices:\n[1]Start a test:\n[2]Check scores:\n[3]Exit:\n");
  printf("Chose 1 or 2 or 3:\n");
  scanf("%d",&selection);
  switch(selection)
  {
	case 1:
	  Test();/*Turn to the test module*/
	  break;
	case 2:
	  check();/*Turn to the check module*/
	  break;
	case 3:
	  printf("\nThanks for using!Good bye!\n");
	  printf("！！！！！！！！！！！！Goodbye！！！！！！！！！！！！！！！！！\n");
	  exit(1); /*Exit the program*/ 
	default:
	  printf("Please select the number again.\n");
  }
   } 
  
  return 0;
 } 
 
 /*！！！！！！！！！！！！！！！！IDcheck Part！！！！！！！！！！！！！！！！！！*/ 
 void IDcheck()/*The function is used to check the login ID*/
 {
  A:int i,m=0,n=0;
  printf("Please input your four digit ID no: ");
  gets(ID);
  for(i=0;i<2;i++)
  {
    if(ID[i]>='A'&&ID[i]<='Z')
    m++;
  }  
  for (i=2;i<6;i++)
  {
    if(ID[i]>='0'&&ID[i]<='9')
    n++;
  }

  if (m==2&&n==4)
  printf("Login successfully!\n");
  else
  {     
   printf("Error!Please input your ID again.\n"); 
   goto A;
  }
 } 
 /*！！！！！！！！！！！！！！！！Test Part！！！！！！！！！！！！！！！！！！！！*/ 
 void Test()/*The function is used to do the math test*/
 {
  FILE *outFile;
  int i,num1[10],num2[10],n[10],result[10],score=0,Uranswer[10],timelong,t1,t2;
  srand(time(NULL)); 
  printf("The test begins.\n");/*The test module begins*/
  t1=time(NULL);
  for(i=0;i<10;i++)
  {
    n[i]=rand()%4+1;
  
  switch(n[i])
  {
  	case 1:
  	  do
  	  {num1[i]=rand()%100+1;
      num2[i]=rand()%100+1;	
      result[i]=num1[i]+num2[i];
	  }while(result[i]>=100);
  	  printf("%d+%d=",num1[i],num2[i]);
  	  scanf("%d",&Uranswer[i]);
  	  if(Uranswer[i]==result[i])
  	    score+=10;
  	  break;	
  	case 2:
  	  do
  	  {num1[i]=rand()%100+1;
      num2[i]=rand()%100+1;	
      result[i]=num1[i]-num2[i];
	  }while(result[i]<0);
  	  printf("%d-%d=",num1[i],num2[i]);
  	  scanf("%d",&Uranswer[i]);
  	  if(Uranswer[i]==result[i])
  	    score+=10;
  	  break;	 
  	case 3:
  	  do
  	  {num1[i]=rand()%100+1;
      num2[i]=rand()%100+1;	
      result[i]=num1[i]*num2[i];
	  }while(result[i]>=100);
  	  printf("%d*%d=",num1[i],num2[i]);
  	  scanf("%d",&Uranswer[i]);
  	  if(Uranswer[i]==result[i])
  	    score+=10;
  	  break;
  	case 4:
	  do
  	  {num1[i]=rand()%100+1;
      num2[i]=rand()%100+1;	
      result[i]=num1[i]/num2[i];
	  }while(num2[i]==0||num1[i]%num2[i]!=0);
  	  printf("%d/%d=",num1[i],num2[i]);
  	  scanf("%d",&Uranswer[i]);
  	  if(Uranswer[i]==result[i])
  	    score+=10;
  	  break;	
  }
  }
  t2=time(NULL);
  timelong=t2-t1;
  printf("\nThe time you used is %ds.\nYour score is %d.\n\n",timelong,score);
  printf("The right answers are as follows:\nProb.\tCorrect answer.\tUr.answer\n");
  for(i=0;i<10;i++)
  {
  	switch(n[i])
	{
  	case 1:
  	  printf("%d+%d\t%d\t\t%d\n",num1[i],num2[i],result[i],Uranswer[i]);
  	  break;
  	case 2:
  	  printf("%d-%d\t%d\t\t%d\n",num1[i],num2[i],result[i],Uranswer[i]);
  	  break;
  	case 3:
  	  printf("%d*%d\t%d\t\t%d\n",num1[i],num2[i],result[i],Uranswer[i]);
  	  break;
  	case 4:
  	  printf("%d/%d\t%d\t\t%d\n",num1[i],num2[i],result[i],Uranswer[i]);
  	  break; 
	}
  }
  outFile=fopen("record.txt","a");
  if(outFile==NULL)
  {
  printf("\nFailed to open the file.\n");
  exit(1);
  }
  
  fprintf(outFile,"%s\t%d\t%d seconds\n",ID,score,timelong);  
  
  fclose(outFile);
  }
 
 /*！！！！！！！！！！！！！！！！Check Part！！！！！！！！！！！！！！！！！！！！*/ 
 void check()/*The function is used to check the records*/ 
 {
  FILE *inFile;
  int score,timelong;
  
  inFile=fopen("record.txt","r");
  if(inFile==NULL)
  {
    printf("\nFailed to open the file.\n");
  	exit(1);	
  }
  
  printf("Your previous records are:\n");
  while(fscanf(inFile,"%s\t%d\t%d seconds",ID,&score,&timelong)!=EOF)
  {
    printf("%s\t%d\t%d seconds\n",ID,score,timelong);
  }
 }
 
