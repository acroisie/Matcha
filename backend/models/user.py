from werkzeug.security import generate_password_hash
from email_validator import validate_email, EmailNotValidError
import re

class User:
    def __init__(self, username, email, password, first_name, last_name, gender, sexual_preferences, bio, interests, profile_pictures, fame_rating, location):
        self.username = self.validate_username(username)
        self.email = self.validate_email(email)
        self.password = generate_password_hash(password)
        self.first_name = self.sanitize_name(first_name)
        self.last_name = self.sanitize_name(last_name)
        self.gender = self.sanitize_text(gender)
        self.sexual_preferences = self.sanitize_text(sexual_preferences)
        self.bio = self.sanitize_text(bio)
        self.interests = self.sanitize_text(interests)
        self.profile_pictures = self.validate_pictures(profile_pictures)
        self.fame_rating = self.validate_fame_rating(fame_rating)
        self.location = self.sanitize_text(location)

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

    @staticmethod
    def validate_username(username):
        if not re.match("^[a-zA-Z0-9_.-]+$", username) or not 5 <= len(username) <= 20:
            raise ValueError("Invalid username")
        return username

    @staticmethod
    def validate_email(email):
        try:
            valid = validate_email(email)
            return valid.email
        except EmailNotValidError:
            raise ValueError("Invalid email")

    @staticmethod
    def sanitize_name(name):
        return re.sub(r'[^a-zA-Z ]', '', name).strip()

    @staticmethod
    def sanitize_text(text):
        return re.sub(r'[^a-zA-Z0-9,.!? ]', '', text).strip()

    @staticmethod
    def validate_pictures(pictures):
        if not all(re.match(r'https?://[^\s]+', pic) for pic in pictures):
            raise ValueError("Invalid picture URL")
        return pictures

    @staticmethod
    def validate_fame_rating(rating):
        if not isinstance(rating, (int, float)) or not 0 <= rating <= 5:
            raise ValueError("Invalid fame rating")
        return rating
