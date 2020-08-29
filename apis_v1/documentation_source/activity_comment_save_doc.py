# apis_v1/documentation_source/activity_comment_save_doc.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-


def activity_comment_save_doc_template_values(url_root):
    """
    Show documentation about activityCommentSave
    """
    required_query_parameter_list = [
        {
            'name':         'voter_device_id',
            'value':        'string',  # boolean, integer, long, string
            'description':  'An 88 character unique identifier linked to a voter record on the server',
        },
        {
            'name':         'api_key',
            'value':        'string (from post, cookie, or get (in that order))',  # boolean, integer, long, string
            'description':  'The unique key provided to any organization using the WeVoteServer APIs',
        },
    ]
    optional_query_parameter_list = [
        {
            'name':         'statement_text',
            'value':        'string',  # boolean, integer, long, string
            'description':  'A text comment.',
        },
        {
            'name':         'visibility_setting',
            'value':        'string',  # boolean, integer, long, string
            'description':  'Two values are currently supported: \'FRIENDS_ONLY\' or \'SHOW_PUBLIC\'.',
        },
    ]

    potential_status_codes_list = [
        {
            'code':         'VALID_VOTER_DEVICE_ID_MISSING',
            'description':  'Cannot proceed. A valid voter_device_id parameter was not included.',
        },
        {
            'code':         'VALID_VOTER_ID_MISSING',
            'description':  'Cannot proceed. A valid voter_id was not found.',
        },
    ]

    try_now_link_variables_dict = {
        # 'organization_we_vote_id': 'wv85org1',
    }

    api_response = '{\n' \
                   '  "status": string,\n' \
                   '  "success": boolean,\n' \
                   '  "date_created": string,\n' \
                   '  "date_last_changed": string,\n' \
                   '  "date_of_notice": string,\n' \
                   '  "id": integer,\n' \
                   '  "activity_post_id": integer,\n' \
                   '  "kind_of_activity": string,\n' \
                   '  "kind_of_seed": string,\n' \
                   '  "new_positions_entered_count": integer,\n' \
                   '  "position_we_vote_id_list": list,\n' \
                   '  "speaker_name": string,\n' \
                   '  "speaker_organization_we_vote_id": string,\n' \
                   '  "speaker_voter_we_vote_id": string,\n' \
                   '  "speaker_profile_image_url_medium": string,\n' \
                   '  "speaker_profile_image_url_tiny": string,\n' \
                   '  "speaker_twitter_handle": string,\n' \
                   '  "speaker_twitter_followers_count": number,\n' \
                   '  "statement_text": string,\n' \
                   '  "visibility_is_public": boolean,\n' \
                   '}'

    template_values = {
        'api_name': 'activityCommentSave',
        'api_slug': 'activityCommentSave',
        'api_introduction':
            "Save a new comment posted to the news feed.",
        'try_now_link': 'apis_v1:activityCommentSaveView',
        'try_now_link_variables_dict': try_now_link_variables_dict,
        'url_root': url_root,
        'get_or_post': 'GET',
        'required_query_parameter_list': required_query_parameter_list,
        'optional_query_parameter_list': optional_query_parameter_list,
        'api_response': api_response,
        'api_response_notes':
            "",
        'potential_status_codes_list': potential_status_codes_list,
    }
    return template_values
