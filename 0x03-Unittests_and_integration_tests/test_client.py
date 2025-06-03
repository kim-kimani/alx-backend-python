#!/usr/bin/env python3
"""Integration tests for GithubOrgClient.public_repos using fixtures.
"""

import unittest
from unittest.mock import patch, Mock, MagicMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized_class


@parameterized_class([
    {
        "org_payload": payload,
        "repos_payload": repos,
        "expected_repos": [repo["name"] for repo in repos],
        "apache2_repos": [
            repo["name"] for repo in repos
            if access_nested_map(repo, ("license", "key")) == "apache-2.0"
        ]
    }
    for payload, repos in TEST_PAYLOAD
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient using fixtures."""

    @classmethod
    def setUpClass(cls):
        """Set up mock for requests.get to return fixture payloads."""
        cls.get_patcher = patch("client.requests.get")
        cls.mock_get = cls.get_patcher.start()

        # Define side effect to return appropriate JSON based on URL
        def get_json_side_effect(url):
            if url == cls.org_payload["repos_url"]:
                return cls.repos_payload
            return None

        mock_response = MagicMock()
        mock_response.json.side_effect = get_json_side_effect
        cls.mock_get.return_value = mock_response

    @classmethod
    def tearDownClass(cls):
        """Stop the requests.get patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos returns expected list of repository names."""
        client = GithubOrgClient(self.org_payload["login"])
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos with license='apache-2.0' returns correct subset."""
        client = GithubOrgClient(self.org_payload["login"])
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )
        