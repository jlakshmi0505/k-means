from cluster import cluster
class KMeans(cluster):
    def __init__(self, k =5, tolerance = 0.0001, max_iterations = 100):
        self.k = k
        self.tolerance = tolerance
        self.max_iterations = max_iterations
        
    def fit(self,data):
        self.centroids=[]
        #randomly initialize the means
        for i in range(self.k):
              self.centroids.append(data[i])
        for i in range(self.max_iterations):
            #assign the data points that they belong to
            #create empty clusters
            clusters=[]
            for j in range(self.k):
                clusters.append([])
                predictions=[]
            for point in data:
                #find distance to all the means values
                distances=[((point-m)**2).sum() for m in self.centroids]
                #find the minimum distance
                minDistance=min(distances)
                #find the mean for which we got the min distance
                l=distances.index(minDistance)
                #add this point to the cluster
                clusters[l].append(point)
                predictions.append(l)
        #calculate the new mean values
            change=False
            for j in range(self.k):
                new_mean=np.average(clusters[j],axis=0)
                if not np.array_equal(self.centroids[j],new_mean):
                    change=True
                self.centroids[j]=new_mean
                if not change:
                    break
        print(predictions)
        print(*self.centroids, sep = ", ")  
    
    
    def fit_extended(self,data,balanced='false'):
        if balanced == 'true':
            self.centroids=[]
            maxval=len(data)/self.k
            #randomly initialize the means
            for i in range(self.k):
                self.centroids.append(data[i])
            for i in range(self.max_iterations):
                clusters=[]
            for j in range(self.k):
                clusters.append([])
                predictions=[]
            for point in data:
                #find distance to all the means values
                distances=[((point-m)**2).sum() for m in self.centroids]
            
                new_arr = distances.copy()
                #sort the array to get min distance
                new_arr.sort()
                #find the mean for which we got the min distance
                l=distances.index(new_arr[0])
                #if maxval already reached assign to second shortest centroid
                if len(clusters[l]) == maxval :
                    l=distances.index(new_arr[1])
                clusters[l].append(point)
                predictions.append(l)
            #calculate the new mean values
            change=False
            for j in range(self.k):
                new_mean=np.average(clusters[j],axis=0)
                if not np.array_equal(self.centroids[j],new_mean):
                    change=True
                self.centroids[j]=new_mean
                if not change:
                    break
        
            print(predictions)
            print(*self.centroids, sep = ", ")              
        else :
            self.fit(X)