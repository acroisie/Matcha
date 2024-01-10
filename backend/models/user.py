from werkzeug.security import generate_password_hash

class User:
	def __init__(self, username, email, password, first_name, last_name, gender, sexual_preferences, bio, interests, profile_pictures, fame_rating, location):
		self.username = username
		self.email = email
		self.password = generate_password_hash(password)
		self.first_name = first_name
		self.last_name = last_name
		self.gender = gender
		self.sexual_preferences = sexual_preferences
		self.bio = bio
		self.interests = interests
		self.profile_pictures = profile_pictures
		self.fame_rating = fame_rating
		self.location = location

	def to_json(self):
		return {
			"username": self.username,
			"email": self.email,
			"password": self.password,
			"first_name": self.first_name,
			"last_name": self.last_name,
			"gender": self.gender,
			"sexual_preferences": self.sexual_preferences,
			"bio": self.bio,
			"interests": self.interests,
			"profile_pictures": self.profile_pictures,
			"fame_rating": self.fame_rating,
			"location": self.location
		}