#CA5 - PArt A 'Test R Skills'
#Student No: 10352221
#github: https://github.com/AndrewKennyDBS/programming_big_data_10352221.git

#Function 1 - Addition

addition <- function(x,y){
  addresult <- sum(x + y)
  return(addresult)
}

#Function 2 - Subtraction

subtraction <- function(x,y){
  subresult <- (x - y)
  return(subresult)
}

#Function 3 - Multiply

multiply <- function(x,y){
  multresult <- (x * y)
  return(multresult)
}

#Function 4 - Divide

divide <- function(x,y){
  divresult <- (x / y)
  return(divresult)
}

#Function 5 - Exponent

exponent <- function(x,y){
  expresult <- (x ** y)
  return(expresult)
}

#Function 6 - Miles to Kilometre conversion

mile_to_km <- function(x){
  m_to_km_result <- (x * 1.609)
  return(m_to_km_result)
}

#Function 7 - Kilometre to Miles conversion

km_to_mile <- function(x){
  km_to_m_result <- (x / 1.609)
  return(km_to_m_result)
}

#Function 8 - Miles per hour to Metres per second conversion

mph_to_mps <- function(x){
  mph_to_mps_result <- (x * 0.447)
  return(mph_to_mps_result)
}

#Function 9 - Metres per second to Miles per hour conversion

mps_to_mph <- function(x){
  mps_to_mph_result <- (x / 0.447)
  return(mps_to_mph_result)
}

#Function 10 - Miles per hour converts to Feet per second conversion

mph_to_fps <- function(x){
  mph_to_fps_result <- (x * 1.466)
  return(mph_to_fps_result)
}

#Calls for the 10 Functions
addition(5,5)
subtraction(10,5)
multiply(3,4)
divide(10,2)
exponent(3,2)
mile_to_km(10)
km_to_mile(16.09)
mph_to_mps(100)
mps_to_mph(44.7)
mph_to_fps(10)