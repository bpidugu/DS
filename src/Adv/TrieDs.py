
#!/usr/local/bin/python
# Shebang
'''
Trie Data Structure
https://albertauyeung.github.io/2020/06/15/python-trie.html/

'''

from email import charset


class TrieNode:
    def __init__(self,char):
        self.char=char
        self.is_end = False
        self.counter = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode('')

    def insert(self,word):
        node = self.root

        for c in word:
            if c in node.children:
                 node = node.children[c]
            else:
                new_node = TrieNode(c)
                node.children[c] = new_node
                node = new_node

        node.is_end = True
        node.counter +=1
    
    def dfs(self, node, prefix):

        if(node.is_end):
            self.output.append((prefix+node.char, node.counter))
        
        for child in node.children.values():
            self.dfs(child, prefix + node.char)
    
    def query(self,x):
        self.output =[]
        node = self.root

        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        self.dfs(node, x[:-1])
        
        return sorted(self.output, key = lambda x: x[1], reverse = True)



if __name__ == "__main__":
    
    t = Trie()
    t.insert("was")
    t.insert("word")
    t.insert("war")
    t.insert("where")
    t.insert("what")
   

    res=t.query("wh")
    print(res)
