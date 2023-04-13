import json


def evaluate(lines):
    pull_request = json.loads(''.join(lines))
    requestor = pull_request['user']['login']
    reviewers = [reviewer['login'] for reviewer in pull_request['requested_reviewers']]
    if requestor in reviewers:
        return {'passed': False, 'message': f'The PR Requestor is also a reviewer. '
                                            f'Requestor: [{requestor}], Reviewer(s): {reviewers}'}
    else:
        return {'passed': True, 'message': f'The PR Requestor is not a reviewer.'
                                           f' Requestor: [{requestor}], Reviewer(s): {reviewers}'}


def description():
    return 'Validates the PR Requestor cannot be a PR Reviewer.'