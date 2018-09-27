#include <stdio.h>
#include <vector>
#include <set>
using namespace std ;

vector<vector<int> > g(1005, vector<int>()) ;

void dfs(int node, vector<bool>& visited){
    visited[node] = 1 ;
    vector<int> nei = g[node] ;
    int size = nei.size() ;
    for(int i=0;i<size;i++){
        if(!visited[nei[i]]){
            dfs(nei[i], visited) ;
        }
    }
}

int main(){
     int n , m ;
     scanf("%d %d", &n, &m) ;
     set<int> nodes ;
     for(int i=0;i<m;i++){
         int u, v ;
         scanf("%d %d", &u, &v) ;
         g[u].push_back(v) ;
         nodes.insert(u) ;
         nodes.insert(v) ;
     }
     int ans = 0 ;
     vector<int> in(1005, 0) ;
     vector<int> out(1005, 0) ;
     for(set<int>::iterator it=nodes.begin();it!=nodes.end();++it){
         vector<bool> visited(1005, 0) ;
         dfs(*it, visited) ;
         int n_out = 0 ;
         for(int i=0;i<1005;i++){
             if(visited[i]){
                 in[i]++ ;
                 n_out++ ;
             }
         }
         out[*it] = n_out ;
     }
    for(set<int>::iterator it=nodes.begin();it!=nodes.end();++it){
        if(out[*it]>in[*it]){
            ans++ ;
        }
    }
    printf("%d\n", ans) ;
}
