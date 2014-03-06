#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>

using namespace std;

string revcomp(string);


int main()
{
	string test;
	test = "ATCC";
	string ans;
	ans = revcomp(test);
	cout<<ans<<endl;

	return 0;
}

string revcomp(string bases)
{
	string rev;
	char seqchr[1024];
	strcpy(seqchr,bases.c_str());
	
	for(int i=0;seqchr[i]!='\0';i++)
	{
		if(seqchr[i]=='A')
		{
			rev.append("T");
		}
		else if(seqchr[i]=='T')
		{
			rev.append("A");
		}
		else if(seqchr[i]=='G')
		{
			rev.append("C");
		}
		else if(seqchr[i]=='C')
		{
			rev.append("G");
		}
	}
	std::reverse(rev.begin(),rev.end());
	return rev; 
}


			
