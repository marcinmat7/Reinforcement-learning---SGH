setwd("~/Pulpit/rakietka_v0.1/Parameters/Pokolenie_0")

run_1 <- read.csv("run_1.csv")

results <- NULL

for(i in 1:10){
    name <- paste0("run_", i, "_results.csv")
    tmp <- read.csv(name)
    results <- rbind(results, tmp)    
}

plot(results$X0, 1050 - results$X1, xlim = c(0, 1920), ylim = c(0, 1050))

# srodek <- c(1000, 400)
# promien <- 300
# kat1 <- 0
# kat2 <- 90
# 
# ind <- seq(kat1, kat2, by = 1)
# # angle - x 
# # 360 - 2 * Pi
# 
# plot(srodek[1] + promien * cos(pi * 2 * ind / 360), 
#      srodek[2] + promien * sin(pi * 2 * ind / 360), 
#      xlim = c(0, 1920), 
#      ylim = c(0, 1050), type = "l")




abline(h = 300)

table((1050 - results$X1) <= 300)


i <- 1
params <- NULL
name <- paste0("run_", i, ".csv")
tmp <- read.csv(name)
tmp <- tmp[, -1]
names(tmp) <- 10*(i-1) + 1:10
params <- tmp

for(i in 2:10){
    name <- paste0("run_", i, ".csv")
    tmp <- read.csv(name)
    tmp <- tmp[, -1]
    names(tmp) <- 10*(i-1) + 1:10
    params <- cbind(params, tmp)    
}

number2binary = function(number, noBits) {
    number <- abs(number)
    binary_vector = rev(as.numeric(intToBits(number)))
    if(missing(noBits)) {
        return(binary_vector)
    } else {
        binary_vector[-(1:(length(binary_vector) - noBits))]
    }
}

params_selected <- params[, (1050 - results$X1) <= 300]
params_selected_new <- matrix(data = 0, nrow = 48, ncol = 100)
i <- 1
for (i in 1:50 ) {
    wek <- sample(x = c(1:ncol(params_selected)), size = 2, replace = F)
    a <- round(1e6 * params_selected[, wek[1]])
    b <- round(1e6 * params_selected[, wek[2]])
    j <- 5
    for(j in 1:48) {
        bin1 <- number2binary(a[j], 32)
        bin2 <- number2binary(b[j], 32)
        
        cut <- sample(x = 10:31, size = 1)
        bin1_changed <- bin1
        bin1_changed[1:31 > cut] <- bin2[1:31 > cut] 
        
        bin2_changed <- bin2
        bin2_changed[1:31 > cut] <- bin1[1:31 > cut] 
        
        int1 <- sum(bin1_changed  * 2^(30:0)) / 1e6
        int2 <- sum(bin2_changed  * 2^(30:0)) / 1e6
        
        if(a[j] < 0 ) {int1 <- -int1}
        if(b[j] < 0 ) {int2 <- -int2}
        
        params_selected_new[j, i] <- int1
        params_selected_new[j, 50 + i] <- int2
    }
    
    
}

setwd("~/Pulpit/rakietka_v0.1/Parameters")
for(i in 1:10){
    tmp <- params_selected_new[, c((10*(i-1) + 1):(10 * i) )]
    write.csv(x = tmp, file = paste0("Pokolenie_1/", "run_", i, ".csv"))
}
    
# Pokolenie 1:

setwd("~/Pulpit/rakietka_v0.1/Parameters/Pokolenie_1")



results <- NULL

for(i in 1:10){
    name <- paste0("run_", i, "_results.csv")
    tmp <- read.csv(name)
    results <- rbind(results, tmp)    
}

plot(results$X0, 1050 - results$X1, xlim = c(0, 1920))
abline(v = 1500)

ind1 <- results$X0 >= 1500
ind2 <- F
ind <- ind1 | ind2
table(ind)
setwd("~/Pulpit/rakietka_v0.1/Parameters/Pokolenie_1")
i <- 1
params <- NULL
name <- paste0("run_", i, ".csv")
tmp <- read.csv(name)
tmp <- tmp[, -1]
names(tmp) <- 10*(i-1) + 1:10
params <- tmp

for(i in 2:10){
    name <- paste0("run_", i, ".csv")
    tmp <- read.csv(name)
    tmp <- tmp[, -1]
    names(tmp) <- 10*(i-1) + 1:10
    params <- cbind(params, tmp)    
}

number2binary = function(number, noBits) {
    number <- abs(number)
    binary_vector = rev(as.numeric(intToBits(number)))
    if(missing(noBits)) {
        return(binary_vector)
    } else {
        binary_vector[-(1:(length(binary_vector) - noBits))]
    }
}
prob_ratio <- 0.001
params_selected <- params[, ind]
params_selected_new <- matrix(data = 0, nrow = 48, ncol = 100)
i <- 1
for (i in 1:50 ) {
    wek <- sample(x = c(1:ncol(params_selected)), size = 2, replace = F)
    a <- round(1e6 * params_selected[, wek[1]])
    b <- round(1e6 * params_selected[, wek[2]])
    j <- 5
    for(j in 1:48) {
        bin1 <- number2binary(a[j], 32)
        bin2 <- number2binary(b[j], 32)
        
        cut <- sample(x = 10:31, size = 1)
        bin1_changed <- bin1
        bin1_changed[1:31 > cut] <- bin2[1:31 > cut] 
        x <- rbinom(n = 1, size = 31, prob = prob_ratio)
        if(x > 0){
            y <- sample(x = 1:31, size = x, replace = F)
            bin1_changed[y] <- 1 - bin1_changed[y]
        }
        
        bin2_changed <- bin2
        bin2_changed[1:31 > cut] <- bin1[1:31 > cut] 
        x <- rbinom(n = 1, size = 31, prob = prob_ratio)
        if(x > 0){
            y <- sample(x = 1:31, size = x, replace = F)
            bin2_changed[y] <- 1 - bin2_changed[y]
        }
        
        
        int1 <- sum(bin1_changed  * 2^(30:0)) / 1e6
        int2 <- sum(bin2_changed  * 2^(30:0)) / 1e6
        
        if(a[j] < 0 ) {int1 <- -int1}
        if(b[j] < 0 ) {int2 <- -int2}
        
        params_selected_new[j, i] <- int1
        params_selected_new[j, 50 + i] <- int2
    }
    
    
}
setwd("~/Pulpit/rakietka_v0.1/Parameters")
for(i in 1:10){
    tmp <- params_selected_new[, c((10*(i-1) + 1):(10 * i) )]
    write.csv(x = tmp, file = paste0("Pokolenie_2/", "run_", i, ".csv"))
}




# Pokolenie 2:

setwd("~/Pulpit/rakietka_v0.1/Parameters/Pokolenie_2")



results <- NULL

for(i in 1:10){
    name <- paste0("run_", i, "_results.csv")
    tmp <- read.csv(name)
    results <- rbind(results, tmp)    
}

plot(results$X0, 1050 - results$X1, xlim = c(0, 1920))
abline(h = 350)

ind1 <- results$X0 >= 1500
ind2 <- 1050 - results$X1 >= 347
ind <- ind1 & ind2
table(ind)

setwd("~/Pulpit/rakietka_v0.1/Parameters/Pokolenie_2")
i <- 1
params <- NULL
name <- paste0("run_", i, ".csv")
tmp <- read.csv(name)
tmp <- tmp[, -1]
names(tmp) <- 10*(i-1) + 1:10
params <- tmp

for(i in 2:10){
    name <- paste0("run_", i, ".csv")
    tmp <- read.csv(name)
    tmp <- tmp[, -1]
    names(tmp) <- 10*(i-1) + 1:10
    params <- cbind(params, tmp)    
}

number2binary = function(number, noBits) {
    number <- abs(number)
    binary_vector = rev(as.numeric(intToBits(number)))
    if(missing(noBits)) {
        return(binary_vector)
    } else {
        binary_vector[-(1:(length(binary_vector) - noBits))]
    }
}

params_selected <- params[, ind]
params_selected_new <- matrix(data = 0, nrow = 48, ncol = 100)
i <- 1
for (i in 1:50 ) {
    wek <- sample(x = c(1:ncol(params_selected)), size = 2, replace = F)
    a <- round(1e6 * params_selected[, wek[1]])
    b <- round(1e6 * params_selected[, wek[2]])
    j <- 5
    for(j in 1:48) {
        bin1 <- number2binary(a[j], 32)
        bin2 <- number2binary(b[j], 32)
        
        cut <- sample(x = 10:31, size = 1)
        bin1_changed <- bin1
        bin1_changed[1:31 > cut] <- bin2[1:31 > cut] 
        x <- rbinom(n = 1, size = 31, prob = prob_ratio)
        if(x > 0){
            y <- sample(x = 1:31, size = x, replace = F)
            bin1_changed[y] <- 1 - bin1_changed[y]
        }
        
        bin2_changed <- bin2
        bin2_changed[1:31 > cut] <- bin1[1:31 > cut] 
        x <- rbinom(n = 1, size = 31, prob = prob_ratio)
        if(x > 0){
            y <- sample(x = 1:31, size = x, replace = F)
            bin2_changed[y] <- 1 - bin2_changed[y]
        }
        
        
        int1 <- sum(bin1_changed  * 2^(30:0)) / 1e6
        int2 <- sum(bin2_changed  * 2^(30:0)) / 1e6
        
        if(a[j] < 0 ) {int1 <- -int1}
        if(b[j] < 0 ) {int2 <- -int2}
        
        params_selected_new[j, i] <- int1
        params_selected_new[j, 50 + i] <- int2
    }
    
    
}
setwd("~/Pulpit/rakietka_v0.1/Parameters")
for(i in 1:10){
    tmp <- params_selected_new[, c((10*(i-1) + 1):(10 * i) )]
    write.csv(x = tmp, file = paste0("Pokolenie_3/", "run_", i, ".csv"))
}






# Pokolenie 3:

setwd("~/Pulpit/rakietka_v0.1/Parameters/Pokolenie_3")



results <- NULL

for(i in 1:10){
    name <- paste0("run_", i, "_results.csv")
    tmp <- read.csv(name)
    results <- rbind(results, tmp)    
}

plot(results$X0, 1050 - results$X1, xlim = c(0, 1920))
abline(v = 1500)
abline(h = 800)

ind1 <- results$X0 >= 1500 
ind2 <- 1050 - results$X1 >= 800

# ind2[20:100] <- FALSE

ind <- ind1 | ind2
table(ind2)

setwd("~/Pulpit/rakietka_v0.1/Parameters/Pokolenie_3")
i <- 1
params <- NULL
name <- paste0("run_", i, ".csv")
tmp <- read.csv(name)
tmp <- tmp[, -1]
names(tmp) <- 10*(i-1) + 1:10
params <- tmp

for(i in 2:10){
    name <- paste0("run_", i, ".csv")
    tmp <- read.csv(name)
    tmp <- tmp[, -1]
    names(tmp) <- 10*(i-1) + 1:10
    params <- cbind(params, tmp)    
}

number2binary = function(number, noBits) {
    number <- abs(number)
    binary_vector = rev(as.numeric(intToBits(number)))
    if(missing(noBits)) {
        return(binary_vector)
    } else {
        binary_vector[-(1:(length(binary_vector) - noBits))]
    }
}

params_selected <- params[, ind]
params_selected_new <- matrix(data = 0, nrow = 48, ncol = 100)
i <- 1
for (i in 1:50 ) {
    wek <- sample(x = c(1:ncol(params_selected)), size = 2, replace = F)
    a <- round(1e6 * params_selected[, wek[1]])
    b <- round(1e6 * params_selected[, wek[2]])
    j <- 5
    for(j in 1:48) {
        bin1 <- number2binary(a[j], 32)
        bin2 <- number2binary(b[j], 32)
        
        cut <- sample(x = 10:31, size = 1)
        bin1_changed <- bin1
        bin1_changed[1:31 > cut] <- bin2[1:31 > cut] 
        x <- rbinom(n = 1, size = 31, prob = prob_ratio)
        if(x > 0){
            y <- sample(x = 1:31, size = x, replace = F)
            bin1_changed[y] <- 1 - bin1_changed[y]
        }
        
        bin2_changed <- bin2
        bin2_changed[1:31 > cut] <- bin1[1:31 > cut] 
        x <- rbinom(n = 1, size = 31, prob = prob_ratio)
        if(x > 0){
            y <- sample(x = 1:31, size = x, replace = F)
            bin2_changed[y] <- 1 - bin2_changed[y]
        }
        
        
        int1 <- sum(bin1_changed  * 2^(30:0)) / 1e6
        int2 <- sum(bin2_changed  * 2^(30:0)) / 1e6
        
        if(a[j] < 0 ) {int1 <- -int1}
        if(b[j] < 0 ) {int2 <- -int2}
        
        params_selected_new[j, i] <- int1
        params_selected_new[j, 50 + i] <- int2
    }
    
    
}
setwd("~/Pulpit/rakietka_v0.1/Parameters")
for(i in 1:10){
    tmp <- params_selected_new[, c((10*(i-1) + 1):(10 * i) )]
    write.csv(x = tmp, file = paste0("Pokolenie_4/", "run_", i, ".csv"))
}





# Pokolenie 4:

setwd("~/Pulpit/rakietka_v0.1/Parameters/Pokolenie_4")



results <- NULL

for(i in 1:10){
    name <- paste0("run_", i, "_results.csv")
    tmp <- read.csv(name)
    results <- rbind(results, tmp)    
}

plot(results$X0, 1050 - results$X1, xlim = c(0, 1920))
abline(v = 1500)
abline(h = 800)


ind1 <- results$X0 >= 1500
ind2 <- 1050 - results$X1 >= 800
# ind2[20:100] <- FALSE

ind <- ind1 & ind2
table(ind)

setwd("~/Pulpit/rakietka_v0.1/Parameters/Pokolenie_4")
i <- 1
params <- NULL
name <- paste0("run_", i, ".csv")
tmp <- read.csv(name)
tmp <- tmp[, -1]
names(tmp) <- 10*(i-1) + 1:10
params <- tmp

for(i in 2:10){
    name <- paste0("run_", i, ".csv")
    tmp <- read.csv(name)
    tmp <- tmp[, -1]
    names(tmp) <- 10*(i-1) + 1:10
    params <- cbind(params, tmp)    
}

number2binary = function(number, noBits) {
    number <- abs(number)
    binary_vector = rev(as.numeric(intToBits(number)))
    if(missing(noBits)) {
        return(binary_vector)
    } else {
        binary_vector[-(1:(length(binary_vector) - noBits))]
    }
}

params_selected <- params[, ind]
params_selected_new <- matrix(data = 0, nrow = 48, ncol = 100)
i <- 1
for (i in 1:50 ) {
    wek <- sample(x = c(1:ncol(params_selected)), size = 2, replace = F)
    a <- round(1e6 * params_selected[, wek[1]])
    b <- round(1e6 * params_selected[, wek[2]])
    j <- 5
    for(j in 1:48) {
        bin1 <- number2binary(a[j], 32)
        bin2 <- number2binary(b[j], 32)
        
        cut <- sample(x = 10:31, size = 1)
        bin1_changed <- bin1
        bin1_changed[1:31 > cut] <- bin2[1:31 > cut] 
        x <- rbinom(n = 1, size = 31, prob = prob_ratio)
        if(x > 0){
            y <- sample(x = 1:31, size = x, replace = F)
            bin1_changed[y] <- 1 - bin1_changed[y]
        }
        
        bin2_changed <- bin2
        bin2_changed[1:31 > cut] <- bin1[1:31 > cut] 
        x <- rbinom(n = 1, size = 31, prob = prob_ratio)
        if(x > 0){
            y <- sample(x = 1:31, size = x, replace = F)
            bin2_changed[y] <- 1 - bin2_changed[y]
        }
        
        
        int1 <- sum(bin1_changed  * 2^(30:0)) / 1e6
        int2 <- sum(bin2_changed  * 2^(30:0)) / 1e6
        
        if(a[j] < 0 ) {int1 <- -int1}
        if(b[j] < 0 ) {int2 <- -int2}
        
        params_selected_new[j, i] <- int1
        params_selected_new[j, 50 + i] <- int2
    }
    
    
}

setwd("~/Pulpit/rakietka_v0.1/Parameters")
for(i in 1:10){
    tmp <- params_selected_new[, c((10*(i-1) + 1):(10 * i) )]
    write.csv(x = tmp, file = paste0("Pokolenie_5/", "run_", i, ".csv"))
}




# Pokolenie 5:

setwd("~/Pulpit/rakietka_v0.1/Parameters/Pokolenie_5")



results <- NULL

for(i in 1:10){
    name <- paste0("run_", i, "_results.csv")
    tmp <- read.csv(name)
    results <- rbind(results, tmp)    
}

plot(results$X0, 1050 - results$X1, xlim = c(0, 1920))
abline(v = 1500)
abline(h = 800)
abline(h = 200)

ind1 <- results$X0 >= 1500 & 1050 - results$X1 > 800
ind2 <- 1050 - results$X1 <= 200 & results$X0 > 1000



ind <- ind1
table(ind)
setwd("~/Pulpit/rakietka/Parameters/Pokolenie_5")
i <- 1
params <- NULL
name <- paste0("run_", i, ".csv")
tmp <- read.csv(name)
tmp <- tmp[, -1]
names(tmp) <- 10*(i-1) + 1:10
params <- tmp

for(i in 2:10){
    name <- paste0("run_", i, ".csv")
    tmp <- read.csv(name)
    tmp <- tmp[, -1]
    names(tmp) <- 10*(i-1) + 1:10
    params <- cbind(params, tmp)    
}

number2binary = function(number, noBits) {
    number <- abs(number)
    binary_vector = rev(as.numeric(intToBits(number)))
    if(missing(noBits)) {
        return(binary_vector)
    } else {
        binary_vector[-(1:(length(binary_vector) - noBits))]
    }
}

params_selected <- params[, ind]
params_selected_new <- matrix(data = 0, nrow = 48, ncol = 100)
i <- 1
for (i in 1:50 ) {
    wek <- sample(x = c(1:62), size = 2, replace = F)
    a <- round(1e6 * params_selected[, wek[1]])
    b <- round(1e6 * params_selected[, wek[2]])
    j <- 5
    for(j in 1:48) {
        bin1 <- number2binary(a[j], 32)
        bin2 <- number2binary(b[j], 32)
        
        cut <- sample(x = 10:31, size = 1)
        bin1_changed <- bin1
        bin1_changed[1:31 > cut] <- bin2[1:31 > cut] 
        
        bin2_changed <- bin2
        bin2_changed[1:31 > cut] <- bin1[1:31 > cut] 
        
        int1 <- sum(bin1_changed  * 2^(30:0)) / 1e6
        int2 <- sum(bin2_changed  * 2^(30:0)) / 1e6
        
        if(a[j] < 0 ) {int1 <- -int1}
        if(b[j] < 0 ) {int2 <- -int2}
        
        params_selected_new[j, i] <- int1
        params_selected_new[j, 50 + i] <- int2
    }
    
    
}
setwd("~/Pulpit/rakietka/Parameters")
for(i in 1:10){
    tmp <- params_selected_new[, c((10*(i-1) + 1):(10 * i) )]
    write.csv(x = tmp, file = paste0("Pokolenie_6/", "run_", i, ".csv"))
}

i <- 70
for(i in 70:100) {
    params_selected_new[, i] <- params_selected_new[, i] + rnorm(n = 48, 
                                                                 mean = 0, 
                                                                 sd = sd(params_selected_new[, i]))    
}





