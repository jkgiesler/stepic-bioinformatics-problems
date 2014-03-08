#include <string>
#include <iostream>
#include <cstring>
#include <vector>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;


int skew(string);

int main()
{	
	string userinput;
	cout<<"please enter filename!\n";
	cin>>userinput;
	string line;
	string seq;
	ifstream myfile (userinput.c_str());
	if (myfile.is_open())
	{
		while ( getline (myfile, line) )
		{
		  seq = line;
		}
	}
	else cout<<"cant open file! \n";
	
	seq= seq+seq.substr(0,((int)seq.length()/2));
	int ans;
	ans = skew(seq);
	cout<<ans<<endl;
	return 0;
}

int skew(string seq)
{
	vector<int> skewtable;
	int running = 0;
	
	ofstream myfile ("output.dat");
	if (myfile.is_open())
	{
		for(int i=0; i<seq.length(); i++)
		{
			if((char)seq[i]=='G')
			{
				running++;
			}
			else if((char)seq[i]=='C')
			{
				running--;
			}
			skewtable.push_back(running);
			myfile<<running<<"\n";
		}
		myfile.close();
		system("Rscript mapgraph.R");
	}
	else cout<<"Can't open file! \n";
	int minimum =0;
	int index=0;
	for(int i=0; i<skewtable.size(); i++)
	{
		if (skewtable[i]< minimum)
		{
			index = i;
			minimum = skewtable[i];
			
		}
	}
	
	
	return index;
	
}
