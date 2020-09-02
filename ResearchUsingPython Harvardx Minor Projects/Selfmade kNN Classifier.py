
import numpy as np
import random
import matplotlib.pyplot as plt
import scipy.stats as ss

# #Find distance between p1 and p2
# def distance(p1,p2):

#     # print(p2-p1)
#     # print(np.power(p2-p1, 2))
#     ans = np.sqrt(np.sum(np.power(p2-p1, 2)))            #using pythagoras way : normal pythagoras theorem
#     return ans

# p1 = np.array([2,2])            #Defining points
# p2 = np.array([3,3])
# # print(distance(p1,p2))



#  #COMPUTING MAJORITY VOTES

# # def majority_votes(votes):
# #     vote_counts = {}
# #     for vote in votes:          
# #         if vote in vote_counts:
# #             vote_counts[vote] += 1     
# #         else:
# #             vote_counts[vote] = 1
# #     return vote_counts

# # votes = [1,2,3,1,2,3,3,2]
# # vote_counts = majority_votes(votes)
# # print(vote_counts)

# # #FINDING MAXIMUM COUNT

# # winners = []
# # max_count = max(vote_counts.values())
# # for vote,count in vote_counts.items():
# #     if count == max_count:
# #         winners.append(vote)

# # print(winners)

# # # print(max(vote_counts))   #print the maximum valued key
# # # print(max(vote_counts.keys()))     #same as above

# # # loop over all entries in the dictionary and find which entry/entries corresponds to the maximum count.

# # FINALLY COMPUTING MAJORITY VOTES:  

# import numpy as np
# import random

# def majority_vote(votes):
#     vote_counts = {}
#     for vote in votes:          
#         if vote in vote_counts:
#             vote_counts[vote] += 1     
#         else:
#             vote_counts[vote] = 1
    
#     winners = []
#     max_count = max(vote_counts.values())
#     for vote,count in vote_counts.items():
#         if count == max_count:
#             winners.append(vote)
        
#     return random.choice(winners)     #in case of tie


# import scipy.stats as ss
# def majority_vote_short(votes):
#     mode,count = ss.mstats.mode(votes)
#     print(ss.mstats.mode(votes))
#     return mode

# votes = [1,2,3,1,2,3,3,2,3,2,1,3,2,2,2,2]
# # print(majority_vote(votes))
# # print(majority_vote_short(votes))

# #Finding Nearest Neighbors

# #TASKS
# #1. The first is to loop over all points.
# #2. For any given point, compute the distance between point P,that we're hoping to classify, and every other point.
# #3. Sort distances and return those k points that are nearest to point p.

# points = np.array([[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]])  #NumPy array expects as input just one list
# p = np.array([2.5,2])

# def find_nearest_neighbours(p,points,k):    # k is value of nearest neighbours we want
#     """ find the k nearest neighbors of point p"""
#     distances = np.zeros(points.shape[0]) #empty array to hold all of our distances have the same number of elements as we have rows in our points array
#     for i in range(len(distances)):
#         distances[i] = distance(p,points[i])
#     ind = np.argsort(distances)  
#     return ind[:k]    #argsort return sorted indices and not arrays


# index = find_nearest_neighbours(p,points,3)
# # print(points[index])

# #function to predict the class of our new point p
# def knn_predict(p,points,outcomes,k):
# #1. find k nearest neighbors.
# #2. To predict the class or category of p
#     ind = find_nearest_neighbours(p,points,k)
#     return majority_vote_short(outcomes[ind])
# #outcomes : classes of the points that are specified in the input variable points

# outcomes = np.array([0,0,0,0,1,1,1,1,1])        #9 point outcomes for 9 points  #Class 0 and class 1
# result = knn_predict(p,points,outcomes,3)
# # print(result)

# import matplotlib.pyplot as plt
# plt.plot(points[:,0],points[:,1],"ro")       #plot all of x axis and y axis data 
# plt.plot(p[0],p[1],"bo")
# # plt.show()

#GENERATING SYNTHETIC DATA        #PROBLEM IN THIS

# ss.norm(0,1).rvs((5,2))    #CLASS 0  #mean 0 , standard = 1 , array of 5 rows and 2 coloumn
# ss.norm(1,1).rvs((5,2))     #CLASS 1
#concatenating these 2 arrays 

def generate_synthetic_data(n=20):
    """ create two sets of points from bivariate normal distributions"""
    points = np.concatenate((ss.norm(0,1).rvs((n,2)),ss.norm(1,1).rvs((n,2))), axis = 0)  #generated points
    outcomes = np.concatenate( (np.repeat(0,20), np.repeat(1,20)),axis = 0)
    return (points,outcomes)
    #GENERATING OUTCOMES
# np.repeat(0,n)
# np.repeat(1,n)   #repeat 1 n times
       
    plt.figure()
    plt.plot(points[:n,0],points[:n,1],"ro")
    plt.plot(points[n:,0],points[n:,1],"bo")
    plt.show()
    plt.savefig("bivardata.pdf")


generate_synthetic_data(n=20)
print(generate_synthetic_data())
plt.show()
 
#Making a Prediction Grid

def make_prediction_grid():
    #We'll start by specifying the x values of our grid
    

