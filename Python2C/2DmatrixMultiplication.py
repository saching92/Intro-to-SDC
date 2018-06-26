#include<vector>
#include<iostream>

using namespace std;

int main()
{
    
    vector<vector <int> >twodvector1;
    vector<int>singlerow1(3,2);
    
    vector<vector <int> >twodvector2;
    vector<int>singlerow2(3,2);
    
    for(int i=0; i<3;i++)
    {
        
        twodvector1.push_back(singlerow1);
        twodvector2.push_back(singlerow2);
    }
    
    
    for(int row=0; row<twodvector1.size();row++)
    {
        for(int col=0; col<twodvector1[0].size(); col++)
        {
            cout<<twodvector1[row][col]+twodvector2[row][col];
        }
        cout<<endl;
    }
    
    return 0;
    
}
