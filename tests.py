import unittest

import server

class FlaskTests(unittest.TestCase):

    def setUp(self):

        self.client = server.app.test_client()
        server.app.config['TESTING'] = True
    
    def test_homepage(self):

        result = self.client.get("/")
        self.assertIn(b"Welcome",result.data)
    
    def test_imagepage(self):

        image_info = {"f.filename":"se6hfub7w1121.jpeg"}

        result = self.client.post("/show_image", data=image_info,
                                  follow_redirects=True)
        
        self.assertNotIn(b"Your Image", result.data)


if __name__ == "__main__":
    unittest.main()