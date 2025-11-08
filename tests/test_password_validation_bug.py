
import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.user_profile import UserProfile


class TestPasswordValidationBug:
    
    def test_password_with_uppercase_at_start(self):
        assert UserProfile.valid_password("Abcdef1@") == True, \
            "Password starting with uppercasase should be valid"
    
    def test_password_with_uppercase_in_middle(self):
        assert UserProfile.valid_password("abcDef1@") == True, \
            "Ppassword with uppercas in middle should be valid"
    
    def test_password_with_uppercase_at_end(self):
        assert UserProfile.valid_password("abcdef1@Z") == True, \
            "Password with uppercase at end should be valid"
    
    def test_password_starting_with_digit(self):
        assert UserProfile.valid_password("1abcDef@") == True, \
            "assword starting with digit but containing uppercase should be valid"
    
    def test_password_complex_with_uppercase_middle(self):
        assert UserProfile.valid_password("test1Pass@word") == True, \
            "complex password with uppercase in middle should be valid"
    
    def test_password_multiple_uppercase_not_at_start(self):
        assert UserProfile.valid_password("abc1DEF@gh") == True, \
            "password with multiple uppercase letters ( should be valid"
    
    def test_password_without_uppercase_should_fail(self):
        assert UserProfile.valid_password("abcdef1@") == False, \
            "Password without uppercase should be invalid"
    
    def test_password_without_lowercase_should_fail(self):
        assert UserProfile.valid_password("ABCDEF1@") == False, \
            "Password without lowercase should be invalid"
    
    def test_password_without_digit_should_fail(self):
        assert UserProfile.valid_password("Abcdefg@") == False, \
            "Password without digit should be invalid"
    
    def test_password_without_special_char_should_fail(self):
        assert UserProfile.valid_password("Abcdef1g") == False, \
            "Password without special character should be invalid"
    
    def test_password_too_short_should_fail(self):
        assert UserProfile.valid_password("Abc1@") == False, \
            "Password shorter than 8 characters should be invalid"
    
    def test_all_requirements_met_various_positions(self):

        valid_passwords = [
            "Password1@",     
            "pAssword1@",      
            "password1@A",    
            "12Password@",    
            "p@ssworD1",       
            "PassW0rd!",     
        ]
        
        for password in valid_passwords:
            assert UserProfile.valid_password(password) == True, \
                f"Password '{password}' should be valid (has all requirements)"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

