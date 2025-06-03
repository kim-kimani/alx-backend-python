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