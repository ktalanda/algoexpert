def validStartingCity(distances, fuel, mpg):
    numberOfCities = len(distances)
    milesRemaining = 0

    startingCityIndex = 0
    milesRemainingAtStartingCity = 0

    for i in range(1, numberOfCities):
        distanceFromPreviousCity = distances[i - 1]
        fuelAtPreviousCity = fuel[i - 1]
        milesRemaining += fuelAtPreviousCity*mpg - distanceFromPreviousCity

        if milesRemaining < milesRemainingAtStartingCity:
            startingCityIndex = i
            milesRemainingAtStartingCity = milesRemaining

    return startingCityIndex