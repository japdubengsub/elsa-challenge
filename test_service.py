import http.client
import json
import unittest


class TestServices(unittest.TestCase):

    def setUp(self):
        self.server1_host = "localhost"
        self.server1_port = 5000

        self.server2_host = "localhost"
        self.server2_port = 5001

    def make_request(self, host, port, endpoint, data):
        headers = {'Content-Type': 'application/json'}
        conn = http.client.HTTPConnection(host, port)
        conn.request("POST", endpoint, json.dumps(data), headers)
        response = conn.getresponse()
        response = json.loads(response.read().decode("utf-8"))
        conn.close()
        return response

    def test_server1_positive_sentiment_text(self):
        data = {"text": "I love this product. It is amazing."}
        response = self.make_request(self.server1_host, self.server1_port, "/analyze_paragraph/", data)
        self.assertEqual(response["label"], "POSITIVE")
        self.assertTrue(0.5 < response["score"] <= 1.0)

    def test_server1_negative_sentiment_text(self):
        data = {"text": "I hate this. It's terrible."}
        response = self.make_request(self.server1_host, self.server1_port, "/analyze_paragraph/", data)
        print(response)
        self.assertEqual(response["label"], "NEGATIVE")
        self.assertTrue(0.5 < response["score"] <= 1.0)

    def test_server1_positive_sentiment_sentence(self):
        data = {"text": "This is fantastic!"}
        response = self.make_request(self.server1_host, self.server1_port, "/analyze_sentence/", data)
        self.assertEqual(response["label"], "POSITIVE")
        self.assertTrue(0.5 < response["score"] <= 1.0)

    def test_server1_negative_sentiment_sentence(self):
        data = {"text": "This is not good at all."}
        response = self.make_request(self.server1_host, self.server1_port, "/analyze_sentence/", data)
        self.assertEqual(response["label"], "NEGATIVE")
        self.assertTrue(0.5 < response["score"] <= 1.0)

    def test_server2_positive_sentiment(self):
        data = {"text": "This is fantastic!"}
        response = self.make_request(self.server2_host, self.server2_port, "/", data)
        self.assertEqual(response["label"], "POSITIVE")
        self.assertTrue(0.5 < response["score"] <= 1.0)

    def test_server2_negative_sentiment(self):
        data = {"text": "This is not good at all."}
        response = self.make_request(self.server2_host, self.server2_port, "/", data)
        self.assertEqual(response["label"], "NEGATIVE")
        self.assertTrue(0.5 < response["score"] <= 1.0)


if __name__ == "__main__":
    unittest.main()
