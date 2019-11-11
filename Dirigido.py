def CaminoMinimo():
    int Pesos
    int ultimo
    int D
    boolean F
    int s, n  #vertice origen y numero de vertices

def CaminoMinimo(GrafMatPeso gp, int origen):
    n = gp.numeroDeVertices()
    s = origen
    Pesos = gp.matPeso
    ultimo = new int [n]
     D = new int [n]  
    F = new boolean [n]

def caminoMinimos():
    #valores iniciales
    for(int i =0; i<n; i++):
        F[i]=false
        D[i]= Pesos[s][i]
        ultimo[i]=s

    F[s] = true; D[s] = 0;   #Pasos para marcar los n-1 vértices   
    for (int i = 1; i < n; i++) :
         int v = minimo()#/* selecciona vértice no marcado de menor distancia */  
         F[v] = true #actualiza distancia de vértices no marcados    
         for (int w = 1; w < n; w++)    if (!F[w])     if ((D[v] + Pesos[v][w]) < D[w])     {      D[w] = D[v] + Pesos[v][w];      
    ultimo[w] = v
