#!/usr/bin/env python3
"""Integration tests for GithubOrgClient.public_repos using fixtures."""

import unittest
from unittest.mock import patch, Mock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized_class


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos,
    }
    for (
        org_payload,
        repos_payload,
        expected_repos,
        apache2_repos
    ) in TEST_PAYLOAD
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient using fixture data."""

    @classmethod
    def setUpClass(cls):
        """Patch requests.get to mock GitHub API responses."""
        cls.get_patcher = patch("client.requests.get")
        cls.mock_get = cls.get_patcher.start()

        def get_json_side_effect(url):
            if url == cls.org_payload["repos_url"]:
                return cls.repos_payload
            return {}

        mock_response = Mock()
        mock_response.json.side_effect = get_json_side_effect
        cls.mock_get.return_value = mock_response

    @classmethod
    def tearDownClass(cls):
        """Stop patching requests.get."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test that public_repos returns correct repository names."""
        client = GithubOrgClient(self.org_payload["login"])
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos filters repositories by license."""
        client = GithubOrgClient(self.org_payload["login"])
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)
