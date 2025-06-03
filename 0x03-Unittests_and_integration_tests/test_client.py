#!/usr/bin/env python3
"""Unit tests for the GithubOrgClient class.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test org returns correct payload from get_json."""
        expected_url = f"https://api.github.com/orgs/{org_name}"
        test_payload = {"login": org_name}
        mock_get_json.return_value = test_payload
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, test_payload)

    @patch.object(GithubOrgClient, "org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test _public_repos_url returns correct repos URL."""
        org_name = "google"
        expected_url = "https://api.github.com/orgs/google/repos"
        mock_org.return_value = {"repos_url": expected_url}
        client = GithubOrgClient(org_name)
        result = client._public_repos_url
        self.assertEqual(result, expected_url)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test public_repos returns list of repo names."""
        payload = [
            {"name": "episodes.dart", "license": {"key": "bsd-3-clause"}},
            {"name": "cpp-netlib", "license": {"key": "bsl-1.0"}},
            {"name": "dagger", "license": {"key": "apache-2.0"}},
        ]
        expected_names = [item["name"] for item in payload]
        mock_get_json.return_value = payload
        client = GithubOrgClient("google")
        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=PropertyMock
        ) as mock_url:
            mock_url.return_value = (
                "https://api.github.com/orgs/google/repos"
            )
            result = client.public_repos()
        self.assertEqual(result, expected_names)
        mock_url.assert_called_once()
        mock_get_json.assert_called_once_with(mock_url.return_value)


if __name__ == "__main__":
    unittest.main()
