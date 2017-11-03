setwd("~/github/cits4404")

customers10 = read.csv(file="results_10_customers.csv",header=TRUE, stringsAsFactors=F)

mean_solution = mean(customers10$Best.Solution)
minimum_combination = customers10[customers10$Best.Solution == min(customers10$Best.Solution),]
max_combination = customers10[customers10$Best.Solution == max(customers10$Best.Solution),]


#calculate the percentage deviation from the mean

(max(max_combination$Best.Solution,minimum_combination$Best.Solution)-mean_solution)/mean_solution * 100


customers25 = read.csv(file="results_25_customers.csv",header=TRUE, stringsAsFactors=F)

mean_solution = mean(customers25$Best.Solution)
minimum_combination = customers25[customers25$Best.Solution == min(customers25$Best.Solution),]
max_combination = customers25[customers25$Best.Solution == max(customers25$Best.Solution),]
(max(max_combination$Best.Solution,minimum_combination$Best.Solution)-mean_solution)/mean_solution * 100

customers50 = read.csv(file="results_50_customers.csv",header=TRUE, stringsAsFactors=F)

mean_solution = mean(customers50$Best.Solution)
minimum_combination = customers50[customers50$Best.Solution == min(customers50$Best.Solution),]
max_combination = customers50[customers50$Best.Solution == max(customers50$Best.Solution),]
(max(max_combination$Best.Solution,minimum_combination$Best.Solution)-mean_solution)/mean_solution * 100



# For a given set of combinations, lets check the iterations

iter10 = customers25[customers25$Itertions==10,]
iter20 = customers25[customers25$Itertions==20,]
iter50 = customers25[customers25$Itertions==50,]
iter100 = customers25[customers25$Itertions==100,]

y = c(mean(iter10$Best.Solution),mean(iter20$Best.Solution),
      mean(iter50$Best.Solution),mean(iter100$Best.Solution))
x = c(10,20,50,100)

tikz(file = "~/github/cits4404/example_convergence.tex", width = 5, height = 3)

plot(x, y,xlab="No. Iterations",ylab="Tour Length",col='red',
     xlim=c(0,100),ylim=c(1400,1600))


ymax = c(max(iter10$Best.Solution),max(iter20$Best.Solution),
      max(iter50$Best.Solution),max(iter100$Best.Solution))
xmax = c(10,20,50,100)


ymin = c(min(iter10$Best.Solution),min(iter20$Best.Solution),
         min(iter50$Best.Solution),min(iter100$Best.Solution))
xmin = c(10,20,50,100)

lines(x, y, xlim=range(x), ylim=range(y), pch=16)
lines(xmax, ymax, xlim=range(xmax), ylim=range(ymax),type='p',col='blue')
lines(xmax, ymax, xlim=range(xmax), ylim=range(ymax))
lines(xmin, ymin, xlim=range(xmin), ylim=range(ymin),type='p',col='green')

tmp = lines(xmin, ymin, xlim=range(xmin), ylim=range(ymin))
dev.copy2eps("~/github/cits4404/example_convergence.tex")
dev.off() 


