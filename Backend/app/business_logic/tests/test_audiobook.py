
try:

    from app import create_app
    app = create_app("DevelopmentConfig")

    import unittest

except Exception as e:
    print(f"MODULES CANNOT BE IMPORTED: {e}")

class AudiobookAudioFileTest(unittest.TestCase):

    def test_create_audiobook_audiofile(self):

        tester = app.test_client(self)

        sample_data = {
            "file_type": "audiobook",
            "file_metadata": {
                "title": "I learn from children",
                "duration": "26856",
                "author":"Caroline Pratt",
                "narator":"Becky Ann Baker"
            }
        }

        response = tester.post("/create", json = sample_data)
        
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.content_type, "application/json")

    def test_get_all_audiobook_audiofile(self):

        tester = app.test_client(self)

        response = tester.get("/audiobook")
        
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.content_type, "application/json")

    def test_get_single_audiobook_audiofile(self):

        tester = app.test_client(self)

        response = tester.get("/audiobook/1")
        
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.content_type, "application/json")

    def test_delete_single_audiobook_audiofile(self):

        tester = app.test_client(self)

        response = tester.delete("/audiobook/1")
        
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.content_type, "application/json")

    def test_update_single_audiobook_audiofile(self):

        tester = app.test_client(self)

        sample_data = {
            "file_type": "audiobook",
            "file_metadata": {
                "title": "I learn from children",
                "duration": "26856",
                "author":"Caroline Pratt",
                "narator":"Becky Ann Baker"
            }
        }

        response = tester.put("/audiobook/1", json = sample_data)
        
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.content_type, "application/json")


if __name__ == "__main__":
    unittest.main()