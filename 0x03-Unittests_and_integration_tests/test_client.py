#!/usr/bin/env python3

import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


@parameterized_class([
    {
        "org_payload": payload,
        "repos_payload": repos,
        "expected_repos": [repo["name"] for repo in repos],
        "apache2_repos": [
            repo["name"]
            for repo in repos
            if repo.get("license", {}).get("key") == "apache-2.0"
        ],
    }
    for payload, repos in TEST_PAYLOAD
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient using requests.get"""

    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            mock_resp = MagicMock()
            if url == f"https://api.github.com/orgs/{cls.org_payload['login']}":
                mock_resp.json.return_value = cls.org_payload
            elif url == cls.org_payload["repos_url"]:
                mock_resp.json.return_value = cls.repos_payload
            else:
                mock_resp.json.return_value = {}
            return mock_resp

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        client = GithubOrgClient(self.org_payload["login"])
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        client = GithubOrgClient(self.org_payload["login"])
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )
