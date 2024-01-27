#!/usr/bin/env python3
"""
Test for the GithubOrgClient class.
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
import client


class TestGithubOrgClient(unittest.TestCase):
    """ Test for the GithubOrgClient class.
        Args:
            unittest (unittest.TestCase): unittest
        Returns:
            Test for correct data retrieval
    """
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """ Test that GithubOrgClient.org returns the correct value.
            Args:
                org_home (str): name of the org
                mock_get_json (function): mock function
            Returns:
                Test for correct data retrieval
        """
        # Instantiate GithubOrgClient with the org_name
        github_org_client = GithubOrgClient(org_name)

        # call the .org property
        github_org_client.org()

        # Assert that get_json was called once with the expected URL
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')
