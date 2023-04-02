class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def boruvkaMST(self):
        parent = []
        rank = []
        cheapest = []
        numTrees = self.V
        MSTweight = 0
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
            cheapest.append([-1, -1, float('inf')])

        while numTrees > 1:
            for i in range(len(self.graph)):
                u, v, w = self.graph[i]
                set1 = self.find(parent, u)
                set2 = self.find(parent, v)

                if set1 != set2:
                    if cheapest[set1][2] > w:
                        cheapest[set1] = [u, v, w]
                    if cheapest[set2][2] > w:
                        cheapest[set2] = [u, v, w]

            for node in range(self.V):
                if cheapest[node][0] != -1:
                    u, v, w = cheapest[node]
                    set1 = self.find(parent, u)
                    set2 = self.find(parent, v)
                    if set1 != set2:
                        MSTweight += w
                        self.union(parent, rank, set1, set2)
                        numTrees -= 1
                    cheapest[node] = [-1, -1, float('inf')]

            if numTrees == 1:
                break

        print("Weight of MST is %d" % MSTweight)

g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)


g.boruvkaMST()


#Bu kod, Boruvka algoritmasını kullanarak verilen ağırlıklı bir grafın minimum germe ağacını (MST) bulur. Boruvka algoritması, her adımda grafın birden fazla bileşenine ayrılması durumunda her bileşene en az ağırlıklı kenarlarla bağlı olan düğümleri seçerek birleştirir. Bu işlem, her adımda bileşen sayısının en az yarısı kadar bileşenin birleştiği anlamına gelen bir toplama olanağı ile sonuçlanır.

#__init__ fonksiyonu, grafın düğüm sayısını (vertices) ve grafi depolamak için boş bir liste oluşturur.

#addEdge fonksiyonu, bir düğümden diğerine yönelik bir kenar ve ağırlığını ekler.

#find fonksiyonu, bir düğümün ait olduğu bileşeni bulmak için kullanılır.

#union fonksiyonu, iki düğümü birbirine bağlar ve ait oldukları bileşenleri birleştirir.

#boruvkaMST fonksiyonu, algoritmanın ana adımlarını içerir. En ucuz kenarlar ve düğümler bir listeye eklenir. Ardından, her bileşen için en ucuz kenarlar seçilir ve bileşenler birleştirilir. Bu işlem, sadece bir bileşen kaldığında sonlandırılır. Sonuç olarak, MST'nin ağırlığı yazdırılır.

#g = Graph(4) satırı, 4 düğümlü bir graf oluşturur.

#g.addEdge() satırları, kenar ve ağırlıklarını ekler.

#Son olarak, g.boruvkaMST() komutu, MST'nin ağırlığını hesaplar ve yazdırır.