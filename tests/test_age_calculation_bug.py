"""
Teeest for age calculation bug 
"""

import pytest
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.user_profile import UserProfile
from src.location import Location


class TestAgeCalculationBug:
    
    def test_age_when_birthday_is_today(self):
        location = Location(city="Boston", state="MA", country="US")
        profile = UserProfile(
            name="Alice Test",
            email="alice@test.com",
            password="Test123!",
            dob="11/07/2000",
            location=location
        )
        
        reference_date = datetime(2025, 11, 7)  # Their birthday
        age = profile.get_age(reference_date)
        
        assert age == 25, f"Expected age 25 on birthday, but got {age}"
    
    def test_age_when_birthday_was_yesterday(self):
        location = Location(city="Portland", state="OR", country="US")
        profile = UserProfile(
            name="Charlie Test",
            email="charlie@test.com",
            password="Test123!",
            dob="11/06/2000",
            location=location
        )
        
        reference_date = datetime(2025, 11, 7)  # Day after birthday
        age = profile.get_age(reference_date)
        
        assert age == 25, f"Expected age 25 (birthday was yesterday), but got {age}"
    
    def test_age_when_birthday_is_tomorrow(self):
        location = Location(city="Seattle", state="WA", country="US")
        profile = UserProfile(
            name="Bob Test",
            email="bob@test.com",
            password="Test123!",
            dob="11/08/2000",
            location=location
        )
        
        reference_date = datetime(2025, 11, 7)  # Day before birthday
        age = profile.get_age(reference_date)
        
        assert age == 24, f"Expected age 24 (birthday is tomorrow), but got {age}"
    
    def test_age_when_birthday_earlier_this_month(self):
        location = Location(city="Denver", state="CO", country="US")
        profile = UserProfile(
            name="Diana Test",
            email="diana@test.com",
            password="Test123!",
            dob="11/01/2000",
            location=location
        )
        
        reference_date = datetime(2025, 11, 7)  # 6 days after birthday
        age = profile.get_age(reference_date)
        
        assert age == 25, f"Expected age 25 (birthday was Nov 1), but got {age}"
    
    def test_age_with_different_date_format(self):
        location = Location(city="Austin", state="TX", country="US")
        profile = UserProfile(
            name="Eve Test",
            email="eve@test.com",
            password="Test123!",
            dob="2000-11-07",
            location=location
        )
        
        reference_date = datetime(2025, 11, 7)  # Their birthday
        age = profile.get_age(reference_date)
        
        assert age == 25, f"Expected age 25 on birthday (YYYY-MM-DD format), but got {age}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

