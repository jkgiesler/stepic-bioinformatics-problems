/* This code is an attempt at seeing how much faster C++ is than python
 * at solving the mismatch kmer algorithm which seems to be the closest
 * to an anzer I've found. This was coded pretty dirty and quickly 
 * so don't hate on me for my lazyness...
 * if it works well i'll clean it up. I promise. 
 * 
 * looks like its working pretty well.. awesome!*/
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <cstring>
#include <ctime>
using namespace std; //blah blah bad practice i know. IM LAZY TODAY.


vector<string> getkmer(string,int,int); //generate all kmers in a string
void printvector(vector<string>); //prints vector in c++
vector<string> massmutate(vector<string>); //mutates kmers 1 time
bool closeenough(string, string, int); //checks to see if it's legit
int counter(string,string, int); //counts shit up


int main()
{
	std::clock_t start;
	double duration;
	start = std::clock();
	string seq;
	seq = "ATTCACGGGCAACGACGAGGCAACGACGACGAGGCAACGAAGAGACGACGACGATTCACGACGAACGAACGAGAGACGAACGAGAGACGAACGACGACGAATTCAGAGATTCACGATTCGGCAAGAGGGCAACGAAGAGATTCAGAGACGAAGAGATTCACGAATTCGGCAAGAGATTCGGCAGGCAGGCAAGAGGGCAAGAGATTCGGCAAGAGATTCATTCACGAACGAGGCAAGAGATTCGGCAACGGGCAGGCAACGGGCAACGATTCGGCAACGAGAGATTCAGAGGGCAGGCAACGAACGAAGAGATTCACGGGCAAGAGACGAAGAGGGCAACGAAGAGACG";
	int k,d;
	k=9;
	d=3;
	
	//not test cases
	vector<string> kmers = getkmer(seq,d,k);
	//vector<string> test;
	//test.push_back("AAAA");
	
	for(int i=0;i<d;i++)
	// this loop is required to mutate the kmer d times
	{
		kmers = massmutate(kmers);	
	}
	
	vector<int> counts;
	//loop captures counts for everything
	for(int i=0;i<(int)kmers.size();i++)
	{
		counts.push_back(counter(seq,kmers[i],d));
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
	
	for(int i=0;i<(int)counts.size();i++) //loop finds max values
	{ 
		if(counts[i]==max)
		{
			ans.push_back(kmers[i]);
		}
	}

	printvector(ans);
	
	duration = ( std::clock() - start) / (double) CLOCKS_PER_SEC;
	
	cout<<"Time it took"<<duration<<endl;
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
