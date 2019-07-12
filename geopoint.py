class GeoLocalizer:
    def __init__(self, databse):
        self.database = databse
        self.radiusList = [2, 4, 6, 8, 10]
        self.radiusPoint = [{"id": 2, "points": 10}, {"id": 4, "points": 8}, {
            "id": 6, "points": 6}, {"id": 8, "points": 4}, {"id": 10, "points": 2}]

    def findNear(self, geopoint, radio_max_meters=1000):
        return self.database.germany_after_geoindex.find({
            "geo": {
                "$near": {
                    "$geometry": geopoint,
                    "$maxDistance": radio_max_meters,
                }
            }
        })


    def getTotalScore(self, data):
        totalScore = 0
        officeGeoPoints = data['geo']
        for officeGeoPoint in officeGeoPoints:
            for radius in self.radiusList:
                nearCompanies = self.findNear(officeGeoPoint, radius*1000)            
                for nearCompany in nearCompanies:
                    score = getScore(nearCompany, radius)
                    totalScore+=score
        return {'score': totalScore} 
                
                
                
                

    def getRadiusPoint(self, radius):
        return (radPoint for radPoint in self.radiusPoint if radPoint["id"] == radius)

    def getFoundedYearPoints(self, year):
        if year >= 2002.0:
            return 10
        else:
            return 0

    def getMoneyPoints(self, money):
        if money.find('M'):
            return 10
        else:
            return 0

    def getEmployeesPoints(self, number):
        if number < 100:
            return 10
        else:
            return 0

    def getScore(self, company, radius):
        return self.getRadiusPoint(radius) + self.getFoundedYearPoints(company['founded_year']) + self.getMoneyPoints(company['total_money_raised'])+self.getEmployeesPoints(company['number_of_employees'])


localizer = GeoLocalizer(db)
df[].apply(localizer.getTotalScore)