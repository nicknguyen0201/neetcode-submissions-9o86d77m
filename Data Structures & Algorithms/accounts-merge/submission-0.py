class UnionFind:
    def __init__(self, n):
        self.rank={}
        self.parents={}

        for i in range(n):
            self.rank[i]=0
            self.parents[i]=i
    def find(self,k):
        if self.parents[k]!=k:#compression
            self.parents[k]= self.find(self.parents[k])
        return self.parents[k]
    def union(self,k,v):
        p1, p2=self.find(k),self.find(v)
        if p1==p2:
            return False #not unionable because will create loop
        if self.rank[p1]>self.rank[p2]:
            self.parents[p2]=p1
        elif self.rank[p1]<self.rank[p2]:
            self.parents[p1]=p2
        else:
            self.parents[p1]=p2
            self.rank[p1]+=1
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        e_to_id=defaultdict(int)
        uf = UnionFind(len(accounts))
        for id, emails in enumerate(accounts):
            for email in emails[1:]: #skip the name at [0]
                if email not in e_to_id:
                    e_to_id[email]=id
                else:
                    #so 2 id has the same email, they are 1, so we need to union
                    uf.union(id, e_to_id[email])

        #construct [name, sorted(list of email)]

        #construct id->emails
        id_to_e =defaultdict(list)
        for email, id in e_to_id.items():
            parent_id = uf.find(id) 
            id_to_e[parent_id].append(email)
        
        res= []
        for id, emails in id_to_e.items():
            res.append([accounts[id][0]] + sorted(emails))
        return res
        
        
                
        

                

        