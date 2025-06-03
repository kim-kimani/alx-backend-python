#!/usr/bin/env python3
"""Unit tests for GithubOrgClient class.
"""

from client import GithubOrgClient
from unittest import TestCase
from unittest.mock import patch, Mock
from parameterized import parameterized


class TestGithubOrgClient(TestCase):
    """Test cases for GithubOrgClient.org property."""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the expected payload."""
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