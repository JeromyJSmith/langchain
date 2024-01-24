# flake8: noqa
GET_ISSUES_PROMPT = """
This tool will fetch a list of the repository's issues. It will return the title, and issue number of 5 issues. It takes no input.
"""

GET_ISSUE_PROMPT = """
This tool will fetch the title, body, and comment thread of a specific issue. **VERY IMPORTANT**: You must specify the issue number as an integer in the input.
"""

COMMENT_ON_ISSUE_PROMPT = """
This tool is useful when you need to comment on a GitHub issue. **VERY IMPORTANT**: Your input to this tool MUST strictly follow these rules:

- First you must specify the issue number as an integer in the input
- Then you must place two newlines
- Then you must specify your comment in the input.
"""
CREATE_PULL_REQUEST_PROMPT = """
This tool is useful when you need to create a new pull request in a GitHub repository. **VERY IMPORTANT**: Your input to this tool MUST strictly follow these rules:

- First you must specify the title of the pull request
- Then you must place two newlines
- Then you must write the body or description of the pull request

This tool is useful when you need to create a new pull request in a GitHub repository. **VERY IMPORTANT**: Your input to this tool MUST strictly follow these rules:

- First you must specify the title of the pull request in the input
- Then you must place two newlines
- Then you must write the body or description of the pull request in the input

To reference an issue in the body, put its issue number directly after a #. For example, if you would like to create a pull request called "README updates" with contents "added contributors' names, closes issue #3", you would pass in the following string:

README updates

added contributors' names, closes issue #3
"""
CREATE_FILE_PROMPT = """
This tool is a wrapper for the GitHub API, useful when you need to create a file in a GitHub repository. **VERY IMPORTANT**: Your input to this tool MUST strictly follow these rules:

- First you must specify which file to create by passing a full file path (**IMPORTANT**: the path must not start with a slash)
- Then you must specify the contents of the file

For example, if you would like to create a file called /test/test.txt with contents "test contents", you would pass in the following string:

This tool is a wrapper for the GitHub API, useful when you need to create a file in a GitHub repository. **VERY IMPORTANT**: Your input to this tool MUST strictly follow these rules:

- First you must specify which file to create in the input by passing a full file path (**IMPORTANT**: the path must not start with a slash)
- Then you must specify the contents of the file in the input

For example, if you would like to create a file called /test/test.txt with contents "test contents", you would pass in the following string:
"""

READ_FILE_PROMPT = """
This tool is a wrapper for the GitHub API, useful when you need to read the contents of a file in a GitHub repository. This tool is a wrapper for the GitHub API, useful when you need to read the contents of a file in a GitHub repository. **VERY IMPORTANT**: Your input to this tool MUST strictly follow these rules:

- Simply pass in the full file path of the file you would like to read in the input (**IMPORTANT**: the path must not start with a slash)
"""

UPDATE_FILE_PROMPT = """
This tool is a wrapper for the GitHub API, useful when you need to update the contents of a file in a GitHub repository. **VERY IMPORTANT**: Your input to this tool MUST strictly follow these rules:

- First you must specify which file to modify by passing a full file path (**IMPORTANT**: the path must not start with a slash)
- Then you must specify the old contents which you would like to replace wrapped in OLD <<<< and >>>> OLD
- Then you must specify the new contents which you would like to replace the old contents with wrapped in NEW <<<< and >>>> NEW

This tool is a wrapper for the GitHub API, useful when you need to update the contents of a file in a GitHub repository. **VERY IMPORTANT**: Your input to this tool MUST strictly follow these rules:

- First you must specify which file to modify in the input by passing a full file path (**IMPORTANT**: the path must not start with a slash)
- Then you must specify the old contents which you would like to replace wrapped in OLD <<<< and >>>> OLD in the input
- Then you must specify the new contents which you would like to replace the old contents with wrapped in NEW <<<< and >>>> NEW in the input

For example, if you would like to replace the contents of the file /test/test.txt from "old contents" to "new contents", you would pass in the following string:

test/test.txt

This is text that will not be changed
OLD <<<<
old contents
>>>> OLD
NEW <<<<
new contents
>>>> NEW
"""

DELETE_FILE_PROMPT = """
This tool is a wrapper for the GitHub API, useful when you need to delete a file in a GitHub repository. Simply pass in the full file path of the file you would like to delete. **IMPORTANT**: the path must not start with a slash
"""
