#!/usr/bin/env python3
"""
Test for the GithubOrgClient class.
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


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
        github_org_client.org

        # called once with the expected URL
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ Test that the list of repos is what you expect from the chosen
            payload.
            Args:
                mock_get_json (function): mock function
            Returns:
                Test for correct data retrieval
        """
        # Define the mocked return values for get_json and _public_repos_url
        mock_repos_payload = [{'name': 'repo1'}, {'name': 'repo2'}]
        mock_get_json.return_value = mock_repos_payload
        mock_public_repos_url = 'http://mocked.url/repos'

        # Use patch as a context manager
        # to mock GithubOrgClient._public_repos_url
        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          new_callable=PropertyMock) as mock_repo_url:
            mock_repo_url.return_value = mock_public_repos_url

            # Instantiate the GithubOrgClient
            github_org_client = GithubOrgClient("some_org")

            # Get the public repositories
            public_repos = github_org_client.public_repos()

            # Check that the list of repos matches the mocked payload
            self.assertEqual(public_repos,
                             [repo['name'] for repo in mock_repos_payload])

            # Check that the mocked property and get_json were called once
            mock_repo_url.assert_called_once()
            mock_get_json.assert_called_once_with(mock_public_repos_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, 'my_license', True),
        ({"license": {"key": "other_license"}}, 'my_license', False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """ Test that GithubOrgClient.has_license returns the correct value.
            Args:
                repo (dict): repository
                license_key (str): license key
                expected (bool): expected return value
            Returns:
                Test for correct data retrieval
        """
        # Instantiate GithubOrgClient
        github_org_client = GithubOrgClient("some_org")

        # Call has_license
        has_license = github_org_client.has_license(repo, license_key)

        # Check that the return value is expected
        self.assertEqual(has_license, expected)


if __name__ == '__main__':
    unittest.main()
