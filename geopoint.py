class Finder:
    def __init__(self, database):
        self.database = database
        self.radius_list = [2, 4, 6, 8, 10]
        self.radius_points = [
            {"id": 2, "points": 10},
            {"id": 4, "points": 8},
            {"id": 6, "points": 6},
            {"id": 8, "points": 4},
            {"id": 10, "points": 2}]


    def find_near(self, geopoint, radio_max_meters = 1):
        return self.database.germany_after_geoindex.find({
            "geo": {
                "$near": {
                    "$geometry": geopoint,
                    "$maxDistance": radio_max_meters,
                }
            }
        })


    def get_total_score(self, data):
        total_score = 0
        office_geo = data['geo']
        for office_geo_p in office_geo:
            for radius in self.radius_list:
                near_companies = self.find_near(office_geo, radius*1000)            
                for near_company in near_companies:
                    score = get_score(near_company, radius)
                    total_score += score
        return {'score': total_score} 
                
                
    def get_radius_points(self, radius):
        return (rad_point for rad_point in self.radius_points if rad_point["id"] == radius)


    def get_founded_year_points(self, year):
        if year >= 2002.0:
            return 10
        else:
            return 0


    def get_money_points(self, money):
        if (r'\M+$') in money:
            return 10
        else:
            return 0


    def get_employees_points(self, number):
        if number < 100:
            return 10
        else:
            return 0


    def get_score(self, company, radius):
        return self.get_radius_points(radius) + self.get_founded_year_points(company['founded_year']) + self.get_money_points(company['total_money_raised'])+self.get_employees_points(company['number_of_employees'])


localizer = Finder(db)
df[].apply(localizer.get_total_score)