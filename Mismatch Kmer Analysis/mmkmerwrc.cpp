/* Barrowing my mmkmer algorithm to calculate it with revcomp 
 * 
 * this will take into account the reverse complement when calculating
 * the most common kmer. it takes a little longer but it could be
 * at predicting.
 * 
 * 
 * making modifications to tie in w/ map distance algorithm
 * 
 * looks like its working pretty well.. awesome!*/
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <fstream>
#include <cmath>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>
using namespace std; //blah blah bad practice i know. IM LAZY TODAY.


vector<string> getkmer(string,int,int); //generate all kmers in a string
void printvector(vector<string>); //prints vector in c++
vector<string> massmutate(vector<string>); //mutates kmers 1 time
bool closeenough(string, string, int); //checks to see if it's legit
int counter(string,string, int); //counts shit up
string revcomp(string); //returns the reverse complement
void findmax(string, int, int); //prints the most frequently occuring kmer
int skew(string); //determines probabilistic location


int main()
{
	string seq="";

	//seq = "CTTGCCGGCGCCGATTATACGATCGCGGCCGCTTGCCTTCTTTATAATGCATCGGCGCCGCGATCTTGCTATATACGTACGCTTCGCTTGCATCTTGCGCGCATTACGTACTTATCGATTACTTATCTTCGATGCCGGCCGGCATATGCCGCTTTAGCATCGATCGATCGTACTTTACGCGTATAGCCGCTTCGCTTGCCGTACGCGATGCTAGCATATGCTAGCGCTAATTACTTAT";
	int k,d;
	k=9;
	d=1;
	
	string userinput;
	cout<<"please enter filename!\n";
	cin>>userinput;
	string line;
	ifstream myfile (userinput.c_str());
	if (myfile.is_open())
	{
		while ( getline (myfile, line) )
		{
		  seq = seq+line;
		}
	}
	else cout<<"cant open file! \n";
	
	seq= seq+seq.substr(0,((int)seq.length()/2));
	int ans;
	ans = skew(seq);
	
	
	
	cout<<seq.substr(ans,500)<<endl;
	findmax(seq.substr(ans,500),k,d);


	return 0;
}

vector<string> getkmer(string sequence,int d,int k)
{	/* this function will return all kmers of the sequence given */
	map<string,int> kmers;
	
	for(int i=0;i<((int)sequence.length()-k);i++)
	{
		string seq;
		seq=sequence.substr(i,k);
		kmers[seq]=0;
	}
	
	vector<string> possible;
	
	
	//turns a map into a vector. stole this from the internets
	//maybe should make a function later as I call this multiple times
	for (map<string,int>::iterator it=kmers.begin();it != kmers.end(); it++)
	{
		possible.push_back(it->first);
	}
	
	return possible;
}


vector<string> massmutate(vector<string> kmers)
{	/* this function takes a vector and returns every possible mutation */
	vector<char> bp;
	bp.push_back('A');
	bp.push_back('T');//is there a better way to set up an array
	bp.push_back('C');//there has to be 
	bp.push_back('G');
	map<string,int> mapmutants;

	string sequence;
	
	
	char tempchar[1024];//need to make char to just alter once base
	for(int z=0;z<(int)kmers.size();z++)
	{
		for(int i=0;i<(int)kmers[z].length();i++)
		{
			sequence=kmers[z]; 
			
			strcpy(tempchar,sequence.c_str());//char can be directly edited..kinda ugly
			
			for(int j=0;j<4;j++)
			{
					tempchar[i] = bp[j];				
					string ansstr(tempchar);
					mapmutants[ansstr]=0;		
					
			}
		}
	}
	
	vector<string> bases;
	
	//turns a map into a vector. stole this from the internets
	//maybe should make a function later as I call this multiple times
	for (map<string,int>::iterator it=mapmutants.begin();it != mapmutants.end(); it++)
	{
		bases.push_back(it->first);
	}

	return bases;
}

void printvector(vector<string> ans)
{ /* This function will print all components of a vector that is passed to it */
    int count;
    for (count=0;count<(int)ans.size();count++)
        {
            cout<<ans[count]<<endl; //standard loop printing everything in the vector
        }
}

bool closeenough(string kmer1, string kmer2, int d)
{ /* logical test to see if two strings are d distance from eachother */
	
	int count = 0;
	int acceptable = (int)kmer1.length()-d;
	
	char kmer1ch[1024];
	char kmer2ch[1024];
	
	strcpy(kmer1ch,kmer1.c_str());
	strcpy(kmer2ch,kmer2.c_str());
	
	for (int i = 0;i < (int)kmer1.length();i++)
	{
		if(kmer1ch[i]==kmer2ch[i])
		{
			count = count + 1;
		}
	}
	
	if (count>=acceptable)
	{
		return true;
	}
	else
	{
		return false;
	}
}

int counter(string sequence,string kmer,int d)
{ /*this function takes the sequence and the kmer and returns how many
	times the kmer occurs in the sequence within a d distance */
	int count = 0;
	int k =(int)kmer.length();
	int end = ((int)sequence.length() - (int)kmer.length() + 1);
	string seq;
	bool ans;
	for(int i = 0;i<end;i++)
	{
		seq = sequence.substr(i,k); //i length k
		ans = closeenough(seq,kmer,d);
		
		if(ans)
		{
			count = count + 1;
		}
	}
	
	return count;
}

string revcomp(string bases)
{ /*this function returns the reverse complement of a given sequence*/
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

void findmax(string seq, int k , int d)
{	/*this function does all the work and prints the top occuring kmer */
	
	std::clock_t start;
	double duration;
	start = std::clock();
	vector<string> kmers = getkmer(seq,d,k);
	
	for(int i=0;i<d;i++)
	// this loop is required to mutate the kmer d times
	{
		kmers = massmutate(kmers);	
	}
	
	vector<int> counts;
	string revcompans;
	double times = 0;
	double tot = 0;
	tot= (double)kmers.size();
	
	//loop captures counts for everything
	for(int i=0;i<(int)kmers.size();i++)
	{
		revcompans = revcomp(kmers[i]);
		counts.push_back(counter(seq,kmers[i],d) + counter(seq,revcompans,d));
		times++;
		//cout<<times/tot<<endl;
	}
		
	vector<string> ans;
	int max = 0;
	for(int i=0;i<(int)counts.size();i++) //loop to get max value
	{ 
		if(counts[i]>max)
		{
			max = counts[i];
		}
	}
	
	for(int i=0;i<(int)counts.size();i++) //loop values which equal max
	{ 
		if(counts[i]==max)
		{
			ans.push_back(kmers[i]);
		}
	}

	printvector(ans);
	
	duration = ( std::clock() - start) / (double) CLOCKS_PER_SEC;
	
	cout<<"Time it took"<<duration<<endl;
}

int skew(string seq)
{ /*calcualtes map distance and returns the lowester area */
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



