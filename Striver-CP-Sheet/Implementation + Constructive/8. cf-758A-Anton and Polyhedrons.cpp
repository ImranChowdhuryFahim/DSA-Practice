#include <bits/stdc++.h>
using namespace std;

int main()
{

    map<string, int> mp;
    mp = {{"Tetrahedron", 4}, {"Cube", 6}, {"Octahedron", 8}, {"Dodecahedron", 12}, {"Icosahedron", 20}};
    int n, count = 0;
    cin >> n;

    string s;

    while (n--)
    {
        cin >> s;
        count += mp[s];
    }
    cout << count << endl;
}