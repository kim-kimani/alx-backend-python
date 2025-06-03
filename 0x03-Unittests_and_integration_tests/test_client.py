#!/usr/bin/env python3
"""Unit tests for the GithubOrgClient class.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        # Arrange
        expected_url = f"https://api.github.com/orgs/{org_name}" 
        test_payload = {"login": org_name}

        mock_get_json.return_value = test_payload

        # Act
        client = GithubOrgClient(org_name)
        result = client.org

        # Assert
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, test_payload)
        
    def test_public_repos_url(self):
        """Test _public_repos_url returns correct URL based on mocked org payload."""
        # Define a known org name and expected repo URL
        org_name = "google"
        expected_repos_url = "https://api.github.com/orgs/google/repos" 

        # Create an instance of the client
        client = GithubOrgClient(org_name)

        # Patch the `org` property to return a custom payload
        with patch.object(GithubOrgClient, "org", new_callable=property) as mock_org:
            # Set the return value of the mocked `org` property
            mock_org.return_value = {"repos_url": expected_repos_url}

            # Access the `_public_repos_url` property
            result = client._public_repos_url

        # Assert the returned URL matches expected value
        self.assertEqual(result, expected_repos_url)
        
    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test public_repos returns correct list of repo names."""
        # Define test payload and expected repo names
        test_repos_payload = [
            {"name": "episodes.dart", "license": {"key": "bsd-3-clause"}},
            {"name": "cpp-netlib", "license": {"key": "bsl-1.0"}},
            {"name": "dagger", "license": {"key": "apache-2.0"}},
        ]
        expected_repo_names = [repo["name"] for repo in test_repos_payload]

        # Set mock_get_json to return the test payload
        mock_get_json.return_value = test_repos_payload

        # Create instance of GithubOrgClient
        client = GithubOrgClient("google")

        # Patch _public_repos_url to return a known URL
        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=property
        ) as mock_repos_url:
            # Set the mocked repos URL
            mock_repos_url.return_value = "https://api.github.com/orgs/google/repos" 

            # Call public_repos
            result = client.public_repos()

        # Assertions
        self.assertEqual(result, expected_repo_names)
        mock_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(mock_repos_url.return_value)