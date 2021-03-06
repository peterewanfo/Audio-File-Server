
try:

    from app import create_app
    app = create_app("DevelopmentConfig")

    import unittest

except Exception as e:
    print(f"MODULES CANNOT BE IMPORTED: {e}")

class SongAudioFileTest(unittest.TestCase):

    def test_create_song_audiofile(self):

        tester = app.test_client(self)

        sample_data = {
            "file_type": "song",
            "file_metadata": {
                "name": "Story of My Life",
                "duration": "248"
            }
        }

        # response = tester.get("/song/1")
        response = tester.post("/create", json = sample_data)
        
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.content_type, "application/json")


    def test_get_all_song_audiofile(self):

        tester = app.test_client(self)

        response = tester.get("/song")
        
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.content_type, "application/json")

    def test_get_single_song_audiofile(self):

        tester = app.test_client(self)

        response = tester.get("/song/1")
        
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.content_type, "application/json")

    def test_delete_single_song_audiofile(self):

        tester = app.test_client(self)

        response = tester.delete("/song/1")
        
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.content_type, "application/json")

    def test_update_single_song_audiofile(self):

        tester = app.test_client(self)

        sample_data = {
            "file_type": "song",
            "file_metadata": {
                "name": "Story of My Life",
                "duration": "248"
            }
        }

        response = tester.put("/song/1", json = sample_data)
        
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.content_type, "application/json")


if __name__ == "__main__":
    unittest.main()