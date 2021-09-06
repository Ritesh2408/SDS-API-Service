try:
    from app import app
    import unittest
except Exception as e:
    print(f"Missing modules are: {e}")

class FlaskTest(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/fo")
        statuscode = response.status_code
        self.assertEqual(statuscode,404)

    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/fo")
        self.assertEqual(response.content_type,'text/html; charset=utf-8')



if __name__=="__main__":
    unittest.main()
