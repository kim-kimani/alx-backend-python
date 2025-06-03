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