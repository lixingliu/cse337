import re
import impl
import unittest

class TestPhysicalInfoClass(unittest.TestCase):
    def test_name_type_string(self):
        instance = impl.PhysicalInfo()
        instance.set_name("Jason")
        self.assertIsInstance(instance.name, str)
    
    def test_name_type_bool_throw_valueError(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_name(True)
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
             self.fail("Expected ValueError when setting a name with a boolean value")

    def test_name_type_int_throw_valueError(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_name(54)
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
             self.fail("Expected ValueError when setting a name with a boolean value") 

    def test_name_type_float_throw_valueError(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_name(4.5)
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
             self.fail("Expected ValueError when setting a name with a boolean value")

    def test_name_type_not_string(self):
        instance = impl.PhysicalInfo()
        with self.assertRaises(ValueError):
            instance.set_name(123)

    def test_nane_valid_chars(self):
        instance = impl.PhysicalInfo()
        pattern = r'^[a-zA-Z0-9 -]+$'
        instance.set_name("abc   566 9874354 ---- aaa --- bbb asd ---")
        self.assertTrue(re.match(pattern, instance.name))

    def test_name_invalid_chars_throw_valueError(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_name("abc  @%#!@%^ ---- aaa --- bbb asd ---")
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Expected ValueError when setting a name with a invalid characters")
    def test_at_least_two_alphanumeric_chars1(self):
        instance = impl.PhysicalInfo()
        instance.set_name("ab")
        alphanumeric_count = sum(1 for char in instance.name if char.isalnum())
        self.assertTrue(alphanumeric_count >= 2)
        
    def test_at_least_two_alphanumric_chars2(self):
        instance = impl.PhysicalInfo()
        instance.set_name("1a")
        alphanumeric_count = sum(1 for char in instance.name if char.isalnum())
        self.assertTrue(alphanumeric_count >= 2)

    def test_less_than_two_alphanumric_chars_throw_valueError1(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_name("a")
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Expected ValueError when setting a name with less than 2 alphanumeric characters")

    def test_less_than_two_alphanumric_chars_throw_valueError2(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_name("1")
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Expected ValueError when setting a name with less than 2 alphanumeric characters")

    def test_less_than_two_alphanumric_chars_throw_valueError3(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_name("1@")
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Expected ValueError when setting a name with less than 2 alphanumeric characters")

    def test_less_than_two_alphanumric_chars_throw_valueError4(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_name(" @ ")
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Expected ValueError when setting a name with less than 2 alphanumeric characters")

    def test_at_least_one_alphabet_char(self):
        instance = impl.PhysicalInfo()
        instance.set_name("a999")
        alphabet_count = sum(1 for char in instance.name if char.isalpha())
        self.assertTrue(alphabet_count >= 1)
        
    def test_less_than_one_alphabet_char_throw_ValueError1(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_name("999")
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Expected ValueError when setting a name with less than 1 character from the English Alphabet")

    def test_less_than_one_alphabet_char_throw_ValueError2(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_name(" ")
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Expected ValueError when setting a name with less than 1 character from the English Alphabet")

    def test_less_than_one_alphabet_char_throw_ValueError3(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_name("-----")
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Expected ValueError when setting a name with less than 1 character from the English Alphabet")

    def test_gender_is_type_string(self):
        instance = impl.PhysicalInfo()
        instance.set_gender("F")
        self.assertIsInstance(instance.gender, str)

    def test_gender_is_type_boolean(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_gender(True)
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Expected ValueError when setting a gender with a boolean value")

    def test_gender_is_type_int(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_gender(1)
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Expected ValueError when setting a gender with a int value")

    def test_gender_is_type_float(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_gender(1.5)
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Expected ValueError when setting a gender with a float value")

    def test_gender_is_M(self):
        instance = impl.PhysicalInfo()
        instance.set_gender("M")
        self.assertEqual(instance.gender, "M")

    def test_gender_is_F(self):
        instance = impl.PhysicalInfo()
        instance.set_gender("F")
        self.assertEqual(instance.gender, "F")

    def test_gender_is_not_M_or_F(self):
        instance = impl.PhysicalInfo()
        with self.assertRaises(ValueError):
            instance.set_gender("X")

    def test_height_is_integer(self):
        instance = impl.PhysicalInfo()
        instance.set_height(50)
        self.assertIsInstance(instance.height, int)

    def test_height_is_not_integer(self):
        instance = impl.PhysicalInfo()
        with self.assertRaises(ValueError):
            instance.set_height(2.5)

    def test_height_is_float_should_throw_ValueError(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_height(2.18)
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Expected ValueError when setting a height with a float value")

    def test_height_is_boolean_should_throw_ValueError(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_height(True)
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Expected ValueError when setting a height with a boolean value")

    def test_height_is_string_should_throw_ValueError(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_height("2.18")
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Expected ValueError when setting a height with a string value")

    def test_height_is_between_17_and_84_inclusive(self):
        instance = impl.PhysicalInfo()
        instance.set_height(17)
        self.assertTrue(instance.height >= 17)

    def test_height_is_not_valid_range(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_height(100)
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Expected ValueError when setting a height thats out of range")

    def test_height_is_84(self):
        instance = impl.PhysicalInfo()
        instance.set_height(84)
        self.assertTrue(instance.height <= 84)

    def test_temp_is_float(self):
        instance = impl.PhysicalInfo()
        instance.set_temperature(95.1)
        self.assertEqual(instance.temperature, 95.1)
        self.assertIsInstance(instance.temperature, float)

    def test_temp_is_boolean(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_temperature(True)
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Expected ValueError when setting a temp thats a boolean")

    def test_temp_is_int(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_temperature(97)
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Expected ValueError when setting a temp thats a int")

    def test_temp_is_str(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_temperature("100")
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Expected ValueError when setting a temp thats a str")

    def test_temp_is_105(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_temperature(105.0)
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Expected ValueError when setting a temp thats out of range")

    def test_temp_is_94(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_temperature(94.0)
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Expected ValueError when setting a temp thats out of range")

    def test_temp_is_104(self):
        instance = impl.PhysicalInfo()
        instance.set_temperature(104.0)
        self.assertEqual(instance.temperature, 104.0)
        self.assertIsInstance(instance.temperature, float)

    def test_temp_is_95(self):
        instance = impl.PhysicalInfo()
        instance.set_temperature(95.0)
        self.assertEqual(instance.temperature, 95.0)
        self.assertIsInstance(instance.temperature, float)

    def test_date_is_string(self):
        instance = impl.PhysicalInfo()
        instance.set_date("07-21-2002")
        self.assertEqual(instance.date, "07-21-2002")

    def test_date_is_boolean(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_date(True)
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Expected ValueError when setting a date thats a boolean")
            
    def test_date_is_int(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_date(123)
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Expected ValueError when setting a date thats a int")
        
    def test_date_is_float(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_date(2.5)
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Expected ValueError when setting a date thats a boolean")
        
    def test_date_is_list(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_date([1,2,3])
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Expected ValueError when setting a date thats a list")
        
    def test_date_year_1899(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_date("07-21-1899")
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else: 
            self.fail("Expected ValueError when setting a date thats out of range 1900 and 2100 inclusive")

    def test_date_year_1900(self):
        instance = impl.PhysicalInfo()
        instance.set_date("07-21-1900")
        self.assertEqual(instance.date, "07-21-1900")

    def test_date_year_1901(self):
        instance = impl.PhysicalInfo()
        instance.set_date("07-21-1901")
        self.assertEqual(instance.date, "07-21-1901")

    def test_date_year_2099(self):
        instance = impl.PhysicalInfo()
        instance.set_date("07-21-2099")
        self.assertEqual(instance.date, "07-21-2099")

    def test_date_year_2100(self):
        instance = impl.PhysicalInfo()
        instance.set_date("07-21-2100")
        self.assertEqual(instance.date, "07-21-2100")


    def test_date_year_2101(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_date("07-21-2101")
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else: 
            self.fail("Expected ValueError when setting a date thats out of range 1900 and 2100 inclusive")

    def test_date_format(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_date("07/21/2002")
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Expected ValueError when setting a date thats not proper format")
            
    def test_data_format2(self):
        instance = impl.PhysicalInfo()
        try:
            instance.set_date("99-99-2000")
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Expected ValueError when setting a date thats not in range")
if __name__ == '__main__':
	unittest.main(verbosity=2)

