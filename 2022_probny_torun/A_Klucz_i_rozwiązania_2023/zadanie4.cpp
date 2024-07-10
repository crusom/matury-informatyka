#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
const int n=201;
bool palindrom(string s)
    {
        int i=0, d=s.size()/2;
        while (i<=d){
            if (s[i]!=s[s.size()-i-1]) return false;
            i++;
        }
        return true;
    }

int main()
{
    ifstream we("slowa.txt");
    int ilepalindromow=0;
    string s;
    vector<string> t[n];
    while (!we.eof())
    {
        we>>s;
        if (palindrom(s)) {
                ilepalindromow++;
                t[s.size()].push_back(s);
        }
    }
    we.close();
    cout<<"Liczba palindromow jest rowna "<<ilepalindromow<<endl;
    ofstream wy("rodziny.txt");
    int ilerodzin=0;
    for (int i=0; i<n; i++)
        if (t[i].size()!=0){
                ilerodzin++;
                sort (t[i].begin(), t[i].end());
                for (int j=0; j<t[i].size(); j++) wy<<t[i][j]<<" ";
                wy<<"\n";
        }
    wy.close();
    cout<<"Liczba rodzin palindromow jest rowna "<<ilerodzin;
    return 0;
}
