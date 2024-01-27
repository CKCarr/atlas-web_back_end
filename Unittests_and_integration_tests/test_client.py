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

        # called once with the expected URL
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')

    def test_public_repos_url(self):
        """  Test that the result of _public_repos_url is the expected one.
        Args:
            unittest (unittest.TestCase): unittest
        """
        # Instantiate GithubOrgClient with the org_name
        github_org_client = GithubOrgClient("google")

        # check that the _public_repos_url is equal to the expected URL
        self.assertEqual(github_org_client._public_repos_url,
                         "https://api.github.com/orgs/google/repos")


if __name__ == '__main__':
    unittest.main()
