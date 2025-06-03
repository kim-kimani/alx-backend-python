#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized_class


@parameterized_class([
    {
        "org_payload": payload,
        "repos_payload": repos,
        "expected_repos": [repo["name"] for repo in repos],
        "apache2_repos": [
            repo["name"]
            for repo in repos
            if repo.get("license", {}).get("key") == "apache-2.0"
        ]
    }
    for payload, repos in TEST_PAYLOAD
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient using fixtures."""

    @classmethod
    def setUpClass(cls):
        """Patch get_json to return fixture payloads in sequence."""
        cls.get_patcher = patch("client.get_json", side_effect=[
            cls.org_payload,
            cls.repos_payload
        ])
        cls.mock_get_json = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Stop get_json patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos returns all expected repositories."""
        client = GithubOrgClient(self.org_payload["login"])
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos filters repositories by license."""
        client = GithubOrgClient(self.org_payload["login"])
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )
