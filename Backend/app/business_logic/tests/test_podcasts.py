
try:

    from app import create_app
    app = create_app("DevelopmentConfig")

    import unittest

except Exception as e:
    print(f"MODULES CANNOT BE IMPORTED: {e}")

class PodcastAudioFileTest(unittest.TestCase):

    def test_create_podcast_audiofile(self):

        tester = app.test_client(self)

        sample_data = {
            "file_type": "podcast",
            "file_metadata": {
                "name": "Story of My Life",
                "duration": "248",
                "host":"One Direction",
                "participants":["james", "peter", "John"]
            }
        }

        response = tester.post("/create", json = sample_data)
        
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.content_type, "application/json")


    def test_get_all_podcast_audiofile(self):

        tester = app.test_client(self)

        response = tester.get("/podcast")
        
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.content_type, "application/json")

    def test_get_single_podcast_audiofile(self):

        tester = app.test_client(self)

        response = tester.get("/podcast/1")
        
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.content_type, "application/json")

    def test_delete_single_podcast_audiofile(self):

        tester = app.test_client(self)

        response = tester.delete("/podcast/1")
        
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.content_type, "application/json")

    def test_update_single_podcast_audiofile(self):

        tester = app.test_client(self)

        sample_data = {
            "file_type": "podcast",
            "file_metadata": {
                "name": "Story of My Life",
                "duration": "248",
                "host":"One Direction",
                "participants":["james", "peter", "John"]
            }
        }

        response = tester.put("/podcast/1", json = sample_data)
        
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.content_type, "application/json")


if __name__ == "__main__":
    unittest.main()