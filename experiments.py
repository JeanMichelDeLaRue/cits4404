from ant import Ant, AntColony

alpha= [0.1,0.5,1.0]
beta = [1,0.5,0.1]
num_ants = 10
graph = 'example_50.csv'
iteration = [10,50,100]
q0 = [0.1,0.5,0.9]

print "Itertions,Alpha,Beta,Customers, q0,Best Solution"
for a in alpha:
	for b in beta:
		for i in iteration:
			for q in q0:
				aco = AntColony(num_ants,a,b,i,q,graph)
				# print aco._alpha
				# print aco._beta
				aco.run()

